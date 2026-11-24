
from models.dao import DAO
from models.atendimento import Atendimento

class AtendimentoDAO(DAO):
    def __init__(self):
        super().__init__("atendimentos.json", Atendimento)
