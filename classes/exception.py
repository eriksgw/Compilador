'''
Exceptions
'''

class VariableAlreadyDeclaredError(Exception):
    ''' A variável já foi declarada '''

class VariableNotDeclaredError(Exception):
    ''' A variável não foi declarada '''

class ScopeNotExistError(Exception):
    ''' O escopo não existe '''

class InvalidTypeOperationError(Exception):
    ''' Tipo de operação inválida '''

class BreakOutLoopError(Exception):
    ''' Break fora de um loop '''

class TypeError(Exception):
    ''' Operação com variável de tipo inválido '''

class IdentifierNotFunction(Exception):
    ''' A variável é um indentificador, não uma função '''

class ParamCountError(Exception):
    ''' Número inválido de parâmetros '''