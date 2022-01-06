from lex import tokens
import ply.yacc as yacc


def p_program_1(p):
    '''
    program : statement
    '''

def p_program_2(p):
    '''
    program : funclist
    '''

def p_program_3(p):
    '''
    program : 
    '''
    p[0]=None

def p_funclist(p):
    '''
    funclist : funcdef funclist1
    '''

def p_funclist1_1(p):
    '''
    funclist1 : DEF IDENT LPAREN paramlist RPAREN LBRACE statelist RBRACE funclist1
    '''

def p_funclist1_2(p):
    '''
    funclist1 : 
    '''
    p[0]=None

def p_funcdef(p):
    '''
    funcdef : DEF IDENT LPAREN paramlist RPAREN LBRACE statelist RBRACE
    '''

def p_types_1(p):
    '''
    types : INT
    '''

def p_types_2(p):
    '''
    types : FLOAT
    '''

def p_types_3(p):
    '''
    types : STRING
    '''

def p_paramlist_1(p):
    '''
    paramlist : STRING listdcl IDENT paramlist1 
    '''

def p_paramlist_2(p):
    '''
    paramlist : FLOAT listdcl IDENT paramlist1 
    '''

def p_paramlist_3(p):
    '''
    paramlist : INT listdcl IDENT paramlist1 
    '''

def p_paramlist_4(p):
    '''
    paramlist : 
    '''
    p[0]=None

def p_paramlist1_1(p):
    '''
    paramlist1 : COMMA paramlist
    '''

def p_paramlist1_2(p):
    '''
    paramlist1 : 
    '''
    p[0]=None

def p_listdcl_1(p):
    '''
    listdcl : LBRACKET RBRACKET listdcl
    '''

def p_listdcl_2(p):
    '''
    listdcl : 
    '''
    p[0]=None

# def p_statement_1(p):
#     '''
#     statement : vardecl SEMICOLON
#     '''

def p_statement_1_1(p):
    '''
    statement : INT IDENT statement2
    '''

def p_statement_1_2(p):
    '''
    statement : FLOAT IDENT statement2
    '''

def p_statement_1_3(p):
    '''
    statement : STRING IDENT statement2
    '''

def p_statement_2(p):
    '''
    statement : IDENT statement1
    '''

def p_statement_3(p):
    '''
    statement : printstat SEMICOLON
    '''
 
def p_statement_4(p):
    '''
    statement : readstat SEMICOLON
    '''

def p_statement_5(p):
    '''
    statement : returnstat SEMICOLON
    '''

def p_statement_6(p):
    '''
    statement : ifstat
    '''

def p_statement_7(p):
    '''
    statement : forstat
    '''

def p_statement_8(p):
    '''
    statement : whilestat
    '''

def p_statement_9(p):
    '''
    statement : LBRACE statelist RBRACE
    '''

def p_statement_10(p):
    '''
    statement : BREAK SEMICOLON
    '''

def p_statement_11(p):
    '''
    statement : SEMICOLON
    '''

def p_statement1_1(p):
    '''
    statement1 : LBRACKET numexpression RBRACKET lvalue1 ASSIGN atribstat1 SEMICOLON
    '''

def p_statement1_2(p):
    '''
    statement1 : ASSIGN atribstat1 SEMICOLON
    '''

def p_statement1_3(p):
    '''
    statement1 : LPAREN paramlistcall RPAREN SEMICOLON
    '''

def p_statement2_1(p):
    '''
    statement2 : LBRACKET numexpression RBRACKET lvalue1 SEMICOLON
    '''

def p_statement2_2(p):
    '''
    statement2 : SEMICOLON
    '''

def p_atribstat1_1(p):
    '''
    atribstat1 : expression
    '''

def p_atribstat1_2(p):
    '''
    atribstat1 : allocexpression
    '''

def p_atribstat1_3(p):
    '''
    atribstat1 : funccall
    '''

def p_funccall(p):
    '''
    funccall : IDENT LPAREN paramlistcall RPAREN
    '''

def p_paramlistcall_1(p):
    '''
    paramlistcall : factor paramlistcall2
    '''

def p_paramlistcall_2(p):
    '''
    paramlistcall : 
    '''
    p[0]=None

def p_paramlistcall1_1(p):
    '''
    paramlistcall1 : COMMA paramlistcall
    '''

def p_paramlistcall1_2(p):
    '''
    paramlistcall1 : 
    '''
    p[0]=None

def p_paramlistcall2_1(p):
    '''
    paramlistcall2 : LBRACKET numexpression RBRACKET lvalue1 paramlistcall1
    '''

