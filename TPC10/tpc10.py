import requests
from bs4 import BeautifulSoup
import json
from tqdm import tqdm

BASE_URL = "https://revista.spmi.pt"
CAMINHO_ARQUIVO = f"info_artigos.json"
ARTIGOS_EXTRAIDOS = []

def obter_edicoes(limit=3):
    """Entra no arquivo da revista e retorna os links das últimas edições."""
    pagina = requests.get(f"{BASE_URL}/index.php/rpmi/issue/archive")
    soup = BeautifulSoup(pagina.text, "html.parser")

    edicoes = []
    for tag in soup.select("a.title")[:limit]:
        edicoes.append({
            "titulo": tag.get_text(strip=True),
            "url": tag['href'] if tag['href'].startswith("http") else BASE_URL + tag['href']
        })
    return edicoes

def processar_edicao(edicao):
    """Processa uma edição da revista e retira os dados de cada um dos artigos."""
    print(f"\n Edição: {edicao['titulo']}")
    pagina = requests.get(edicao["url"])
    soup = BeautifulSoup(pagina.text, "html.parser")
    artigos = soup.find_all("div", class_="obj_article_summary")

    for artigo in tqdm(artigos, desc="  A processar artigos", leave=False):
        tag_titulo = artigo.find("h3", class_="title").find("a")
        titulo = tag_titulo.get_text(strip=True)
        url_artigo = tag_titulo["href"] if tag_titulo["href"].startswith("http") else BASE_URL + tag_titulo["href"]

        autores_tag = artigo.find("div", class_="authors")
        autores = autores_tag.get_text(strip=True) if autores_tag else "Não identificado"

        detalhes = extrair_detalhes_artigo(url_artigo)
        dados_artigo = {
            "titulo": titulo,
            "autores": autores,
            "url": url_artigo,
            "resumo": detalhes["resumo"],
            "doi": detalhes["doi"],
            "palavras_chave": detalhes["palavras_chave"],
            "data_publicacao": detalhes["data"]
        }
        ARTIGOS_EXTRAIDOS.append(dados_artigo)

def extrair_detalhes_artigo(link):
    """Extrai detalhes da página do artigo."""
    dados = {
        "resumo": {},
        "palavras_chave": [],
        "doi": "",
        "data": ""
    }
    resposta = requests.get(link)
    soup = BeautifulSoup(resposta.text, "html.parser")

    
    sec_keywords = soup.find("section", class_="item keywords")
    if sec_keywords:
        span = sec_keywords.find("span")
        if span:
            raw = span.get_text()
            dados["palavras_chave"] = [x.strip() for x in raw.replace("Palavras-chave:", "").split(",") if x.strip()]

    
    sec_abstract = soup.find("section", class_="item abstract")
    if sec_abstract:
        for par in sec_abstract.find_all("p"):
            negrito = par.find("strong")
            if negrito:
                chave = negrito.get_text(strip=True).strip(":")
                negrito.extract()
                texto = par.get_text(strip=True)
                dados["resumo"][chave] = texto
            else:
                dados["resumo"]["geral"] = par.get_text(strip=True)

    
    sec_doi = soup.find("section", class_="item doi")
    if sec_doi:
        link_doi = sec_doi.find("a")
        if link_doi:
            dados["doi"] = link_doi["href"]

    
    data_tag = soup.find("div", class_="item published")
    if data_tag:
        span = data_tag.find("span")
        if span:
            dados["data"] = span.get_text(strip=True)

    return dados

def guardar_json():
    """Escreve os dados num arquivo JSON."""
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(ARTIGOS_EXTRAIDOS, f, ensure_ascii=False, indent=2)
    print(f"\n {len(ARTIGOS_EXTRAIDOS)} artigos exportados para '{CAMINHO_ARQUIVO}'")

def principal():
    edicoes = obter_edicoes(limit=3)
    for edicao in edicoes:
        processar_edicao(edicao)
    guardar_json()

if __name__ == "__main__":
    principal()
