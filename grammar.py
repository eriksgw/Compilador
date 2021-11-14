import main
from main import tokens
import ply.yacc as yacc


# TODO: Create Grammar

def p_program(p):
    '''
    program : statement | funclist
    '''
    p[0]=p[1]

def p_funclist(p):
    '''
    funclist : funcdef funclist | funcdef
    '''
    p[0]=p[1]

def p_funcdef(p):
    '''
    funcdef : DEF IDENT LPAREN paramlist RPAREN LBRACKET statelist RBRACKET
    '''

def p_empty(p):
    '''
    empty : 
    '''
    p[0]=None

parser=yacc.yacc(start='program')  #build the parser