def p_paramlistcall2_2(p):
    '''
    paramlistcall2 : paramlistcall1
    '''


def p_printstat(p):
    '''
    printstat : PRINT expression
    '''

def p_readstat(p):
    '''
    readstat : READ expression
    '''

def p_returnstat(p):
    '''
    returnstat : RETURN returnstat1
    '''

def p_returnstat1_2(p):
    '''
    returnstat1 : expression
    '''

def p_returnstat1_3(p):
    '''
    returnstat1 : 
    '''
    p[0]=None

def p_ifstat(p):
    '''
    ifstat : IF LPAREN expression RPAREN statement ifstat1
    '''

def p_ifstat1_1(p):
    '''
    ifstat1 : ELSE statement
    '''

def p_ifstat1_2(p):
    '''
    ifstat1 : %prec IF
    '''
    p[0]=None

def p_forstat(p):
    '''
    forstat : FOR LPAREN forstat1 SEMICOLON forstat2 SEMICOLON forstat1 RPAREN statement
    '''

def p_forstat1_1(p):
    '''
    forstat1 : IDENT forstat3
    '''

def p_forstat1_2(p):
    '''
    forstat1 : 
    '''
    p[0]=None

def p_forstat2_1(p):
    '''
    forstat2 : expression
    '''

def p_forstat2_2(p):
    '''
    forstat2 : 
    '''
    p[0]=None

def p_forstat3_1(p):
    '''
    forstat3 : LBRACKET numexpression RBRACKET lvalue1 ASSIGN atribstat1
    '''

def p_forstat3_2(p):
    '''
    forstat3 : ASSIGN atribstat1
    '''

def p_whilestat(p):
    '''
    whilestat : WHILE LPAREN expression RPAREN statement
    '''

def p_statelist_1(p):
    '''
    statelist : INT listdcl IDENT statelist2
    '''

def p_statelist_2(p):
    '''
    statelist : FLOAT listdcl IDENT statelist2
    '''

def p_statelist_3(p):
    '''
    statelist : STRING listdcl IDENT statelist2
    '''

def p_statelist_4(p):
    '''
    statelist : IDENT statelist3
    '''

def p_statelist_5(p):
    '''
    statelist : PRINT expression SEMICOLON statelist1
    '''

def p_statelist_6(p):
    '''
    statelist : READ IDENT statelist2
    '''

def p_statelist_7(p):
    '''
    statelist : RETURN returnstat1 SEMICOLON statelist1
    '''

def p_statelist_8(p):
    '''
    statelist : IF LPAREN expression RPAREN statement ifstat1 statelist1
    '''

def p_statelist_9(p):
    '''
    statelist : FOR LPAREN forstat1 SEMICOLON forstat2 SEMICOLON forstat1 RPAREN statement statelist1
    '''

def p_statelist_10(p):
    '''
    statelist : WHILE LPAREN expression RPAREN statement statelist1
    '''

def p_statelist_11(p):
    '''
    statelist : LBRACE statelist RBRACE statelist1
    '''

def p_statelist_12(p):
    '''
    statelist : BREAK SEMICOLON statelist1
    '''

def p_statelist_13(p):
    '''
    statelist : SEMICOLON statelist1
    '''

def p_statelist_14(p):
    '''
    statelist : IDENT LPAREN paramlistcall RPAREN SEMICOLON statelist1
    '''

def p_statelist1_1(p):
    '''
    statelist1 : INT listdcl IDENT statelist2
    '''

def p_statelist1_2(p):
    '''
    statelist1 : FLOAT listdcl IDENT statelist2
    '''

def p_statelist1_3(p):
    '''
    statelist1 : STRING listdcl IDENT statelist2
    '''

def p_statelist1_4(p):
    '''
    statelist1 : IDENT statelist3
    '''

def p_statelist1_5(p):
    '''
    statelist1 : PRINT expression SEMICOLON statelist1
    '''

def p_statelist1_6(p):
    '''
    statelist1 : READ IDENT statelist2
    '''

def p_statelist1_7(p):
    '''
    statelist1 : RETURN returnstat1 SEMICOLON statelist1
    '''

def p_statelist1_8(p):
    '''
    statelist1 : IF LPAREN expression RPAREN statement ifstat1 statelist1
    '''

def p_statelist1_9(p):
    '''
    statelist1 : FOR LPAREN forstat1 SEMICOLON forstat2 SEMICOLON forstat1 RPAREN statement statelist1
    '''

