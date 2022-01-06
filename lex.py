import ply.lex as lex

# RESERVED WORDS
reserved = {
    'def':'DEF',          # def
    'break':'BREAK',      # break
    'for':'FOR',          # for
    'while':'WHILE',      # while
    'if':'IF',            # if
    'else':'ELSE',        # else
    'int':'INT',          # int
    'float':'FLOAT',      # float
    'new':'NEW',          # new
    'print':'PRINT',      # print
    'read':'READ',        # read
    'return':'RETURN',      # return
    'string':'STRING',    # string
}

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

tokens = list(reserved.values()) + operators + special + constant + identifiers
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
    t.type = reserved.get(t.value, 'IDENT')
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

text = ""

def find_column(token):
        last_cr = text.rfind('\n',0,token.lexpos)
        if last_cr < 0:
            last_cr = 0
        column = (token.lexpos - last_cr) + 1
        if token.lineno > 1:
            column -= 1
        return column

def analyze(input_value):
    global text
    lexer = lex.lex()

    text = input_value

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
    return lexer