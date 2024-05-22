from pymongo import MongoClient


class mongodb():

    def __init__(self):
        self.connection_string="mongodb+srv://admin:12344@igor--dev-2024.3bvgbxa.mongodb.net/?retryWrites=true&w=majority"
        self.client=MongoClient(self.connection_string)

    def inserir_peca(self, peca):
        #pecas é o nome do db
        db = self.client.pecas
        #pecas_civic é o nome da collection:
        pecas_civic_collection=db['pecas_civic']
        retorno_inserir = pecas_civic_collection.insert_one(peca)

        return retorno_inserir
    
    def consulta_peca(self,peca_consulta):

        db=self.client.pecas
        pecas_civic_collection=db['pecas_civic']
        retorno_consulta=pecas_civic_collection.find(filter=peca_consulta)

        return retorno_consulta

    
