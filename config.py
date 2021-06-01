# Objeto de conexão para encontrar o servidor, sql logon e efetivar a conexão
from app import app
from flaskext.mysql import MySQL
from flask_basicauth import BasicAuth

app.config['BASIC_AUTH_USERNAME'] = 'silsil'
app.config['BASIC_AUTH_PASSWORD'] = '1234567'

auth = BasicAuth(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'silale'
app.config['MYSQL_DATABASE_PASSWORD'] = 'silale2021' #insira a sua senha do DB
app.config['MYSQL_DATABASE_DB'] = 'db_clientes' #insira o nome do seu DB
app.config['MYSQL_DATABASE_DB'] = 'db_produtos' #insira o nome do seu DB
app.config['MYSQL_DATABASE_DB'] = 'db_vendas' #insira o nome do seu DB
app.config['MYSQL_DATABASE_HOST'] = 'db-silale.cxycaymkd24m.us-east-1.rds.amazonaws.com'


mysql.init_app(app)


