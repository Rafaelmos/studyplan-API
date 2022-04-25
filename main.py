from flask import Flask

#Importando arquivos das Rotas alternativas:
from module.usuario.controller import app_usuario 
from module.lembretes.controller import app_lembretes
from module.metas.controller import app_metas
from module.materias.controller import app_materias
from module.agenda.controller import app_agenda



app = Flask(__name__)
app.register_blueprint(app_usuario)
app.register_blueprint(app_lembretes)
app.register_blueprint(app_metas)
app.register_blueprint(app_materias)
app.register_blueprint(app_agenda)



if __name__ == '__main__':
  app.run(debug=True)