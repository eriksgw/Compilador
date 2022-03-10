from classes.simbolo import Type
from classes.escopo import Escopo, Node
from classes.simbolo import EntradaTabela
from lex import tokens
from classes.exception import *
import ply.yacc as yacc

scope_stack = []
num_expressions = []

LC = 0

VARS = []

NEXT_LOOP_LABEL = ""

def format_code(code):
    if '$label:' in code:
        label = code[7:]
        return "{:<20} | \n".format(label)

    return "{:<20} | {}\n".format("", code)

def generate_label(loop=False):
    global LC
    LC += 1
    return f'L{loop if loop else ""}{LC}'

def get_var():
    var = f't{len(VARS) + 1}'
    VARS.append(var)
    return var

def convert_type(enum):
    types = {
        Type.INT: 'int',
        Type.FLOAT: 'float',
        Type.STRING: 'string',
    }
    return types[enum]

def type2str(t, dim, ndim):
    if (ndim > dim):
        raise InvalidTypeOperationError(f'Invalid Dimension Array: used {ndim}, max {dim}')

    return f"{t}{'[]' * (dim - ndim)}"

lazy_check_var = []

def search_var(ident, line_no, lazy=False):
    global lazy_check_var
    if scope_stack:
        scope = scope_stack[-1]
        while scope:
            for e in scope.table:
                if e.ident == ident:
                    return e
            
            scope = scope.escopo_pai
        
        if lazy:
            lazy_check_var.append((ident, line_no))
            return
        else:
            raise VariableAlreadyDeclaredError(f'Linha {line_no}: Variável {ident} não declarada')

    raise ScopeNotExistError()

def lazy_check():
    global lazy_check_var

    for var in lazy_check_var:
        search_var(*var)

    lazy_check_var = []


def check_type(left, right, operation, lineno):
    valids = {
        ('string', '+', 'string'): 'string',
        ('string', '+', 'int'): 'string',
        ('string', '+', 'float'): 'string',
        ('int', '+', 'string'): 'string',
        ('float', '+', 'string'): 'string',
        ('int', '+', 'int'): 'int',
        ('int', '-', 'int'): 'int',
        ('int', '*', 'int'): 'int',
        ('int', '%', 'int'): 'int',
        ('int', '/', 'int'): 'float',
        ('float', '+', 'float'): 'float',
        ('float', '-', 'float'): 'float',
        ('float', '*', 'float'): 'float',
        ('float', '/', 'float'): 'float',
        ('float', '+', 'int'): 'float',
        ('float', '-', 'int'): 'float',
        ('float', '*', 'int'): 'float',
        ('float', '/', 'int'): 'float',
        ('int', '+', 'float'): 'float',
        ('int', '-', 'float'): 'float',
        ('int', '*', 'float'): 'float',
        ('int', '/', 'float'): 'float',
    }

    result = valids.get((left.result_type, operation, right.result_type), None)

    if result is None:
        raise InvalidTypeOperationError(f'Error on operation {operation}: {left.result_type},{right.result_type},{lineno}')

    return result

def add_scope(loop):
    parent_scope = scope_stack[-1] if scope_stack else None
    if parent_scope:
        new_scope = Escopo(len(parent_scope.escopos_internos)+1, parent_scope, loop)
        parent_scope.add_inner_scope(new_scope)
    else:
        new_scope = Escopo('global', None, loop)
    scope_stack.append(new_scope)

def num_expressions_as_json():
    output = []

    for exp, line in num_expressions:
        if exp.left == None and exp.right == None:
            continue

        output.append({
            'ID': str(exp),
            'lineno': line,
            'tree': exp.as_json()
        })

    return output

def p_new_loop_label(p):
    '''
    new_loop_label : 
    '''

    global NEXT_LOOP_LABEL
    NEXT_LOOP_LABEL = generate_label()

def p_new_scope(p):
    '''
    new_scope : 
    '''
    add_scope(False)

def p_new_scope_loop(p):
    '''
    new_scope_loop : 
    '''
    add_scope(True)

def p_program_1(p):
    '''
    program : new_scope statement
    '''
    global_scope = scope_stack.pop()
    p[0] = {
        'scopes': global_scope.as_json(),
        'num_expressions': num_expressions_as_json(),
        'code': p[1]['code']
    }


