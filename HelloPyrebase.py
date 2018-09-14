import pyrebase
# baseado em https://github.com/FelipeOliveiraTI/PyrebaseSeComp
import config

config = {
    "apiKey": config.apiKey,
    "authDomain": config.authDomain,
    "databaseURL": config.databaseURL,
    "projectId": config.projectId,
    "storageBucket": config.storageBucket,
    "messagingSenderId": config.messagingSenderId
}

firebase = pyrebase.initialize_app(config)

# autenticação
auth = firebase.auth()

# criação user
# user = auth.create_user_with_email_and_password('faccio.rafael@gmail.com','123456')

# login user
user = auth.sign_in_with_email_and_password('faccio.rafael@gmail.com','123456')

# conexao com db e storage (bucket)
db = firebase.database()
storage = firebase.storage()

# upload e download de imagem
result_up = storage.child("images/example.jpg").put("jorge.jpg")
storage.child("images/example.jpg").download("jorge_down.jpg")

# adicionando dados ao db
data = {
    "Nome": "Teste Novouser",
    "Email": "teste@site.com",
    "Idade": "27"
}

# envia o dado
result_db = db.child("users").push(data, user['idToken'])

# retorna o dado
data_get = db.child("users").get(user['idToken'])

# imprime
for u in data_get.each():
    print(u.key())
    print(u.val())