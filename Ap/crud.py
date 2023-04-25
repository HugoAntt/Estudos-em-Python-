from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True #Configuração de banco de dados.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/banco'

db = SQLAlchemy(app)


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(60))
    email = db.Column(db.String(120))


def para_json(self): #Criação de função para conveter os usuários para o formato JSON.
    return {"id": self.id, "nome": self.nome, "email": self.email}


#Selecionar todos os usuários
@app.route("/usuarios", methods = ["GET"])
def selecionar_usuarios():
    usuarios_objeto = Usuario.query.all()
    usuarios_json = [usuario.para_json() for usuario in usuarios_objeto]

    return gerador_response(200, "usuarios", usuarios_json, "Todos os usuários selecionados.")


#Selecionar um usuário pelo ID
@app.route("/usuario/<id>", methods = ["GET"])
def selecionar_usuario(id): 
    usuario_objeto = Usuario.query.filter_by(id = id).first()
    usuario_json = [usuario_objeto.para_json() ]

    return gerador_response(200, "usuario", usuario_json, "Usuário selecionado pelo ID.")


#Cadastrar usuário
@app.route("/usuario", methods = ["POST"])
def cadastrar_usuario():
    body = request.get_json()

    #Validação de que se os parâmetros foram postos corretamente.

    try:
        usuario = Usuario(nome = body["nome"], email = body["email"]) #Criação de um objeto usuário.
        db.session.add(usuario) #Abertura de sessão para adicionar o usuário criado.
        db.session.commit() #Adição do usuário criado.
        return gerador_response(201, "usuario", usuario.para_json(), "Usuário criado com sucesso.")
    except Exception as e: #Em caso de erro, apresentar a exceção.
        print(e)
        return gerador_response(400, "usuario", {}, "Erro ao cadastrar usuário.")


#Método para atualizar algum usuário
@app.route("/usuario/<id>", methods = ["PUT"])
def atualizar_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id = id).first()
    body = request.get_json()

    try:
        if("nome" in body):
            usuario_objeto.nome = body["nome"]
        if("email" in body):
            usuario_objeto.email = body["email"]

        db.session.add(usuario_objeto)
        db.session.commit()
        return gerador_response(200, "usuario", usuario_objeto.para_json(), "Usuário atualizado com sucesso.")
    except Exception as e:
        print(e)
        return gerador_response(400, "usuario", {}, "Erro ao atualizar usuário.")


#Deletar usuário
@app.route("/usuario/<id>", methods = ["DELETE"])
def deletar_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id = id).first()

    try:
        db.session.delete(usuario_objeto)
        db.session.commit()
        return gerador_response(200, "usuario", usuario_objeto.para_json(), "Usuário deletado com sucesso.")
    except Exception as e:
        print(e)
        return gerador_response(400, "usuario", {}, "Erro ao deletar usuário.")


def gerador_response(status, nome_do_conteudo, conteudo, mensagem): #Função para gerar Responses de forma mais automatizada, com a mensagem a ser exibida sendo opcional.
    body = {}
    body[nome_do_conteudo] = conteudo
    body["mensagem"] = mensagem        

    return Response(json.dumps(body), status = status, mimetype = "application/json")