def p_program_2(p):
    '''
    program : new_scope funclist
    '''
    global_scope = scope_stack.pop()
    p[0] = {
        'scopes': global_scope.as_json(),
        'num_expressions': num_expressions_as_json(),
        'code': p[2]['code']
    }

def p_program_3(p):
    '''
    program : 
    '''

def p_funclist(p):
    '''
    funclist : funcdef funclist1
    '''
    p[0] = {
        'code': [*p[1]['code'], *p[2]['code']]
    }

def p_funclist1_1(p):
    '''
    funclist1 : funclist
    '''
    p[0] = {'code': p[1]['code'] }


def p_funclist1_2(p):
    '''
    funclist1 : 
    '''
    p[0] = {'code': []}

def p_funcdef(p):
    '''
    funcdef : DEF IDENT new_scope LPAREN paramlist RPAREN LBRACE statelist RBRACE
    '''

    scope_stack.pop()

    scope = scope_stack[-1]
    entry = EntradaTabela(p[2], 'function', p[5]['dim'], [], p.lineno(2))

    scope.new_entry(entry)

    lazy_check()

    next = generate_label()
    p[0] = { 'code': [f'goto {next}', f'$label:{p[2]}:', *p[5]['code'], *p[8]['code'], f'$label:{next}:'] }

def p_types_1(p):
    '''
    types : INT
    '''
    p[0] = {'type': Type.INT, 'code': p[1]}

def p_types_2(p):
    '''
    types : FLOAT
    '''
    p[0] = {'type': Type.FLOAT, 'code': p[1]}

def p_types_3(p):
    '''
    types : STRING
    '''
    p[0] = {'type': Type.STRING, 'code': p[1]}

def p_paramlist_1(p):
    '''
    paramlist : STRING listdcl IDENT paramlist1 
    '''

    scope = scope_stack[-1]
    entry = EntradaTabela(p[3], 'string', p[2]['dim'], [-1] * p[2]['dim'], p.lineno(3))
    scope.new_entry(entry)

    p[0] = { 'dim': p[4]['dim'] + 1, 'code': [f'from_params {p[3]}', *p[4]['code']] }


def p_paramlist_2(p):
    '''
    paramlist : FLOAT listdcl IDENT paramlist1 
    '''

    scope = scope_stack[-1]
    entry = EntradaTabela(p[3], 'float', p[2]['dim'], [-1] * p[2]['dim'],p.lineno(3))
    scope.new_entry(entry)

    p[0] = { 'dim': p[4]['dim'] + 1, 'code': [f'from_params {p[3]}', *p[4]['code']] }


def p_paramlist_3(p):
    '''
    paramlist : INT listdcl IDENT paramlist1 
    '''
    scope = scope_stack[-1]
    entry = EntradaTabela(p[3], 'int', p[2]['dim'], [-1] * p[2]['dim'], p.lineno(3))
    scope.new_entry(entry)

    p[0] = { 'dim': p[4]['dim'] + 1, 'code': [f'from_params {p[3]}', *p[4]['code']] }


def p_paramlist_4(p):
    '''
    paramlist : 
    '''
    p[0] = { 'dim': 0, 'code': [] }

def p_paramlist1_1(p):
    '''
    paramlist1 : COMMA paramlist
    '''
    p[0] = { 'dim': p[2]['dim'], 'code': p[2]['code'] }

def p_paramlist1_2(p):
    '''
    paramlist1 : 
    '''
    p[0]= { 'dim': 0, 'code': [] }

def p_listdcl_1(p):
    '''
    listdcl : LBRACKET RBRACKET listdcl
    '''
    p[0] = {'dim': p[3]['dim'] + 1, 'code': f"[]{p[3]['code']}"}

def p_listdcl_2(p):
    '''
    listdcl : 
    '''
    p[0] = {'dim': 0, 'code': ''}

def p_statement_1_1(p):
    '''
    statement : INT IDENT statement2
    '''
    entry = EntradaTabela(p[2], str('int'), p[3]['dim'], p[3]['sizes'], p.lineno(2))
    scope = scope_stack[-1]
    scope.new_entry(entry)

    p[0] = {'code': [*p[3]['code'], f"int {p[2]}{p[3]['aux_code']}"]}

