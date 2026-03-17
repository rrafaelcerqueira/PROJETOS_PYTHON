class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

        def get_nome(self):
            return self._nome

        def get_idade(self):
            return self._idade



# Objetos Pessoa
jose = Pessoa('José', 10)
maria = Pessoa('Maria', 11)

dir(jose)

class SuperPoderes:
    def sabe_voar(self):
        return 'sei voar'

    def saber_nadar(self):
        return 'sei nadar'

class Professor(Pessoa, SuperPoderes):
    pass

professor_xavier = Professor('Professor Xavier', 100)