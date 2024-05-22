#modelo da nossa requisiçao

from pydantic import BaseModel

class Produto(BaseModel):
    _id: str
    NOME: str
    SUBPRODUTO: str
    TIPO: str

    