def p_statelist1_10(p):
    '''
    statelist1 : WHILE LPAREN expression RPAREN statement statelist1
    '''

def p_statelist1_11(p):
    '''
    statelist1 : LBRACE statelist RBRACE statelist1
    '''

def p_statelist1_12(p):
    '''
    statelist1 : BREAK SEMICOLON statelist1
    '''

def p_statelist1_13(p):
    '''
    statelist1 : SEMICOLON statelist1
    '''

def p_statelist1_14(p):
    '''
    statelist1 : IDENT LPAREN paramlistcall RPAREN SEMICOLON statelist1
    '''

def p_statelist1_15(p):
    '''
    statelist1 : 
    '''
    p[0]=None

def p_statelist2_1(p):
    '''
    statelist2 : LBRACKET numexpression RBRACKET lvalue1 SEMICOLON statelist1
    '''

def p_statelist2_2(p):
    '''
    statelist2 : SEMICOLON statelist1
    '''

def p_statelist3_1(p):
    '''
    statelist3 : LBRACKET numexpression RBRACKET lvalue1 ASSIGN atribstat1 SEMICOLON statelist1
    '''

def p_statelist3_2(p):
    '''
    statelist3 : ASSIGN atribstat1 SEMICOLON statelist1
    '''

def p_allocexpression(p):
    '''
    allocexpression : NEW types LBRACKET numexpression RBRACKET lvalue1
    '''

def p_expression(p):
    '''
    expression : numexpression expression1
    '''

def p_expression1_1(p):
    '''
    expression1 : compoperator numexpression
    '''

def p_expression1_2(p):
    '''
    expression1 : 
    '''
    p[0]=None

def p_compoperator_1(p):
    '''
    compoperator : GT
    '''

def p_compoperator_2(p):
    '''
    compoperator : LT
    '''

def p_compoperator_3(p):
    '''
    compoperator : GE
    '''

def p_compoperator_4(p):
    '''
    compoperator : LE
    '''

def p_compoperator_5(p):
    '''
    compoperator : EQ
    '''

def p_compoperator_6(p):
    '''
    compoperator : NEQ
    '''

def p_numexpression(p):
    '''
    numexpression : term numexpression1
    '''

def p_numexpression1_1(p):
    '''
    numexpression1 : addsub term
    '''

def p_numexpression1_2(p):
    '''
    numexpression1 : 
    '''
    p[0]=None

def p_addsub_1(p):
    '''
    addsub : PLUS
    '''

def p_addsub_2(p):
    '''
    addsub : MINUS
    '''

def p_term(p):
    '''
    term : unaryexpr term1
    '''

def p_term1_1(p):
    '''
    term1 : multdiv unaryexpr term1
    '''

def p_term1_2(p):
    '''
    term1 : 
    '''
    p[0]=None

def p_multdiv_1(p):
    '''
    multdiv : MULTIPLY
    '''

def p_multdiv_2(p):
    '''
    multdiv : DIVIDE
    '''

def p_multdiv_3(p):
    '''
    multdiv : REM
    '''

def p_unaryexpr_1(p):
    '''
    unaryexpr : addsub factor
    '''

def p_unaryexpr_2(p):
    '''
    unaryexpr : factor
    '''

def p_factor_1(p):
    '''
    factor : int_constant
    '''

def p_factor_2(p):
    '''
    factor : float_constant
    '''

def p_factor_3(p):
    '''
    factor : string_constant
    '''

def p_factor_4(p):
    '''
    factor : null_constant
    '''

def p_factor_5(p):
    '''
    factor : IDENT lvalue1
    '''

def p_factor_6(p):
    '''
    factor : LPAREN numexpression RPAREN
    '''


def p_lvalue1_1(p):
    '''
    lvalue1 : LBRACKET numexpression RBRACKET lvalue1
    '''

def p_lvalue1_2(p):
    '''
    lvalue1 : 
    '''

text = ""

def p_error(p):
    if not p:
        print("End of File!")
        return

    print("Erro:", p)
    print(text[p.lexpos - 40:p.lexpos + 40])

import logging
logging.basicConfig(
    level = logging.DEBUG,
    filename = "./debug/parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()

precedence = (
    ('nonassoc', 'IF'), 
    ('left', 'ELSE'),
    ('left', 'LBRACKET')
)
parser = yacc.yacc(start='program', outputdir='./debug')  #build the parser

def analyze(input_value):
    global text
    text = input_value
    result = parser.parse(input=input_value, debug=log)
    print(result)