def p_statement_1_2(p):
    '''
    statement : FLOAT IDENT statement2
    '''
    entry = EntradaTabela(p[2], str('float'), p[3]['dim'], p[3]['sizes'], p.lineno(2))
    scope = scope_stack[-1]
    scope.new_entry(entry)

    p[0] = {'code': [*p[3]['code'], f"float {p[2]}{p[3]['aux_code']}"]}


def p_statement_1_3(p):
    '''
    statement : STRING IDENT statement2
    '''
    entry = EntradaTabela(p[2], str('string'), p[3]['dim'], p[3]['sizes'], p.lineno(2))
    scope = scope_stack[-1]
    scope.new_entry(entry)

    p[0] = {'code': [*p[3]['code'], f"string {p[2]}{p[3]['aux_code']}"]}


def p_statement_2(p):
    '''
    statement : IDENT statement1
    '''
    var = search_var(p[1], p.lineno(2), p[2]['type'] == 'function')
    if p[2]['type'] == 'function':

        if var is not None:
            if var.type != 'function':
                raise IdentifierNotFunction(f'{p.lineno(2)}')

            if var.dimension != len(p[2]['params']):
                raise ParamCountError(f"Função possui {len(p[2]['params'])} parâmetros, esperado: {var.dimension}")

        p[0] = { 'code': [*p[2]['code'], f"call {p[1]}{p[2]['aux_code']}"]}
    else:
        if p[2]['right_var']['atrib_type'] == 'alloc' and var:
            alloc = p[2]['right_var']['alloc']
            if alloc['type'] != var.type:
                raise InvalidTypeOperationError('Error Type')

            type1 = (var.type, var.dimension - p[2]['left_var_dim'])
            type2 = (alloc['type'], alloc['dim'])

            if type1 != type2:
                raise InvalidTypeOperationError('Error allocating new variable')

        p[0] = { 'code': [*p[2]['code'], f"{p[1]}{p[2]['aux_code']}"]}
    


def p_statement_3(p):
    '''
    statement : printstat SEMICOLON
    '''
    p[0] = { 'code' : p[1]['code'] }
 
def p_statement_4(p):
    '''
    statement : readstat SEMICOLON
    '''
    p[0] = { 'code' : p[1]['code'] }

def p_statement_5(p):
    '''
    statement : returnstat SEMICOLON
    '''
    p[0] = { 'code' : p[1]['code'] }

def p_statement_6(p):
    '''
    statement : ifstat
    '''
    p[0] = { 'code' : p[1]['code'] }

def p_statement_7(p):
    '''
    statement : forstat
    '''
    p[0] = { 'code' : p[1]['code'] }

def p_statement_8(p):
    '''
    statement : whilestat
    '''
    p[0] = { 'code' : p[1]['code'] }

def p_statement_9(p):
    '''
    statement : new_scope LBRACE statelist RBRACE
    '''
    scope_stack.pop()

    p[0] = { 'code' : p[3]['code'] }


def p_statement_10(p):
    '''
    statement : BREAK SEMICOLON
    '''
    scope = scope_stack[-1]
    while scope:
        if scope.loop:
            break

        scope = scope.escopo_pai

    if not scope:
        raise BreakOutLoopError(p.lineno(2))

    p[0] = { 'code': [f'goto {NEXT_LOOP_LABEL}'] }

def p_statement_11(p):
    '''
    statement : SEMICOLON
    '''
    p[0] = { 'code': [] }

def p_statement1_1(p):
    '''
    statement1 : LBRACKET numexpression RBRACKET lvalue1 ASSIGN atribstat1 SEMICOLON
    '''

    p[0] = {
        'type': 'attribution',
        'left_var_dim': p[4]['dim'] + 1,
        'right_var': p[6],
        'code': [*p[2]['code'], *p[4]['code'], *p[6]['code']],
        'aux_code': f"[{p[2]['label']}]{p[4]['aux_code']} = {p[6]['label']}"
    }

def p_statement1_2(p):
    '''
    statement1 : ASSIGN atribstat1 SEMICOLON
    '''
    p[0] = {
        'type': 'attribution',
        'left_var_dim': 0,
        'right_var': p[2],
        'code': p[2]['code'],
        'aux_code': f" = {p[2]['label']}"
    }

