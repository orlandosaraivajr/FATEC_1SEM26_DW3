'''
Principais conceitos de OO:
 - Classe
 - Objeto
 - Método
 - Atributo
'''

class Pessoa: 
    def __init__(self, nome_local, idade):
        # Um underline (_) = "Sabor" privado
        self._nome = nome_local
        # Dois underlines (__) = "Privado"
        self.__idade = idade
    
    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self.__idade
    
    def __str__(self):
        return self._nome
    
    def __repr__(self):
        return self._nome + " " + str(self.__idade)

# Objetos Pessoa
jose = Pessoa('José', 10)
maria = Pessoa('Maria', 11)

# Descobrir tudo que o objeto tem
dir(jose)


class SuperPoderes:
    def sabe_voar(self):
        return 'sei voar'
    
    def sabe_nadar(self):
        return 'sei nadar'

class Professor(Pessoa, SuperPoderes):
    pass

professor_xavier = Professor('Professor Xavier', 100)
