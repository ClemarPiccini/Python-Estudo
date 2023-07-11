from pymongo import MongoClient

# Conectar ao servidor MongoDB local
client = MongoClient('mongodb://localhost:27017/')

# Acessar o banco de dados
db = client['meu_banco_de_dados']

# Acessar a coleção
collection = db['minha_colecao']

# Inserir um documento
documento = {'nome': 'João', 'idade': 25}
collection.insert_one(documento)

# Consultar documentos
documentos = collection.find()
for documento in documentos:
    print(documento)

# Atualizar um documento
collection.update_one({'nome': 'João'}, {'$set': {'idade': 26}})

# Deletar um documento
collection.delete_one({'nome': 'João'})