def p_statement1_3(p):
    '''
    statement1 : LPAREN paramlistcall RPAREN SEMICOLON
    '''
    p[0] = { 'type': 'function', 'params': p[2]['params'], 'code': p[2]['code'], 'aux_code': f", {len(p[2]['params'])}" }

def p_statement2_1(p):
    '''
    statement2 : LBRACKET numexpression RBRACKET lvalue1 SEMICOLON
    '''
    p[0] = { 
        'dim': p[4]['dim'] + 1,
        'sizes': [str(p[2]['node']), *p[4]['sizes']],
        'code': [*p[2]['code'], *p[4]['code']],
        'aux_code': f"[{p[2]['label']}]{p[4]['aux_code']}"
    }

def p_statement2_2(p):
    '''
    statement2 : SEMICOLON
    '''
    p[0] = { 'dim': 0, 'sizes': [], 'code': [], 'aux_code': '' }

def p_atribstat1_1(p):
    '''
    atribstat1 : expression
    '''
    p[0] = { 'atrib_type' : 'expr', 'node': p[1]['node'], 'code': p[1]['code'], 'label': p[1]['label'] }

def p_atribstat1_2(p):
    '''
    atribstat1 : allocexpression
    '''
    p[0] = { 'atrib_type' : 'alloc', 'alloc': p[1], 'code': p[1]['code'], 'label': p[1]['label'] }

def p_atribstat1_3(p):
    '''
    atribstat1 : funccall
    '''
    p[0] = { 'atrib_type' : 'funccall', 'function': p[1], 'code': p[1]['code'], 'label': p[1]['label'] }

def p_funccall(p):
    '''
    funccall : IDENT LPAREN paramlistcall RPAREN
    '''
    var = search_var(p[1], p.lineno(2))

    if var:
        if var.type != 'function':
            raise IdentifierNotFunction(f'{p.lineno(2)}')

        if var.dimension != len(p[3]['params']):
            raise ParamCountError(f"Função possui {len(p[3]['params'])} parâmetros, esperado: {var.dimension}")

    tvar = get_var()

    p[0] = { 'code': [*p[3]['code'], f"{tvar} = call {p[1]}, {len(p[3]['params'])}"], 'label': tvar }
    
def p_paramlistcall_1(p):
    '''
    paramlistcall : factor paramlistcall2
    '''
    scope = scope_stack[-1]

    if 'vartype' in p[1] and p[1]['vartype'] != 'ident':
        var = EntradaTabela(f't{scope.tempcontador.inc()}', p[1]['type'], p[1]['dim'], p[1]['sizes'], p.lineno(2))
        if p[2]['array']:
            raise TypeError(f"{p[1]['label']} is not an array")
    elif p[1]['label'] not in VARS:
        var = search_var(p[1]['label'], p.lineno(2))
    else:
        var = p[1]['label']

    p[0] = { 'params': [var, *p[2]['params']], 'code': [f"param {p[1]['label']}{p[2]['aux_code']}", *p[2]['code']] }

def p_paramlistcall_2(p):
    '''
    paramlistcall : 
    '''
    p[0] = { 'params': [], 'code': [] }

def p_paramlistcall1_1(p):
    '''
    paramlistcall1 : COMMA paramlistcall
    '''
    p[0] = { 'params': p[2]['params'], 'code': p[2]['code'] }

def p_paramlistcall1_2(p):
    '''
    paramlistcall1 : 
    '''
    p[0] = { 'params': [], 'code': [] }

def p_paramlistcall2_1(p):
    '''
    paramlistcall2 : LBRACKET numexpression RBRACKET lvalue1 paramlistcall1
    '''
    p[0] = {
        'array': True,
        'dim': p[4]['dim'] + 1,
        'sizes': [str(p[2]['node']), *p[4]['sizes']],
        'params': p[5]['params'],
        'code': [*p[2]['code'], *p[4]['code'], *p[5]['code']],
        'aux_code': f"[{p[2]['label']}]{p[4]['aux_code']}"
    }

def p_paramlistcall2_2(p):
    '''
    paramlistcall2 : paramlistcall1
    '''
    p[0] = {
        'array': False,
        'code': p[1]['code'],
        'params': p[1]['params'],
        'aux_code': ''
    }

