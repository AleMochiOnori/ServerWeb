from flask import Flask, render_template, request

utenti = [
    ['mario', 'rossi', "1", 'ciao','0'],
    ['gianni', 'derossi', "1", 'fuoco','0'],
    ['Anita', 'Garibaldi', "2", 'acqua','0']
]

api = Flask(__name__)

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/login', methods=['GET'])
def login():
    return render_template("login.html")




@api.route('/registrati', methods=['GET'])
def registrati():
    utente = []
    nome = request.args.get("name")
    cognome = request.args.get("surname")
    sesso = request.args.get("sesso")
    password = request.args.get("password")

    utente.append(nome)
    utente.append(cognome)
    utente.append(sesso) 
    utente.append(password)
    utente.append("0")
    print(utente)
    if utente in utenti:
        index = utenti.index(utente)
        utenti[index][4] = "1"
        return render_template("reg_ok.html")
    else :
        return render_template("reg_ko.html")

api.run(host="0.0.0.0", port=8085)





@api.route('/accedi', methods=['GET'])
def accedi():
    nome = request.args.get("name")
    password = request.args.get("password")
    sesso = request.args.get("sesso")
    utente = []
    utente.append(nome)
    utente.append(password)
    utente.append(sesso)
    print(utente)
    for u in utenti:
        if u[0] == nome and u[2] == sesso and u[3] == password and u[4] == "1":
            return render_template("successo.html")
    
    return render_template("negato.html")

    





