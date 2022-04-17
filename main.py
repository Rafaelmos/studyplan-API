from flask import Flask

#Importando arquivos das Rotas alternativas:
from module.usuario.controller import app_usuario 
from module.lembretes.controller import app_lembretes

app = Flask(__name__)
app.register_blueprint(app_usuario)
app.register_blueprint(app_lembretes)

if __name__ == '__main__':
  app.run(debug=True)