def p_printstat(p):
    '''
    printstat : PRINT expression
    '''
    p[0] = { 'code': [*p[2]['code'], f"print {p[2]['label']}"] }

def p_readstat(p):
    '''
    readstat : READ expression
    '''
    p[0] = { 'code': [*p[2]['code'], f"read {p[2]['label']}"] }

def p_returnstat(p):
    '''
    returnstat : RETURN returnstat1
    '''
    p[0] = { 'code': [*p[2]['code'], f"return {p[2]['label']}"] }


def p_returnstat1_2(p):
    '''
    returnstat1 : expression
    '''
    p[0] = p[1]

def p_returnstat1_3(p):
    '''
    returnstat1 : 
    '''
    p[0] = { 'code': [], 'label': '' }

def p_ifstat(p):
    '''
    ifstat : IF LPAREN expression RPAREN statement ifstat1
    '''
    end_if_label = generate_label()
    if 'label' in p[6]:
        next = p[6]['label']

        p[0] = {
            'code': [
                *p[3]['code'],
                f"if False {p[3]['label']} goto {next}",
                *p[5]['code'],
                f"goto {end_if_label}",
                *p[6]['code'],
                f'$label:{end_if_label}:'
            ]
        }
    else:
        p[0] = {
            'code': [
                *p[3]['code'],
                f"if False {p[3]['label']} goto {end_if_label}",
                *p[5]['code'],
                f'$label:{end_if_label}:'
            ]
        }

def p_ifstat1_1(p):
    '''
    ifstat1 : ELSE statement
    '''
    label = generate_label()
    p[0] = {
        'code': [f'$label:{label}:', *p[2]['code']],
        'label': label
    }

def p_ifstat1_2(p):
    '''
    ifstat1 : %prec IF
    '''
    p[0] = { 'code': [] }

def p_forstat(p):
    '''
    forstat : new_loop_label FOR LPAREN forstat1 SEMICOLON forstat2 SEMICOLON forstat1 RPAREN new_scope_loop LBRACE statelist RBRACE
    '''
    scope_stack.pop()

    start = generate_label()
    next_label = NEXT_LOOP_LABEL

    p[0] = {
        'code': [
            *p[4]['code'],
            f'$label:{start}:',
            *p[6]['code'],
            *([f"if False {p[6]['label']} goto {next_label}"] if p[6]['label'] else []),
            *p[12]['code'],
            *p[8]['code'],
            f'goto {start}',
            f'$label:{next_label}:',
        ]
    }

def p_forstat1_1(p):
    '''
    forstat1 : IDENT forstat3
    '''
    search_var(p[1], p.lineno(1))
    p[0] = { 'code': [*p[2]['code'], f"{p[1]} {p[2]['aux_code']}"] }

def p_forstat1_2(p):
    '''
    forstat1 : 
    '''
    p[0] = { 'code': [] }

def p_forstat2_1(p):
    '''
    forstat2 : expression
    '''

    p[0] = { 'code': p[1]['code'], 'label': p[1]['label'] }

def p_forstat2_2(p):
    '''
    forstat2 : 
    '''
    p[0] = { 'code': [], 'label': None }

def p_forstat3_1(p):
    '''
    forstat3 : LBRACKET numexpression RBRACKET lvalue1 ASSIGN atribstat1
    '''
    p[0] = { 'code': [*p[2]['code'], *p[4]['code']], 'aux_code': f"[{p[2]['label']}]{p[4]['aux_code']} = {p[6]['label']}" }

def p_forstat3_2(p):
    '''
    forstat3 : ASSIGN atribstat1
    '''
    p[0] = { 'code': p[2]['code'], 'aux_code': f"= {p[2]['label']}" }

def p_whilestat(p):
    '''
    whilestat : new_loop_label WHILE LPAREN expression RPAREN new_scope_loop LBRACE statelist RBRACE
    '''
    scope_stack.pop()

    start = generate_label()
    next = NEXT_LOOP_LABEL

    p[0] = {
        'code': [
            f'$label:{start}:',
            *p[4]['code'],
            f"if False {p[4]['label']} goto {next}",
            *p[8]['code'],
            f'goto {start}',
            f'$label:{next}:',
        ]
    }

