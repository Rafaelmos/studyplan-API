from flask import Flask

#Importando arquivos das Rotas alternativas:
from module.usuario.controller import app_usuario 


app = Flask(__name__)
app.register_blueprint(app_usuario)


@app.route("/")
def get_user():
  return "Hello world"

if __name__ == '__main__':
  app.run()