
from models.dao import DAO
from models.servico import Servico

class ServicoDAO(DAO):
    def __init__(self):
        super().__init__("servicos.json", Servico)