def p_statelist(p):
    '''
    statelist : statement statelist1
    '''
    p[0] = { 'code': [*p[1]['code'], *p[2]['code']] }

def p_statelist1_1(p):
    '''
    statelist1 : statelist
    '''
    p[0] = { 'code': p[1]['code'] }

def p_statelist1_2(p):
    '''
    statelist1 :
    '''
    p[0] = { 'code': [] }


def p_allocexpression(p):
    '''
    allocexpression : NEW types LBRACKET numexpression RBRACKET lvalue1
    '''
    num_expressions.append((p[4]['node'], p.lineno(4)))

    var = get_var()

    p[0] = {
        'type': convert_type(p[2]['type']),
        'dim': p[6]['dim'] + 1,
        'label': var,
        'code': [*p[4]['code'], *p[6]['code'], f"{var} = new {p[2]['code']}[{p[4]['label']}]{p[6]['aux_code']}"], 
    }

def p_expression(p):
    '''
    expression : numexpression expression1
    '''
    if p[2]['code']:
        rvar = get_var()
        p[0] = {
            'node': Node(p[2]['operator'], p[1]['node'], p[2]['node'], 'bool'),
            'label': rvar,
            'code': [
                *p[1]['code'],
                *p[2]['code'],
                f"{rvar} = {p[1]['label']}" + (f" {p[2]['operator']} {p[2]['label']}" if len(p[2]['code']) > 0 else "")
            ]
        }
    else:
        p[0] = p[1]

    num_expressions.append((p[0]['node'], p.lineno(1)))


def p_expression1_1(p):
    '''
    expression1 : compoperator numexpression
    '''
    p[0] = { 
        'operator': p[1],
        'node': p[2]['node'],
        'label': p[2]['label'],
        'code': p[2]['code']
    }

def p_expression1_2(p):
    '''
    expression1 : 
    '''
    p[0] = { 'code': '' }

def p_compoperator_1(p):
    '''
    compoperator : GT
    '''
    p[0] = '>'

def p_compoperator_2(p):
    '''
    compoperator : LT
    '''
    p[0] = '<'

def p_compoperator_3(p):
    '''
    compoperator : GE
    '''
    p[0] = '>='

def p_compoperator_4(p):
    '''
    compoperator : LE
    '''
    p[0] = '<='

def p_compoperator_5(p):
    '''
    compoperator : EQ
    '''
    p[0] = '=='

def p_compoperator_6(p):
    '''
    compoperator : NEQ
    '''
    p[0] = '!='

def p_numexpression(p):
    '''
    numexpression : term numexpression1
    '''
    if p[2]['code']:
        rtype = check_type(p[1]['node'], p[2]['node'], p[2]['operator'], p.lineno(1))

        var = get_var()
        p[0] = { 
            'node': Node(p[2]['operator'], p[1]['node'], p[2]['node'], rtype),
            'code': [*p[1]['code'], *p[2]['code'], f"{var} = {p[1]['label']} {p[2]['operator']} {p[2]['label']}"],
            'label': var
        }
    else:
        p[0] = p[1]

    

def p_numexpression1_1(p):
    '''
    numexpression1 : addsub term
    '''
    p[0] = { 'node': p[2]['node'], 'operator': p[1], 'code': p[2]['code'], 'label': p[2]['label'] }

def p_numexpression1_2(p):
    '''
    numexpression1 : 
    '''
    p[0] = { 'code': [] }

def p_addsub_1(p):
    '''
    addsub : PLUS
    '''
    p[0] = '+'

def p_addsub_2(p):
    '''
    addsub : MINUS
    '''
    p[0] = '-'

def p_term(p):
    '''
    term : unaryexpr term1
    '''

    if p[2]['code']:
        rtype = check_type(p[1]['node'], p[2]['node'], p[2]['operator'], p.lineno(1))

        var = get_var()


        p[0] = {
            'node': Node(p[2]['operator'], p[1]['node'], p[2]['node'], rtype),
            'code': [*p[1]['code'], f"{var} = {p[1]['label']} {p[2]['operator']} {p[2]['label']}"],
            'label': var
        } 
    else:
        p[0] = p[1]

