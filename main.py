'''
Authors:
    Bruno Duarte Barreto Borges
    Erik Kazuo Sugawara
    Fábio Oliveira de Abreu
'''

if __name__ == '__main__':
    import sys
    from lex import analyze as la

    if len(sys.argv) != 2:
        file = open('./tmp/lil_example.lcc', 'r')        
    else:
        file = open(sys.argv[1], 'r')

    input_value = file.read()

    lexer = la(input_value)

    from syntax import analyze as sa

    sa(input_value)
