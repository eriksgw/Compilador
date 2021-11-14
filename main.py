import ply.lex as lex
import ply.yacc as yacc

''' TOKENS '''
# TODO: Verificar se skip esta correto.
# TODO: Verificar se faltam tokens.
# TODO: Verificar se tokens estao corretos.
# TODO: Verificar a gramatica disponibilizada no AL.pdf
# TODO: Criar as expressoes regulares de cada token.

skip = [
    'COMMENT_SINGLE',  # Single Line Comment
    'COMMENT_MULT'     # Mult Line Comment
]

# RESERVED WORDS
reserved = [
    'BREAK',       # break
    'CLASS',       # class
    'SUPER'        # super
    'CONSTRUCTOR', # constructor
    'EXTENDS',     # extends
    'FOR',         # for
    'WHILE',       # while
    'IF',          # if
    'ELSE',        # else
    'INT',         # int
    'FLOAT',       # float
    'NEW',         # new
    'PRINT',       # print
    'READ',        # read
    'RETURN',      # return
    'STRING',      # string
]

# OPERATORS
operators = [
    'ASSIGN',      # =
    'GT',          # >
    'LT',          # <
    'EQ',          # ==
    'LE',          # <=
    'GE',          # >=
    'NEQ',         # !=
    'PLUS',        # +
    'MINUS',       # -
    'MULTIPLY',     # *
    'DIVIDE',      # / 
    'REM'          # %
]

# SPECIAL SYMBOLS
special = [
    'LPAREN',      # (
    'RPAREN',      # )
    'LBRACE',      # {
    'RBRACE',      # }
    'LBRACKET',    # [
    'RBRACKET',    # ]
    'SEMICOLON',   # ;
    'COMMA',       # ,
    'DOT'          # .
]

# CONSTANTS
constant = [
    'int_constant',
    'string_constant',
    'null_constant'
]

# IDENTIFIERS
identifiers = [
    'IDENT',
    'LETTER',
    'DIGIT'
]

tokens = skip + reserved + operators + special + constant + identifiers

'''
 Observations
    - "t_" means how ply token's looks like.
    - For complex tokens, we can define a func starting with t_
    - Returns LexToken(Token, symbol, line, column)
'''

 # For simple tokens, we can use the form below.

t_ignore = r' ' # Ignore spaces between char.
t_ASSIGN = r'\='
t_GT = r'\>'
t_LT = r'\<'
t_EQ = r'\=='
t_LE = r'\<='
t_GE = r'\>='
t_NEQ = r'\!='
t_PLUS = r'\+'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_REM = r'\%'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_DOT = r'\.'

# For complex tokens, we can use the form below.
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
   # Ex: 1337
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'IDENT'
    return t

def t_error(t):
    print("Illegal characters")
    t.lexer.skip()

if __name__ == '__main__':
    lexer = lex.lex()
    lexer.input("teste123 = 1 + 2.23")
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok) 