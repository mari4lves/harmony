# Importanto a biblioteca do flask para fazer um site dinamico
from flask import Flask, render_template, request

app = Flask(__name__)

# Criar uma lista e usuarios e senha, depois vamos pegar no BD
usuarios ={
    'abelha' : 'zomzomzom',
    'maria' : '2121',
    'marina' : '12345',
    'helo' : '54321'
}

# Definindo a rota principal do site
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/esqueci')
def esqueci():
    return render_template('esqueci.html')

@app.route('/novaSenha')
def novaSenha():
    return render_template('novaSenha.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/configuração')
def configuração():
    return render_template('configuração.html')

#Verificar o login
@app.route ('/verificar-login', methods= ['POST'])
def verificar_login():
#Pegando o que o usuario digitou no campo de entrada de user e senha
    username = request.form['username']
    password = request.form['password']

    #Verificar se o usuario digitado esta na lista e se
    #a senha está certa
    if username in usuarios and usuarios[username] == password:
        return f"Bem-vindo, {username}!"
    else:
        return "Usuário ou senha inválidos."
    

# Parte principal do programa em Python
if __name__=='__main__':
    app.run(debug=True)