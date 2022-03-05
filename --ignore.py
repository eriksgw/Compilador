# def p_statelist_1(p):
#     '''
#     statelist : INT listdcl IDENT statelist2
#     '''

# def p_statelist_2(p):
#     '''
#     statelist : FLOAT listdcl IDENT statelist2
#     '''

# def p_statelist_3(p):
#     '''
#     statelist : STRING listdcl IDENT statelist2
#     '''

# def p_statelist_4(p):
#     '''
#     statelist : IDENT statelist3
#     '''

# def p_statelist_5(p):
#     '''
#     statelist : PRINT expression SEMICOLON statelist1
#     '''

# def p_statelist_6(p):
#     '''
#     statelist : READ IDENT statelist2
#     '''

# def p_statelist_7(p):
#     '''
#     statelist : RETURN returnstat1 SEMICOLON statelist1
#     '''

# def p_statelist_8(p):
#     '''
#     statelist : IF LPAREN expression RPAREN statement ifstat1 statelist1
#     '''

# def p_statelist_9(p):
#     '''
#     statelist : FOR LPAREN forstat1 SEMICOLON forstat2 SEMICOLON forstat1 RPAREN statement statelist1
#     '''

# def p_statelist_10(p):
#     '''
#     statelist : WHILE LPAREN expression RPAREN statement statelist1
#     '''

# def p_statelist_11(p):
#     '''
#     statelist : LBRACE statelist RBRACE statelist1
#     '''

# def p_statelist_12(p):
#     '''
#     statelist : BREAK SEMICOLON statelist1
#     '''

# def p_statelist_13(p):
#     '''
#     statelist : SEMICOLON statelist1
#     '''

# def p_statelist_14(p):
#     '''
#     statelist : IDENT LPAREN paramlistcall RPAREN SEMICOLON statelist1
#     '''

# def p_statelist1_1(p):
#     '''
#     statelist1 : INT listdcl IDENT statelist2
#     '''

# def p_statelist1_2(p):
#     '''
#     statelist1 : FLOAT listdcl IDENT statelist2
#     '''

# def p_statelist1_3(p):
#     '''
#     statelist1 : STRING listdcl IDENT statelist2
#     '''

# def p_statelist1_4(p):
#     '''
#     statelist1 : IDENT statelist3
#     '''

# def p_statelist1_5(p):
#     '''
#     statelist1 : PRINT expression SEMICOLON statelist1
#     '''

# def p_statelist1_6(p):
#     '''
#     statelist1 : READ IDENT statelist2
#     '''

# def p_statelist1_7(p):
#     '''
#     statelist1 : RETURN returnstat1 SEMICOLON statelist1
#     '''

# def p_statelist1_8(p):
#     '''
#     statelist1 : IF LPAREN expression RPAREN statement ifstat1 statelist1
#     '''

# def p_statelist1_9(p):
#     '''
#     statelist1 : FOR LPAREN forstat1 SEMICOLON forstat2 SEMICOLON forstat1 RPAREN statement statelist1
#     '''

# def p_statelist1_10(p):
#     '''
#     statelist1 : WHILE LPAREN expression RPAREN statement statelist1
#     '''

# def p_statelist1_11(p):
#     '''
#     statelist1 : LBRACE statelist RBRACE statelist1
#     '''

# def p_statelist1_12(p):
#     '''
#     statelist1 : BREAK SEMICOLON statelist1
#     '''

# def p_statelist1_13(p):
#     '''
#     statelist1 : SEMICOLON statelist1
#     '''

# def p_statelist1_14(p):
#     '''
#     statelist1 : IDENT LPAREN paramlistcall RPAREN SEMICOLON statelist1
#     '''

# def p_statelist1_15(p):
#     '''
#     statelist1 : 
#     '''

# def p_statelist2_1(p):
#     '''
#     statelist2 : LBRACKET numexpression RBRACKET lvalue1 SEMICOLON statelist1
#     '''
#     p[0].dim = p[2].dim + 1
#     p[0].sizes = [str(p[1]), *p[2].sizes]

# def p_statelist2_2(p):
#     '''
#     statelist2 : SEMICOLON statelist1
#     '''
#     p[0].dim = 0
#     p[0].sizes = []

# def p_statelist3_1(p):
#     '''
#     statelist3 : LBRACKET numexpression RBRACKET lvalue1 ASSIGN atribstat1 SEMICOLON statelist1
#     '''
#     p[0]['type'] = 'attribution'

# def p_statelist3_2(p):
#     '''
#     statelist3 : ASSIGN atribstat1 SEMICOLON statelist1
#     '''
#     p[0]['type'] = 'attribution'