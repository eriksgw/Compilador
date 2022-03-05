'''
Módulo para definição da classe de escopo
'''

from dataclasses import dataclass
from classes.simbolo import Type
from .exception import (VariableAlreadyDeclaredError)
class Escopo:
    ''' Classe de Escopo '''

    def __init__(self, label='global', escopo_pai=None, loop=False):
        self.label = label
        self.escopo_pai = escopo_pai
        self.loop = loop
        self.table = []
        self.escopos_internos = []

    def new_entry(self, entry):
        '''Adiciona entrada na tabela de símbolos'''

        # Se variavel já foi declarada
        var = list(filter(lambda x: x.ident == entry.ident, self.table))

        if len(var) > 0:
            raise VariableAlreadyDeclaredError('Variável já declarada')

        self.table.append(entry)
    
    def add_inner_scope(self, scope):
        ''' Adiciona escopo interno '''
        self.escopos_internos.append(scope)

    def as_json(self):
        print(self.table)
        return {
            'label': self.label,
            'table': [
                entry.as_json() for entry in self.table
            ],
            'escopos_internos': [scope.as_json() for scope in self.escopos_internos]
        }

    def __str__(self):
        return '\n'.join([str(entry) for entry in self.table]) + '\n'

@dataclass
class Node:

    value: str
    left: ...
    right: ...
    result_type: str

    def as_json(self):
        left = None
        if self.left is not None:
            left = self.left.as_json()

        right = None
        if self.right is not None:
            right = self.right.as_json()

        return {
            'value': self.value,
            'left': left,
            'right': right
        }

    def __str__(self):
        if self.left is not None or self.right is not None:
            return f'({self.left}{self.value}{self.right})'

        return str(self.value)