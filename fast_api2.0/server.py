from fastapi import FastAPI
from schema import request_nova_peca, response_consulta_peca
from methods_app import mongodb_methods

mongodb_methods=mongodb_methods()

app = FastAPI()

#verifica integridade:
@app.get("/healthcheck")
def home():
    return {"Funcionando"}

#adiciona peca nova:
@app.put("/nova/peca/")
def nova_peca(body:request_nova_peca):

    retorno_nova_peca, status_retorno = mongodb_methods.inserir_peca_nova(body.peca, body.valor, body.data_compra)
    print(retorno_nova_peca, status_retorno)
    
    if status_retorno == 201:
        return {}

#rota para consultar por peça:
@app.post("/peca/{peca}")
def consulta_peca(peca):

    #chama consulta de peça:
    retorno_consulta_peca, status_retorno = mongodb_methods.consultar_peca(peca)
    print(status_retorno)
    print(retorno_consulta_peca)
    #trata retorno:
    

#criar um dashboard para ver todas as peças cadastradas e IDs delas

#rota para inserir id e deletar a peça
#rota para inserir id e alterar peças
