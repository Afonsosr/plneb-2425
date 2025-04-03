from bs4 import BeautifulSoup
import json


db_file = open("doencas__.json",encoding="utf-8")
db = json.load(db_file)

db_file.close()


for elem in db:
    div = db[elem]["content"]
    soup = BeautifulSoup(div, "html.parser")

    info = []
    titu = "Intro"
    tex = ""
   
    for conteudo_div in soup.find_all(["h2","p","ul"]):
        if conteudo_div.name == "h2":
            if tex:
                info.append((titu,tex.strip()))
            strong_tag = conteudo_div.find("strong")
            titu = strong_tag.text.strip() if strong_tag else "Untitled"
            tex = ""
        elif conteudo_div.name == "p":
            tex += conteudo_div.text.strip() + " "
        elif conteudo_div.name == "ul":
            list_items = [li.get_text(strip=True) for li in conteudo_div.find_all("li")]
            tex += ", ".join(list_items) + " "         

    if tex:
        info.append((titu,tex.strip()))

    del db[elem]["content"]

    d_info = dict(info)
    db[elem].update(d_info)


a = open("doencas_tpc.json","w",encoding="utf-8")
json.dump(db,a,indent=4,ensure_ascii=False)
a.close()