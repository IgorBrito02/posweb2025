from pymongo import MongoClient

from config import MONGO_URL, MONGO_DB, MONGO_COLLECTION

from models import Cliente, Produto, Venda
from sqlalchemy import func
from models import db

try:
    client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=2000)
    client.server_info()
    mongo_db = client[MONGO_DB]
    dashboard_collection = mongo_db[MONGO_COLLECTION]
    mongo_connected = True
    print("[MongoDB] Conectado com sucesso!")
except Exception as e:
    print(f"[MongoDB] Aviso: não foi possível conectar: {e}")
    mongo_db = None
    dashboard_collection = None
    mongo_connected = False

def registrar_documento(collection_name, filtro, valores):
    if mongo_connected:
        collection = mongo_db[collection_name]
        collection.update_one(filtro,
                              {"$set": valores}, upsert=True)

    else:
        print("[MongoDB] Registro ignorado (sem conexão)")

def obter_documento(collection_name, filtro):
    if mongo_connected:
        collection = mongo_db[collection_name]
        return collection.find_one(filtro)
    return None

def registrar_dashboard_total(total_clientes):
    if mongo_connected:
        dashboard_collection.update_one(
            {"_id": "total_clientes"},
            {"$set": {"total": total_clientes}},
            upsert=True
        )
    else:
        print("[MongoDB] Registro ignorado (sem conexão)")

def obter_dashboard_total():
    if mongo_connected:
        doc = dashboard_collection.find_one({"_id": "total_clientes"})
        return doc["total"] if doc else 0
    return 0

# ========== Dashboard Geral ==========

def registrar_dashboard_info():
    if not mongo_connected:
        print("[MongoDB] Ignorado: sem conexão")
        return

    # Total de clientes
    total_clientes = db.session.query(func.count(Cliente.id_cliente)).scalar()

    # Total de produtos
    total_produtos = db.session.query(func.count(Produto.id_produto)).scalar()

    # Total de vendas
    total_vendas = db.session.query(func.count(Venda.id_pedido)).scalar()

    # Produto mais vendido
    produto_mais_vendido = (
        db.session.query(
            Produto.nome,
            func.count(Venda.id_produto).label("total_vendas")
        )
        .join(Venda, Produto.id_produto == Venda.id_produto)
        .group_by(Produto.id_produto)
        .order_by(func.count(Venda.id_produto).desc())
        .first()
    )

    if produto_mais_vendido:
        nome_produto_mais_vendido = produto_mais_vendido[0]
        quantidade_vendida = produto_mais_vendido[1]
    else:
        nome_produto_mais_vendido = None
        quantidade_vendida = 0

    # Documento consolidado
    dashboard_data = {
        "_id": "dashboard_geral",
        "total_clientes": total_clientes,
        "total_produtos": total_produtos,
        "total_vendas": total_vendas,
        "produto_mais_vendido": {
            "nome": nome_produto_mais_vendido,
            "quantidade": quantidade_vendida
        }
    }

    dashboard_collection.update_one(
        {"_id": "dashboard_geral"},
        {"$set": dashboard_data},
        upsert=True
    )