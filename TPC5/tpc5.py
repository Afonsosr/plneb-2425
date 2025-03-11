from flask import Flask, request, render_template
import json

app = Flask(__name__)
db_file = open("conceitos_.json",encoding="utf-8")
db = json.load(db_file)

db_file.close()

@app.route("/")
def hell_world():
    return "<p>Hello, World!</p>"


@app.route("/conceitos")
def conceitos():
    designacoes = list(db.keys())
    return render_template("conceitos.html", designacoes=designacoes, title="Lista de Conceitos")



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

@app.route("/conceitos/<designacao>")
def api_conceito(designacao):
    if designacao in db:
        return render_template("conceitos.html", designacao=designacao, descricao=db[designacao], title="Conceito")


app.run(host="localhost", port=4002, debug=True)

