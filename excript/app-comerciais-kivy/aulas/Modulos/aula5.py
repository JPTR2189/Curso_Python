# LOCALIZAÇÃO DE MÓDULOS

from pprint import pprint
from sys import path as lpath

# ADICIONANDO UM NOVO CAMINHO PARA PESQUISA DE UM MÓDULO
lpath.insert(0, "C:/dev/tmp")

# IMPORTANDO MODULO COM O NOVO CAMINHO ADICIONADO NA PATH
import aula5b


# pprint(lpath)

