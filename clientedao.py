
from models.dao import DAO
from models.cliente import Cliente

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__("clientes.json", Cliente)
