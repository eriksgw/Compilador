'''
Módulo para contador para número de variáveis
'''

from dataclasses import dataclass

@dataclass
class Contador:
    '''Contador para número de variáveis'''

    label: str
    count: int = 0

    def inc(self, increase = 1):
        '''
        Incrementa o contador
            param: int increase [opcional] : default 1
            return: int
        '''
        self.count += increase
        return self.count

    def dec(self, decrease = 1):
        '''
        Decrementa o contador
            param: int decrease [opcional] : default 1
            return: int
        '''
        self.count -= decrease
        return self.count
