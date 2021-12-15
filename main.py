'''
Authors:
    Bruno Duarte Barreto Borges
    Erik Kazuo Sugawara
    Fábio Oliveira de Abreu
'''

import ply.lex as lex
import ply.yacc as yacc

# RESERVED WORDS
reserved = [
    'DEF',          # def
    'BREAK',       # break
    'FOR',         # for
    'WHILE',
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
    'MULTIPLY',    # *
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
]

# CONSTANTS
constant = [
    'int_constant',
    'string_constant',
    'float_constant',
    'null_constant'
]

# IDENTIFIERS
identifiers = [
    'IDENT',
]

tokens = reserved + operators + special + constant + identifiers

'''
 Observations
    - "t_" means how ply token's looks like.
    - For complex tokens, we can define a func starting with t_
    - Returns LexToken(Token, symbol, line, column)
'''

 # For simple tokens, we can use the form below.

t_ignore = r' ' # Ignore spaces between char.

def t_DEF(t):
    r'def'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_FOR(t):
    r'for'
    return t

def t_WHILE(t):
    r'while'
    return t
    
def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_NEW(t):
    r'new'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_READ(t):
    r'read'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_STRING(t):
    r'string'
    return t

def t_INT(t):
    r'int'
    return t

def t_FLOAT(t):
    r'float'
    return t

t_ASSIGN = r'\='
t_GT = r'\>'
t_LT = r'\<'
t_EQ = r'\=='
t_LE = r'\<='
t_GE = r'\>='
t_NEQ = r'\!='
t_PLUS = r'\+'
t_MINUS = r'\-'
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

def t_null_constant(t):
    r'null'
    return t
# For complex tokens, we can use the form below.
def t_float_constant(t):
    r'[+-]?\d+\.\d+([eE][+-]?\d+)?'
 
    return t

def t_int_constant(t):
    r'[+-]?\d+'

    return t

def t_string_constant(t):
    r'"[^"\n\r]*"'
    return t

def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # t.type = 'IDENT'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

errors = []


def t_error(t):
    # print(pattern.format("*ILLEGAL CHAR*", t.value[0], t.lexer.lineno, t.lexpos))

    errors.append("Illegal char %s in line %d, column %d" % (t.value[0], t.lexer.lineno, find_column(t)))

    t.lexer.skip(1)

def print_table(st):
    max_length = max(map(len, st.keys())) + 4
    pattern = "{:^" + str(max_length) + "} | {:<100}"
    print("\033[4m" + pattern.format("IDENT", "(LINE,COLUMN)") + "\033[0m")
    for k, v in st.items():
        if (len(v) > 10):
            print(pattern.format(k, str(v[:10])))
            for i in range(10, len(v), 10):
                items = v[i:i+10]
                print(pattern.format('', str(items)))
        else:
            print(pattern.format(k, str(v))) 

    for e in errors:
        print(e)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        file = open('./tmp/program_1.lcc', 'r')        
    else:
        file = open(sys.argv[1], 'r')

    lexer = lex.lex()
    input_value = file.read()

    def find_column(token):
        last_cr = input_value.rfind('\n',0,token.lexpos)
        if last_cr < 0:
            last_cr = 0
        column = (token.lexpos - last_cr) + 1
        if token.lineno > 1:
            column -= 1
        return column

    lexer.input(input_value)

    symbol_table = {}
    while True:
        tok = lexer.token()
        if not tok:
            break

        if tok.type == 'IDENT':
            if tok.value in symbol_table:
                symbol_table[tok.value].append((tok.lineno, find_column(tok)))
            else:
                symbol_table[tok.value] = [(tok.lineno, find_column(tok))]

    print_table(symbol_table)
