
from models.dao import DAO
from models.profissional import Profissional

class ProfissionalDAO(DAO):
    def __init__(self):
        super().__init__("profissionais.json", Profissional)
