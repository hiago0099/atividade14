
from models.dao import DAO
from models.horario import Horario

class HorarioDAO(DAO):
    def __init__(self):
        super().__init__("horarios.json", Horario)
