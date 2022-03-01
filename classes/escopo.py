'''
Módulo para definição da classe de escopo
'''

from contador import Contador
from exception import (VariableAlreadyDeclaredError)
class Escopo:
    ''' Classe de Escopo '''

    table = []
    escopos_internos = []


    def __init__(self, label='global', escopo_pai=None, loop=False):
        self.label = label
        self.scopecontador = Contador(label)
        self.funccontador = Contador(label)
        self.varcontador = Contador(label)

        self.escopo_pai = escopo_pai
        self.loop = loop

    def new_entry(self, entry):
        '''Adiciona entrada na tabela de símbolos'''

        # Se variavel já foi declarada
        var = list(filter(lambda x: x.ident == entry.ident, self.table))

        if len(var) > 0:
            raise VariableAlreadyDeclaredError('Variável já declarada')

        self.table.append(var)
    
    def add_inner_scope(self, scope):
        ''' Adiciona escopo interno '''
        self.escopos_internos.append(scope)

    def as_json(self):
        return {
            'table': [
                entry.json() for entry in self.table
            ],
            'escopos_internos': [scope.json() for scope in self.escopos_internos]
        }

    def __str__(self):
        return '\n'.join([str(entry) for entry in self.table]) + '\n'

class Node:

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def json(self):
        left = None
        if self.left is not None:
            left = self.left.json()

        right = None
        if self.right is not None:
            right = self.right.json()

        return {
            'value': self.value,
            'left': left,
            'right': right
        }