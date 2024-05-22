#serializador (creio que um conversor de dados para algum formato espeficio)


def convertProduto(produto) -> dict:
    return{
        "ID": str(produto["_id"]),
        "NOME": produto["NOME"],
        "SUBPRODUTO": produto["SUBPRODUTO"],
        "TIPO": produto["TIPO"]
    }

def convertProdutos(produtos) -> list:
    return [convertProduto(produto) for produto in produtos]