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

    def leaf(self):
        return self.left is None and self.right is None

    # def code(self, label_func):
    #     if self.left is None and self.right is None:
    #         return
    #     else:
    #         code = ""
    #         left_label = None
    #         right_label = None
    #         aux_code_left = []
    #         aux_code_right = []
    #         if self.left.leaf():
    #             code += self.left.value
    #         else:
    #             left_label, aux_code_left = self.left.code(label_func)
    #             code += left_label
            
    #         code += self.value

    #         if self.right.leaf():
    #             code += self.right.value
    #         else:
    #             right_label, aux_code_right = self.right.code(label_func)
    #             code += right_label

    #         this_label = label_func()

    #         return (this_label, [*aux_code_left, aux_code_right, f'{this_label} = code'])

    def __str__(self):
        if self.left is not None or self.right is not None:
            return f'({self.left}{self.value}{self.right})'

        return str(self.value)