#rotas da nossa API

from fastapi import APIRouter
from model.model import Produto
from serializer.serializer import convertProduto, convertProdutos
from config.config import produtosCollection
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from bson import ObjectId

endPoints = APIRouter()

@endPoints.get("/")
def home():
    return {"status":"OK","message":"API RUNING"}


@endPoints.put('/novoproduto')
def novoProduto(produto:Produto):
    produtosCollection.insert_one(dict(produto))
    return {
        "STATUS":"OK",
        "MESSAGE":"DATA INSERTED"
        }

@endPoints.get("/all/products")
def allProducts():
    produtos = produtosCollection.find()
    return produtos
    #convertedProdutos = convertProdutos(produtos)
    #return{
      #"status":"ok",
      #"data": convertedProdutos
    #}

@endPoints.get("/produto/${id}")
def singleProdutc(id: str):
    produto=produtosCollection.find_one({"_id":ObjectId(id)})
    convertedProduto = convertProduto(produto)
    return{
        "Status":"OK",
        "data": convertedProduto
    }
