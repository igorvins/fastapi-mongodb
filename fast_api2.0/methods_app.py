#metodos mongodb
import pymongo
from mongodb import mongodb
import datetime
from datetime import date as dt

date_format='%Y-%m-%d'

class mongodb_methods():

    def __init__(self):
        self.metodo=mongodb()

    def inserir_peca_nova(self, peca, valor, data_compra):

    #convertenco data da compra em epochtime:
        if data_compra == "":
            data_compra = str(dt.today())
            data_compra = datetime.datetime.strptime(data_compra, date_format)
            data_compra_epochtime=int(data_compra.timestamp())

        else:
            data_compra = datetime.datetime.strptime(data_compra, date_format)
            data_compra_epochtime=int(data_compra.timestamp())
            print("DATA EPOCHTIME:",data_compra_epochtime)

    	#criando o dicionario de pecas:
        adicionar_peca = {}
        adicionar_peca['peca'] = peca
        adicionar_peca['valor'] = valor
        adicionar_peca['data_compra'] = data_compra

        self.metodo.inserir_peca(adicionar_peca)

        return "Peça inserida com sucesso", 201
    
    def consultar_peca(self, peca):

        peca_chaves={"peca":peca}

        retorno_consulta = self.metodo.consulta_peca(peca_chaves)

        return retorno_consulta, 200

