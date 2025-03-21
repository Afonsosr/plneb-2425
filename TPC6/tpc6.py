from flask import Flask, request, render_template
import json

app = Flask(__name__)
db_file = open("conceitos_.json",encoding="utf-8")
db = json.load(db_file)

db_file.close()

@app.route("/")
def hell_world():                               ## FALTA ARRANJAR ESTA PARTE DO HOME
    return render_template("home.html")


@app.route("/conceitos")
def conceitos():
    designacoes = list(db.keys())
    return render_template("conceitos.html", designacoes=designacoes, title="Lista de Conceitos",db=db)


@app.route("/pesquisar", methods=["GET"])
def pesquisar():
    termo = request.args.get("termo", "").strip()
    resultados = []
    if termo:
        # Filtra o dicionário para encontrar ocorrências no termo ou na descrição
        for chave, valor in db.items():
            if termo == chave.lower() or termo in valor.lower().split():
                resultados.append({"termo": chave, "descricao": valor})

    return render_template("pesquisar.html", resultados=resultados, termo_pesquisado=termo)

@app.route("/api/conceitos")
def api_conceitos():
    return db



@app.post("/api/conceitos")
def adicionar_conceitos():
    #json
    data = request.get_json()
    #{"designacao":"vida", "descricao":"A vida é ..."}
    db[data["designacao"]] = data["descricao"]
    f_out = open("conceitos.json","w",encoding="utf-8")
    json.dump(db,f_out, indent=4,ensure_ascii=False)
    f_out.close()
    #form data
    return data

# @app.route("/conceitos/<designacao>")        ### ESTA É A MINHA VERSÃO DO QUE O PROFESSOR FEZ ABAIXO. TAMBÉM FUNCIONA DIREITO ###
# def api_conceito(designacao):
#     if designacao in db:        
#         return render_template("conceito_unico.html", designacao=designacao, descricao=db[designacao], title="Conceito",db=db)


@app.get("/conceitos/<designacao>")            ### ESTA É A VERSÃO DE PROFESSOR ###
def conceito(designacao):
    if designacao in db:
        return render_template("conceito_versao_prof.html", designacao=designacao, descricao=db[designacao], db=db)
    else:
        return render_template("conceito_versao_prof.html", designacao="Erro", descricao="Descrição não encontrada")



@app.post("/conceitos")
def adicionar_conceito():
    descricao = request.form.get("descricao")
    designacao = request.form.get("designacao")

    db[designacao] = descricao
    f_out = open("conceitos_.json","w",encoding="utf-8")
    json.dump(db,f_out, indent=4,ensure_ascii=False)
    f_out.close()
    
    designacoes = sorted(list(db.keys()))
    return render_template("conceitos.html",designacoes=designacoes, title = "Lista de Conceitos")




app.run(host="localhost", port=4002, debug=True)

