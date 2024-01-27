# RECARREGAMENTO DE MÓDULO

import importlib
import aula10b

del(aula10b.b)
aula10b.a = 0

# Reimportação do módulo
importlib.reload(aula10b)

from pprint import pprint

pprint(aula10b.__dict__)