def p_term1_1(p):
    '''
    term1 : multdiv unaryexpr term1
    '''
    if p[3]['code']:
        rtype = check_type(p[2]['node'], p[3]['node'], p[3]['operator'], p.lineno(1))

        var = get_var()

        p[0] = { 
            'node': Node(p[3]['operator'], p[2]['node'], p[3]['node'], rtype), 
            'operator': p[1],
            'code': [*p[2]['code'], *p[3]['code'], f"{var} = {p[2]['label']} {p[3]['operator']} {p[3]['label']}"],
            'label': var
        }
    else:
        p[0] = { 'node': p[2]['node'], 'operator': p[1], 'code': p[2]['code'], 'label': p[2]['label'] }

def p_term1_2(p):
    '''
    term1 : 
    '''
    p[0] = { 'code': [] }

def p_multdiv_1(p):
    '''
    multdiv : MULTIPLY
    '''
    p[0] = '*'

def p_multdiv_2(p):
    '''
    multdiv : DIVIDE
    '''
    p[0] = '/'

def p_multdiv_3(p):
    '''
    multdiv : REM
    '''
    p[0] = '%'

def p_unaryexpr_1(p):
    '''
    unaryexpr : addsub factor
    '''
    if (p[1] == '-'):
        p[2]['node'].value *= -1

    var = get_var()

    p[0] = { 'node': p[2]['node'], 'code': [*p[2]['code'], *([f"{var} = {p[1]}{p[2]['label']}"] if p[1] == '-' else [])], 'label': var }

def p_unaryexpr_2(p):
    '''
    unaryexpr : factor
    '''
    p[0] = p[1]

def p_factor_1(p):
    '''
    factor : int_constant
    '''
    var = get_var()

    p[0] = { 'node': Node(p[1], None, None, 'int'), 'code': [f'{var} = {p[1]}'], 'label': var }

def p_factor_2(p):
    '''
    factor : float_constant
    '''
    var = get_var()

    p[0] = { 'node': Node(p[1], None, None, 'float'), 'code': [f'{var} = {p[1]}'], 'label': var  }

def p_factor_3(p):
    '''
    factor : string_constant
    '''
    var = get_var()

    p[0] = { 'node': Node(p[1], None, None, 'string'), 'code': [f'{var} = {p[1]}'], 'label': var  }

def p_factor_4(p):
    '''
    factor : null_constant
    '''
    var = get_var()

    p[0] = { 'node': Node('null', None, None, 'null'), 'code': [f'{var} = {p[1]}'], 'label': var }

def p_factor_5(p):
    '''
    factor : IDENT lvalue1
    '''
    var = search_var(p[1], p.lineno(1))

    nvar = get_var()
    if var:
        p[0] = {
            'node': Node(p[1] + p[2]['expression'], None, None, type2str(var.type, var.dimension, p[2]['dim'])),
            'code': [f"{nvar} = {p[1]}{p[2]['aux_code']}"],
            'label': nvar,
            'vartype': 'ident'
        }

def p_factor_6(p):
    '''
    factor : LPAREN numexpression RPAREN
    '''
    p[0] = p[2]

    num_expressions.append((p[2]['node'], p.lineno(1)))

def p_lvalue1_1(p):
    '''
    lvalue1 : LBRACKET numexpression RBRACKET lvalue1
    '''
    p[0] = {
        'dim': p[4]['dim'] + 1,
        'sizes': [str(p[2]['node']), *p[4]['sizes']],
        'expression':  f'[{str(p[2])}]{p[4]}',
        'code': [*p[2]['code'], *p[4]['code']],
        'aux_code': f"[{p[2]['label']}]{p[4]['aux_code']}"
    }

    num_expressions.append((p[2]['node'], p.lineno(1)))

def p_lvalue1_2(p):
    '''
    lvalue1 :
    '''
    p[0] = {
        'dim':  0,
        'sizes': [],
        'expression': '',
        'code': [],
        'aux_code': ''
    }

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

def gci(codes):
    with open('debug/ci.txt', 'w') as f:
        for c in codes:
            f.write(format_code(c))

import json

def analyze(input_value):
    global text
    text = input_value
    result = parser.parse(input=input_value, debug=log)
    gci(result['code'])

    del result['code']

    log.log(logging.INFO, json.dumps(result, indent=2, sort_keys=True))
