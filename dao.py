
import json
import os

class DAO:
    def __init__(self, arquivo, classe):
        self.__arquivo = arquivo
        self.__classe = classe
        self.__objetos = []

    def abrir(self):
        if not os.path.exists(self.__arquivo):
            self.__objetos = []
            return self.__objetos

        with open(self.__arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        self.__objetos = [
            self.__classe.from_json(json.dumps(dado))
            for dado in dados
        ]

        return self.__objetos

    def salvar(self):
        dados = []

        for objeto in self.__objetos:
            if hasattr(objeto, "to_dict"):
                dados.append(objeto.to_dict())
            else:
                dados.append(json.loads(objeto.to_json()))

        with open(self.__arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
