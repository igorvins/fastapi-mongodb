from pydantic import BaseModel
from typing import List


class request_nova_peca(BaseModel):
    peca: str
    valor: int
    data_compra: str

class peca(BaseModel):
    peca: str
    valor: int
    data_compra: str
    #tempo_desde_compra: int

class response_consulta_peca(BaseModel):
    pecas: List[peca]

'''
class request_consulta_peca (BaseModel):
    data_inicio: 
    data_final:
'''