from flask import Flask # Importa a classe Flask do módulo flask

app = Flask(__name__) # Cria uma instância da classe Flask
app.debug = True # Ativa o modo de depuração

from app import routes # Importa o módulo routes do pacote app
