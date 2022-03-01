'''
Módulo para entradas da tabela de símbolos
'''

from dataclasses import dataclass
from enum import Enum

from typing import List

class Type(Enum):
    ''' Enum dos tipos suportados pelo compilador '''
    INT = 1
    FLOAT = 2
    STRING = 3

@dataclass
class Simbolo:
    ''' Classe dos símbolos '''

    label: str
    index: int
    type: Type
    line_dec: int
    line_ref: List[int]
    function: bool

@dataclass
class EntradaTabela:
    ''' Classe de uma entrada na Tabela de Símbolos'''

    ident: str
    type: str
    dimension: int
    sizes: list
    line: int

    def json(self):
        ''' Returns instance as json object '''
        return {
            'ident': self.ident,
            'type': self.type,
            'line': self.line,
        }