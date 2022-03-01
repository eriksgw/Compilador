
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programnonassocIFleftELSEleftLBRACKETASSIGN BREAK COMMA DEF DIVIDE ELSE EQ FLOAT FOR GE GT IDENT IF INT LBRACE LBRACKET LE LPAREN LT MINUS MULTIPLY NEQ NEW PLUS PRINT RBRACE RBRACKET READ REM RETURN RPAREN SEMICOLON STRING WHILE float_constant int_constant null_constant string_constant\n    program : statement\n    \n    program : funclist\n    \n    program : \n    \n    funclist : funcdef funclist1\n    \n    funclist1 : DEF IDENT LPAREN paramlist RPAREN LBRACE statelist RBRACE funclist1\n    \n    funclist1 : \n    \n    funcdef : DEF IDENT LPAREN paramlist RPAREN LBRACE statelist RBRACE\n    \n    types : INT\n    \n    types : FLOAT\n    \n    types : STRING\n    \n    paramlist : STRING listdcl IDENT paramlist1 \n    \n    paramlist : FLOAT listdcl IDENT paramlist1 \n    \n    paramlist : INT listdcl IDENT paramlist1 \n    \n    paramlist : \n    \n    paramlist1 : COMMA paramlist\n    \n    paramlist1 : \n    \n    listdcl : LBRACKET RBRACKET listdcl\n    \n    listdcl : \n    \n    statement : INT IDENT statement2\n    \n    statement : FLOAT IDENT statement2\n    \n    statement : STRING IDENT statement2\n    \n    statement : IDENT statement1\n    \n    statement : printstat SEMICOLON\n    \n    statement : readstat SEMICOLON\n    \n    statement : returnstat SEMICOLON\n    \n    statement : ifstat\n    \n    statement : forstat\n    \n    statement : whilestat\n    \n    statement : LBRACE statelist RBRACE\n    \n    statement : BREAK SEMICOLON\n    \n    statement : SEMICOLON\n    \n    statement1 : LBRACKET numexpression RBRACKET lvalue1 ASSIGN atribstat1 SEMICOLON\n    \n    statement1 : ASSIGN atribstat1 SEMICOLON\n    \n    statement1 : LPAREN paramlistcall RPAREN SEMICOLON\n    \n    statement2 : LBRACKET numexpression RBRACKET lvalue1 SEMICOLON\n    \n    statement2 : SEMICOLON\n    \n    atribstat1 : expression\n    \n    atribstat1 : allocexpression\n    \n    atribstat1 : funccall\n    \n    funccall : IDENT LPAREN paramlistcall RPAREN\n    \n    paramlistcall : factor paramlistcall2\n    \n    paramlistcall : \n    \n    paramlistcall1 : COMMA paramlistcall\n    \n    paramlistcall1 : \n    \n    paramlistcall2 : LBRACKET numexpression RBRACKET lvalue1 paramlistcall1\n    \n    paramlistcall2 : paramlistcall1\n    \n    printstat : PRINT expression\n    \n    readstat : READ expression\n    \n    returnstat : RETURN returnstat1\n    \n    returnstat1 : expression\n    \n    returnstat1 : \n    \n    ifstat : IF LPAREN expression RPAREN statement ifstat1\n    \n    ifstat1 : ELSE statement\n    \n    ifstat1 : %prec IF\n    \n    forstat : FOR LPAREN forstat1 SEMICOLON forstat2 SEMICOLON forstat1 RPAREN statement\n    \n    forstat1 : IDENT forstat3\n    \n    forstat1 : \n    \n    forstat2 : expression\n    \n    forstat2 : \n    \n    forstat3 : LBRACKET numexpression RBRACKET lvalue1 ASSIGN atribstat1\n    \n    forstat3 : ASSIGN atribstat1\n    \n    whilestat : WHILE LPAREN expression RPAREN statement\n    \n    statelist : INT listdcl IDENT statelist2\n    \n    statelist : FLOAT listdcl IDENT statelist2\n    \n    statelist : STRING listdcl IDENT statelist2\n    \n    statelist : IDENT statelist3\n    \n    statelist : PRINT expression SEMICOLON statelist1\n    \n    statelist : READ IDENT statelist2\n    \n    statelist : RETURN returnstat1 SEMICOLON statelist1\n    \n    statelist : IF LPAREN expression RPAREN statement ifstat1 statelist1\n    \n    statelist : FOR LPAREN forstat1 SEMICOLON forstat2 SEMICOLON forstat1 RPAREN statement statelist1\n    \n    statelist : WHILE LPAREN expression RPAREN statement statelist1\n    \n    statelist : LBRACE statelist RBRACE statelist1\n    \n    statelist : BREAK SEMICOLON statelist1\n    \n    statelist : SEMICOLON statelist1\n    \n    statelist : IDENT LPAREN paramlistcall RPAREN SEMICOLON statelist1\n    \n    statelist1 : INT listdcl IDENT statelist2\n    \n    statelist1 : FLOAT listdcl IDENT statelist2\n    \n    statelist1 : STRING listdcl IDENT statelist2\n    \n    statelist1 : IDENT statelist3\n    \n    statelist1 : PRINT expression SEMICOLON statelist1\n    \n    statelist1 : READ IDENT statelist2\n    \n    statelist1 : RETURN returnstat1 SEMICOLON statelist1\n    \n    statelist1 : IF LPAREN expression RPAREN statement ifstat1 statelist1\n    \n    statelist1 : FOR LPAREN forstat1 SEMICOLON forstat2 SEMICOLON forstat1 RPAREN statement statelist1\n    \n    statelist1 : WHILE LPAREN expression RPAREN statement statelist1\n    \n    statelist1 : LBRACE statelist RBRACE statelist1\n    \n    statelist1 : BREAK SEMICOLON statelist1\n    \n    statelist1 : SEMICOLON statelist1\n    \n    statelist1 : IDENT LPAREN paramlistcall RPAREN SEMICOLON statelist1\n    \n    statelist1 : \n    \n    statelist2 : LBRACKET numexpression RBRACKET lvalue1 SEMICOLON statelist1\n    \n    statelist2 : SEMICOLON statelist1\n    \n    statelist3 : LBRACKET numexpression RBRACKET lvalue1 ASSIGN atribstat1 SEMICOLON statelist1\n    \n    statelist3 : ASSIGN atribstat1 SEMICOLON statelist1\n    \n    allocexpression : NEW types LBRACKET numexpression RBRACKET lvalue1\n    \n    expression : numexpression expression1\n    \n    expression1 : compoperator numexpression\n    \n    expression1 : \n    \n    compoperator : GT\n    \n    compoperator : LT\n    \n    compoperator : GE\n    \n    compoperator : LE\n    \n    compoperator : EQ\n    \n    compoperator : NEQ\n    \n    numexpression : term numexpression1\n    \n    numexpression1 : addsub term\n    \n    numexpression1 : \n    \n    addsub : PLUS\n    \n    addsub : MINUS\n    \n    term : unaryexpr term1\n    \n    term1 : multdiv unaryexpr term1\n    \n    term1 : \n    \n    multdiv : MULTIPLY\n    \n    multdiv : DIVIDE\n    \n    multdiv : REM\n    \n    unaryexpr : addsub factor\n    \n    unaryexpr : factor\n    \n    factor : int_constant\n    \n    factor : float_constant\n    \n    factor : string_constant\n    \n    factor : null_constant\n    \n    factor : IDENT lvalue1\n    \n    factor : LPAREN numexpression RPAREN\n    \n    lvalue1 : LBRACKET numexpression RBRACKET lvalue1\n    \n    lvalue1 : \n    '
    
_lr_action_items = {'$end':([0,1,2,3,9,12,13,14,17,26,32,33,34,49,50,73,75,85,86,88,145,207,240,245,274,282,297,305,319,326,327,332,],[-3,0,-1,-2,-31,-26,-27,-28,-6,-22,-23,-24,-25,-30,-4,-19,-36,-20,-21,-29,-33,-34,-54,-62,-52,-35,-53,-32,-7,-6,-55,-5,]),'INT':([0,9,12,13,14,15,26,32,33,34,35,42,49,73,75,81,85,86,88,98,110,117,142,145,156,164,178,181,182,187,193,198,207,215,223,225,229,234,236,240,245,255,264,266,269,271,274,275,278,282,288,289,291,293,296,297,302,305,310,313,317,321,325,327,330,331,333,],[4,-31,-26,-27,-28,37,-22,-23,-24,-25,37,100,-30,-19,-36,147,-20,-21,-29,100,37,100,202,-33,100,100,100,100,100,202,4,4,-34,100,100,100,100,4,4,-54,-62,100,4,4,-54,100,-52,4,37,-35,100,-54,100,100,37,-53,202,-32,100,100,4,100,4,-55,4,100,100,]),'FLOAT':([0,9,12,13,14,15,26,32,33,34,35,42,49,73,75,81,85,86,88,98,110,117,142,145,156,164,178,181,182,187,193,198,207,215,223,225,229,234,236,240,245,255,264,266,269,271,274,275,278,282,288,289,291,293,296,297,302,305,310,313,317,321,325,327,330,331,333,],[6,-31,-26,-27,-28,39,-22,-23,-24,-25,39,102,-30,-19,-36,148,-20,-21,-29,102,39,102,201,-33,102,102,102,102,102,201,6,6,-34,102,102,102,102,6,6,-54,-62,102,6,6,-54,102,-52,6,39,-35,102,-54,102,102,39,-53,201,-32,102,102,6,102,6,-55,6,102,102,]),'STRING':([0,9,12,13,14,15,26,32,33,34,35,42,49,73,75,81,85,86,88,98,110,117,142,145,156,164,178,181,182,187,193,198,207,215,223,225,229,234,236,240,245,255,264,266,269,271,274,275,278,282,288,289,291,293,296,297,302,305,310,313,317,321,325,327,330,331,333,],[7,-31,-26,-27,-28,40,-22,-23,-24,-25,40,103,-30,-19,-36,149,-20,-21,-29,103,40,103,200,-33,103,103,103,103,103,200,7,7,-34,103,103,103,103,7,7,-54,-62,103,7,7,-54,103,-52,7,40,-35,103,-54,103,103,40,-53,200,-32,103,103,7,103,7,-55,7,103,103,]),'IDENT':([0,4,6,7,9,12,13,14,15,18,19,20,24,26,27,28,29,32,33,34,35,37,39,40,41,42,43,44,49,51,56,58,59,65,69,70,71,73,74,75,85,86,88,89,92,93,94,95,96,98,100,102,103,104,105,106,110,114,115,116,117,120,121,122,123,124,125,126,128,130,131,132,133,136,145,150,153,155,156,158,164,166,168,169,170,174,175,176,178,180,181,182,193,194,196,197,198,200,201,202,205,207,212,215,223,225,229,234,235,236,240,245,247,248,249,251,255,264,265,266,269,271,274,275,276,278,282,287,288,289,291,293,294,296,297,305,310,311,313,317,318,321,325,327,330,331,333,],[5,25,30,31,-31,-26,-27,-28,38,64,64,64,72,-22,64,82,64,-23,-24,-25,38,-18,-18,-18,64,101,112,64,-30,118,64,-109,-110,64,64,140,64,-19,64,-36,-20,-21,-29,157,64,64,82,162,163,101,-18,-18,-18,64,172,64,38,64,140,64,101,64,-100,-101,-102,-103,-104,-105,64,64,-114,-115,-116,64,-33,64,64,64,101,-18,101,219,64,221,222,64,140,64,101,64,101,101,5,64,64,82,5,-18,-18,-18,64,-34,-17,101,101,101,101,5,64,5,-54,-62,279,280,281,82,101,5,64,5,-54,101,-52,5,140,38,-35,82,101,-54,101,101,140,38,-53,-32,101,140,101,5,82,101,5,-55,5,101,101,]),'LBRACE':([0,9,12,13,14,15,26,32,33,34,35,42,49,73,75,85,86,88,98,110,117,145,156,164,178,181,182,193,198,207,215,223,225,229,234,236,240,245,246,255,264,266,269,271,272,274,275,278,282,288,289,291,293,296,297,305,310,313,317,321,325,327,330,331,333,],[15,-31,-26,-27,-28,35,-22,-23,-24,-25,35,110,-30,-19,-36,-20,-21,-29,110,35,110,-33,110,110,110,110,110,15,15,-34,110,110,110,110,15,15,-54,-62,278,110,15,15,-54,110,296,-52,15,35,-35,110,-54,110,110,35,-53,-32,110,110,15,110,15,-55,15,110,110,]),'BREAK':([0,9,12,13,14,15,26,32,33,34,35,42,49,73,75,85,86,88,98,110,117,145,156,164,178,181,182,193,198,207,215,223,225,229,234,236,240,245,255,264,266,269,271,274,275,278,282,288,289,291,293,296,297,305,310,313,317,321,325,327,330,331,333,],[16,-31,-26,-27,-28,48,-22,-23,-24,-25,48,111,-30,-19,-36,-20,-21,-29,111,48,111,-33,111,111,111,111,111,16,16,-34,111,111,111,111,16,16,-54,-62,111,16,16,-54,111,-52,16,48,-35,111,-54,111,111,48,-53,-32,111,111,16,111,16,-55,16,111,111,]),'SEMICOLON':([0,8,9,10,11,12,13,14,15,16,20,25,26,30,31,32,33,34,35,42,44,48,49,52,53,54,55,57,60,61,62,63,64,66,67,68,70,73,75,77,78,79,80,82,85,86,88,97,98,106,110,111,112,113,115,117,119,127,129,134,135,139,145,151,156,157,161,162,163,164,171,172,173,175,178,181,182,184,188,189,190,192,193,194,195,198,203,207,213,215,219,221,222,223,225,227,229,234,235,236,238,239,240,241,242,244,245,250,253,255,259,264,265,266,268,269,270,271,273,274,275,278,282,283,284,288,289,290,291,292,293,296,297,305,306,308,310,313,317,321,325,327,328,330,331,333,],[9,32,-31,33,34,-26,-27,-28,42,49,-51,75,-22,75,75,-23,-24,-25,42,98,-51,117,-30,-47,-99,-108,-113,-118,-119,-120,-121,-122,-126,-48,-49,-50,-57,-19,-36,145,-37,-38,-39,-126,-20,-21,-29,164,98,-51,42,178,181,182,-57,98,-97,-106,-111,-117,-123,194,-33,207,98,181,215,181,181,98,223,181,225,-57,98,98,98,235,-98,-107,-113,-124,9,-59,-56,9,-126,-34,255,98,181,181,181,98,98,265,98,9,-59,9,-112,-126,-54,276,-58,-61,-62,282,-40,98,288,9,-59,9,-126,-54,294,98,-125,-52,9,42,-35,305,-126,98,-54,311,98,313,98,42,-53,-32,-96,321,98,98,9,98,9,-55,-60,9,98,98,]),'PRINT':([0,9,12,13,14,15,26,32,33,34,35,42,49,73,75,85,86,88,98,110,117,145,156,164,178,181,182,193,198,207,215,223,225,229,234,236,240,245,255,264,266,269,271,274,275,278,282,288,289,291,293,296,297,305,310,313,317,321,325,327,330,331,333,],[18,-31,-26,-27,-28,41,-22,-23,-24,-25,41,104,-30,-19,-36,-20,-21,-29,104,41,104,-33,104,104,104,104,104,18,18,-34,104,104,104,104,18,18,-54,-62,104,18,18,-54,104,-52,18,41,-35,104,-54,104,104,41,-53,-32,104,104,18,104,18,-55,18,104,104,]),'READ':([0,9,12,13,14,15,26,32,33,34,35,42,49,73,75,85,86,88,98,110,117,145,156,164,178,181,182,193,198,207,215,223,225,229,234,236,240,245,255,264,266,269,271,274,275,278,282,288,289,291,293,296,297,305,310,313,317,321,325,327,330,331,333,],[19,-31,-26,-27,-28,43,-22,-23,-24,-25,43,105,-30,-19,-36,-20,-21,-29,105,43,105,-33,105,105,105,105,105,19,19,-34,105,105,105,105,19,19,-54,-62,105,19,19,-54,105,-52,19,43,-35,105,-54,105,105,43,-53,-32,105,105,19,105,19,-55,19,105,105,]),'RETURN':([0,9,12,13,14,15,26,32,33,34,35,42,49,73,75,85,86,88,98,110,117,145,156,164,178,181,182,193,198,207,215,223,225,229,234,236,240,245,255,264,266,269,271,274,275,278,282,288,289,291,293,296,297,305,310,313,317,321,325,327,330,331,333,],[20,-31,-26,-27,-28,44,-22,-23,-24,-25,44,106,-30,-19,-36,-20,-21,-29,106,44,106,-33,106,106,106,106,106,20,20,-34,106,106,106,106,20,20,-54,-62,106,20,20,-54,106,-52,20,44,-35,106,-54,106,106,44,-53,-32,106,106,20,106,20,-55,20,106,106,]),'IF':([0,9,12,13,14,15,26,32,33,34,35,42,49,73,75,85,86,88,98,110,117,145,156,164,178,181,182,193,198,207,215,223,225,229,234,236,240,245,255,264,266,269,271,274,275,278,282,288,289,291,293,296,297,305,310,313,317,321,325,327,330,331,333,],[21,-31,-26,-27,-28,45,-22,-23,-24,-25,45,107,-30,-19,-36,-20,-21,-29,107,45,107,-33,107,107,107,107,107,21,21,-34,107,107,107,107,21,21,-54,-62,107,21,21,-54,107,-52,21,45,-35,107,-54,107,107,45,-53,-32,107,107,21,107,21,-55,21,107,107,]),'FOR':([0,9,12,13,14,15,26,32,33,34,35,42,49,73,75,85,86,88,98,110,117,145,156,164,178,181,182,193,198,207,215,223,225,229,234,236,240,245,255,264,266,269,271,274,275,278,282,288,289,291,293,296,297,305,310,313,317,321,325,327,330,331,333,],[22,-31,-26,-27,-28,46,-22,-23,-24,-25,46,108,-30,-19,-36,-20,-21,-29,108,46,108,-33,108,108,108,108,108,22,22,-34,108,108,108,108,22,22,-54,-62,108,22,22,-54,108,-52,22,46,-35,108,-54,108,108,46,-53,-32,108,108,22,108,22,-55,22,108,108,]),'WHILE':([0,9,12,13,14,15,26,32,33,34,35,42,49,73,75,85,86,88,98,110,117,145,156,164,178,181,182,193,198,207,215,223,225,229,234,236,240,245,255,264,266,269,271,274,275,278,282,288,289,291,293,296,297,305,310,313,317,321,325,327,330,331,333,],[23,-31,-26,-27,-28,47,-22,-23,-24,-25,47,109,-30,-19,-36,-20,-21,-29,109,47,109,-33,109,109,109,109,109,23,23,-34,109,109,109,109,23,23,-54,-62,109,23,23,-54,109,-52,23,47,-35,109,-54,109,109,47,-53,-32,109,109,23,109,23,-55,23,109,109,]),'DEF':([0,17,319,326,],[24,51,-7,51,]),'LBRACKET':([5,25,30,31,37,38,39,40,60,61,62,63,64,82,84,100,101,102,103,112,135,140,144,146,147,148,149,157,158,162,163,172,192,200,201,202,203,214,219,221,222,239,254,268,273,277,284,],[27,74,74,74,90,93,90,90,-119,-120,-121,-122,136,136,153,90,93,90,90,180,-123,196,136,205,-8,-9,-10,180,90,180,180,180,-124,90,90,90,136,136,180,180,180,136,136,136,-125,136,136,]),'ASSIGN':([5,38,101,140,144,204,214,239,256,273,277,299,],[28,94,94,197,-126,251,-126,-126,287,-125,-126,318,]),'LPAREN':([5,18,19,20,21,22,23,27,28,29,38,41,44,45,46,47,56,58,59,65,69,71,72,74,82,92,93,94,101,104,106,107,108,109,114,116,118,120,121,122,123,124,125,126,128,130,131,132,133,136,150,153,155,168,174,176,180,194,196,197,205,235,251,265,287,318,],[29,65,65,65,69,70,71,65,65,65,92,65,65,114,115,116,65,-109,-110,65,65,65,142,65,150,65,65,65,168,65,65,174,175,176,65,65,187,65,-100,-101,-102,-103,-104,-105,65,65,-114,-115,-116,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'ELSE':([9,12,13,14,26,32,33,34,49,73,75,85,86,88,145,207,240,245,269,274,282,289,297,305,327,],[-31,-26,-27,-28,-22,-23,-24,-25,-30,-19,-36,-20,-21,-29,-33,-34,275,-62,275,-52,-35,275,-53,-32,-55,]),'RBRACE':([9,12,13,14,26,32,33,34,36,42,49,73,75,85,86,87,88,91,98,99,117,145,156,164,165,167,177,178,179,181,182,186,207,210,211,215,216,217,218,223,224,225,229,230,232,233,240,245,255,257,258,260,261,262,263,267,269,271,274,282,286,288,289,291,293,295,297,300,305,309,310,312,313,314,316,321,322,324,327,329,331,333,334,335,],[-31,-26,-27,-28,-22,-23,-24,-25,88,-91,-30,-19,-36,-20,-21,156,-29,-66,-91,-75,-91,-33,-91,-91,-89,-80,229,-91,-68,-91,-91,-74,-34,-73,-63,-91,-64,-65,-67,-91,-82,-91,-91,-88,-93,-69,-54,-62,-91,-95,-77,-78,-79,-81,-83,-87,-54,-91,-52,-35,-76,-91,-54,-91,-91,-72,-53,319,-32,-90,-91,-86,-91,-70,326,-91,-84,-92,-55,-94,-91,-91,-71,-85,]),'PLUS':([18,19,20,27,28,41,44,54,55,57,58,59,60,61,62,63,64,65,69,71,74,82,93,94,104,106,114,116,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,136,153,174,176,180,190,192,194,196,197,205,235,238,239,251,265,273,287,318,],[58,58,58,58,58,58,58,58,-113,-118,-109,-110,-119,-120,-121,-122,-126,58,58,58,58,-126,58,58,58,58,58,58,58,-100,-101,-102,-103,-104,-105,58,-111,58,-114,-115,-116,-117,-123,58,58,58,58,58,-113,-124,58,58,58,58,58,-112,-126,58,58,-125,58,58,]),'MINUS':([18,19,20,27,28,41,44,54,55,57,58,59,60,61,62,63,64,65,69,71,74,82,93,94,104,106,114,116,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,136,153,174,176,180,190,192,194,196,197,205,235,238,239,251,265,273,287,318,],[59,59,59,59,59,59,59,59,-113,-118,-109,-110,-119,-120,-121,-122,-126,59,59,59,59,-126,59,59,59,59,59,59,59,-100,-101,-102,-103,-104,-105,59,-111,59,-114,-115,-116,-117,-123,59,59,59,59,59,-113,-124,59,59,59,59,59,-112,-126,59,59,-125,59,59,]),'int_constant':([18,19,20,27,28,29,41,44,56,58,59,65,69,71,74,92,93,94,104,106,114,116,120,121,122,123,124,125,126,128,130,131,132,133,136,150,153,155,168,174,176,180,194,196,197,205,235,251,265,287,318,],[60,60,60,60,60,60,60,60,60,-109,-110,60,60,60,60,60,60,60,60,60,60,60,60,-100,-101,-102,-103,-104,-105,60,60,-114,-115,-116,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'float_constant':([18,19,20,27,28,29,41,44,56,58,59,65,69,71,74,92,93,94,104,106,114,116,120,121,122,123,124,125,126,128,130,131,132,133,136,150,153,155,168,174,176,180,194,196,197,205,235,251,265,287,318,],[61,61,61,61,61,61,61,61,61,-109,-110,61,61,61,61,61,61,61,61,61,61,61,61,-100,-101,-102,-103,-104,-105,61,61,-114,-115,-116,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'string_constant':([18,19,20,27,28,29,41,44,56,58,59,65,69,71,74,92,93,94,104,106,114,116,120,121,122,123,124,125,126,128,130,131,132,133,136,150,153,155,168,174,176,180,194,196,197,205,235,251,265,287,318,],[62,62,62,62,62,62,62,62,62,-109,-110,62,62,62,62,62,62,62,62,62,62,62,62,-100,-101,-102,-103,-104,-105,62,62,-114,-115,-116,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'null_constant':([18,19,20,27,28,29,41,44,56,58,59,65,69,71,74,92,93,94,104,106,114,116,120,121,122,123,124,125,126,128,130,131,132,133,136,150,153,155,168,174,176,180,194,196,197,205,235,251,265,287,318,],[63,63,63,63,63,63,63,63,63,-109,-110,63,63,63,63,63,63,63,63,63,63,63,63,-100,-101,-102,-103,-104,-105,63,63,-114,-115,-116,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'NEW':([28,94,197,251,287,318,],[81,81,81,81,81,81,]),'RPAREN':([29,53,54,55,57,60,61,62,63,64,78,79,80,82,83,84,92,119,127,129,134,135,137,138,141,142,150,152,154,155,159,168,183,185,187,188,189,190,192,195,199,206,209,220,226,228,237,238,239,244,253,254,273,276,279,280,281,284,285,294,298,301,302,303,304,306,307,311,315,320,323,328,],[-42,-99,-108,-113,-118,-119,-120,-121,-122,-126,-37,-38,-39,-126,151,-44,-42,-97,-106,-111,-117,-123,192,193,198,-14,-42,-41,-46,-42,213,-42,234,236,-14,-98,-107,-113,-124,-56,246,253,-43,259,264,266,272,-112,-126,-61,-40,-126,-125,-57,-16,-16,-16,-126,-44,-57,317,-11,-14,-12,-13,-96,-45,-57,325,-15,330,-60,]),'GT':([53,54,55,57,60,61,62,63,64,82,127,129,134,135,189,190,192,238,239,273,],[121,-108,-113,-118,-119,-120,-121,-122,-126,-126,-106,-111,-117,-123,-107,-113,-124,-112,-126,-125,]),'LT':([53,54,55,57,60,61,62,63,64,82,127,129,134,135,189,190,192,238,239,273,],[122,-108,-113,-118,-119,-120,-121,-122,-126,-126,-106,-111,-117,-123,-107,-113,-124,-112,-126,-125,]),'GE':([53,54,55,57,60,61,62,63,64,82,127,129,134,135,189,190,192,238,239,273,],[123,-108,-113,-118,-119,-120,-121,-122,-126,-126,-106,-111,-117,-123,-107,-113,-124,-112,-126,-125,]),'LE':([53,54,55,57,60,61,62,63,64,82,127,129,134,135,189,190,192,238,239,273,],[124,-108,-113,-118,-119,-120,-121,-122,-126,-126,-106,-111,-117,-123,-107,-113,-124,-112,-126,-125,]),'EQ':([53,54,55,57,60,61,62,63,64,82,127,129,134,135,189,190,192,238,239,273,],[125,-108,-113,-118,-119,-120,-121,-122,-126,-126,-106,-111,-117,-123,-107,-113,-124,-112,-126,-125,]),'NEQ':([53,54,55,57,60,61,62,63,64,82,127,129,134,135,189,190,192,238,239,273,],[126,-108,-113,-118,-119,-120,-121,-122,-126,-126,-106,-111,-117,-123,-107,-113,-124,-112,-126,-125,]),'RBRACKET':([54,55,57,60,61,62,63,64,76,90,127,129,134,135,143,160,189,190,191,192,208,231,238,239,243,252,273,],[-108,-113,-118,-119,-120,-121,-122,-126,144,158,-106,-111,-117,-123,203,214,-107,-113,239,-124,254,268,-112,-126,277,284,-125,]),'MULTIPLY':([55,57,60,61,62,63,64,82,134,135,190,192,239,273,],[131,-118,-119,-120,-121,-122,-126,-126,-117,-123,131,-124,-126,-125,]),'DIVIDE':([55,57,60,61,62,63,64,82,134,135,190,192,239,273,],[132,-118,-119,-120,-121,-122,-126,-126,-117,-123,132,-124,-126,-125,]),'REM':([55,57,60,61,62,63,64,82,134,135,190,192,239,273,],[133,-118,-119,-120,-121,-122,-126,-126,-117,-123,133,-124,-126,-125,]),'COMMA':([60,61,62,63,64,84,135,192,239,254,273,279,280,281,285,],[-119,-120,-121,-122,-126,155,-123,-124,-126,-126,-125,302,302,302,155,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement':([0,193,198,234,236,264,266,275,317,325,330,],[2,240,245,269,271,289,291,297,327,331,333,]),'funclist':([0,],[3,]),'printstat':([0,193,198,234,236,264,266,275,317,325,330,],[8,8,8,8,8,8,8,8,8,8,8,]),'readstat':([0,193,198,234,236,264,266,275,317,325,330,],[10,10,10,10,10,10,10,10,10,10,10,]),'returnstat':([0,193,198,234,236,264,266,275,317,325,330,],[11,11,11,11,11,11,11,11,11,11,11,]),'ifstat':([0,193,198,234,236,264,266,275,317,325,330,],[12,12,12,12,12,12,12,12,12,12,12,]),'forstat':([0,193,198,234,236,264,266,275,317,325,330,],[13,13,13,13,13,13,13,13,13,13,13,]),'whilestat':([0,193,198,234,236,264,266,275,317,325,330,],[14,14,14,14,14,14,14,14,14,14,14,]),'funcdef':([0,],[17,]),'statement1':([5,],[26,]),'statelist':([15,35,110,278,296,],[36,87,177,300,316,]),'funclist1':([17,326,],[50,332,]),'expression':([18,19,20,28,41,44,69,71,94,104,106,114,116,174,176,194,197,235,251,265,287,318,],[52,66,68,78,97,68,138,141,78,171,68,183,185,226,228,242,78,242,78,242,78,78,]),'numexpression':([18,19,20,27,28,41,44,65,69,71,74,93,94,104,106,114,116,120,136,153,174,176,180,194,196,197,205,235,251,265,287,318,],[53,53,53,76,53,53,53,137,53,53,143,160,53,53,53,53,53,188,191,208,53,53,231,53,243,53,252,53,53,53,53,53,]),'term':([18,19,20,27,28,41,44,65,69,71,74,93,94,104,106,114,116,120,128,136,153,174,176,180,194,196,197,205,235,251,265,287,318,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,189,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'unaryexpr':([18,19,20,27,28,41,44,65,69,71,74,93,94,104,106,114,116,120,128,130,136,153,174,176,180,194,196,197,205,235,251,265,287,318,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,190,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'addsub':([18,19,20,27,28,41,44,54,65,69,71,74,93,94,104,106,114,116,120,128,130,136,153,174,176,180,194,196,197,205,235,251,265,287,318,],[56,56,56,56,56,56,56,128,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'factor':([18,19,20,27,28,29,41,44,56,65,69,71,74,92,93,94,104,106,114,116,120,128,130,136,150,153,155,168,174,176,180,194,196,197,205,235,251,265,287,318,],[57,57,57,57,57,84,57,57,134,57,57,57,57,84,57,57,57,57,57,57,57,57,57,57,84,57,84,84,57,57,57,57,57,57,57,57,57,57,57,57,]),'returnstat1':([20,44,106,],[67,113,173,]),'statement2':([25,30,31,],[73,85,86,]),'atribstat1':([28,94,197,251,287,318,],[77,161,244,283,308,328,]),'allocexpression':([28,94,197,251,287,318,],[79,79,79,79,79,79,]),'funccall':([28,94,197,251,287,318,],[80,80,80,80,80,80,]),'paramlistcall':([29,92,150,155,168,],[83,159,206,209,220,]),'listdcl':([37,39,40,100,102,103,158,200,201,202,],[89,95,96,166,169,170,212,247,248,249,]),'statelist3':([38,101,],[91,167,]),'statelist1':([42,98,117,156,164,178,181,182,215,223,225,229,255,271,288,291,293,310,313,321,331,333,],[99,165,186,210,218,230,232,233,257,262,263,267,286,295,309,312,314,322,324,329,334,335,]),'expression1':([53,],[119,]),'compoperator':([53,],[120,]),'numexpression1':([54,],[127,]),'term1':([55,190,],[129,238,]),'multdiv':([55,190,],[130,130,]),'lvalue1':([64,82,144,203,214,239,254,268,277,284,],[135,135,204,250,256,273,285,292,299,306,]),'forstat1':([70,115,175,276,294,311,],[139,184,227,298,315,323,]),'types':([81,],[146,]),'paramlistcall2':([84,],[152,]),'paramlistcall1':([84,285,],[154,307,]),'statelist2':([112,157,162,163,172,219,221,222,],[179,211,216,217,224,258,260,261,]),'forstat3':([140,],[195,]),'paramlist':([142,187,302,],[199,237,320,]),'forstat2':([194,235,265,],[241,270,290,]),'ifstat1':([240,269,289,],[274,293,310,]),'paramlist1':([279,280,281,],[301,303,304,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement','program',1,'p_program_1','syntax.py',7),
  ('program -> funclist','program',1,'p_program_2','syntax.py',12),
  ('program -> <empty>','program',0,'p_program_3','syntax.py',17),
  ('funclist -> funcdef funclist1','funclist',2,'p_funclist','syntax.py',23),
  ('funclist1 -> DEF IDENT LPAREN paramlist RPAREN LBRACE statelist RBRACE funclist1','funclist1',9,'p_funclist1_1','syntax.py',28),
  ('funclist1 -> <empty>','funclist1',0,'p_funclist1_2','syntax.py',33),
  ('funcdef -> DEF IDENT LPAREN paramlist RPAREN LBRACE statelist RBRACE','funcdef',8,'p_funcdef','syntax.py',39),
  ('types -> INT','types',1,'p_types_1','syntax.py',44),
  ('types -> FLOAT','types',1,'p_types_2','syntax.py',49),
  ('types -> STRING','types',1,'p_types_3','syntax.py',54),
  ('paramlist -> STRING listdcl IDENT paramlist1','paramlist',4,'p_paramlist_1','syntax.py',59),
  ('paramlist -> FLOAT listdcl IDENT paramlist1','paramlist',4,'p_paramlist_2','syntax.py',64),
  ('paramlist -> INT listdcl IDENT paramlist1','paramlist',4,'p_paramlist_3','syntax.py',69),
  ('paramlist -> <empty>','paramlist',0,'p_paramlist_4','syntax.py',74),
  ('paramlist1 -> COMMA paramlist','paramlist1',2,'p_paramlist1_1','syntax.py',80),
  ('paramlist1 -> <empty>','paramlist1',0,'p_paramlist1_2','syntax.py',85),
  ('listdcl -> LBRACKET RBRACKET listdcl','listdcl',3,'p_listdcl_1','syntax.py',91),
  ('listdcl -> <empty>','listdcl',0,'p_listdcl_2','syntax.py',96),
  ('statement -> INT IDENT statement2','statement',3,'p_statement_1_1','syntax.py',107),
  ('statement -> FLOAT IDENT statement2','statement',3,'p_statement_1_2','syntax.py',112),
  ('statement -> STRING IDENT statement2','statement',3,'p_statement_1_3','syntax.py',117),
  ('statement -> IDENT statement1','statement',2,'p_statement_2','syntax.py',122),
  ('statement -> printstat SEMICOLON','statement',2,'p_statement_3','syntax.py',127),
  ('statement -> readstat SEMICOLON','statement',2,'p_statement_4','syntax.py',132),
  ('statement -> returnstat SEMICOLON','statement',2,'p_statement_5','syntax.py',137),
  ('statement -> ifstat','statement',1,'p_statement_6','syntax.py',142),
  ('statement -> forstat','statement',1,'p_statement_7','syntax.py',147),
  ('statement -> whilestat','statement',1,'p_statement_8','syntax.py',152),
  ('statement -> LBRACE statelist RBRACE','statement',3,'p_statement_9','syntax.py',157),
  ('statement -> BREAK SEMICOLON','statement',2,'p_statement_10','syntax.py',162),
  ('statement -> SEMICOLON','statement',1,'p_statement_11','syntax.py',167),
  ('statement1 -> LBRACKET numexpression RBRACKET lvalue1 ASSIGN atribstat1 SEMICOLON','statement1',7,'p_statement1_1','syntax.py',172),
  ('statement1 -> ASSIGN atribstat1 SEMICOLON','statement1',3,'p_statement1_2','syntax.py',177),
  ('statement1 -> LPAREN paramlistcall RPAREN SEMICOLON','statement1',4,'p_statement1_3','syntax.py',182),
  ('statement2 -> LBRACKET numexpression RBRACKET lvalue1 SEMICOLON','statement2',5,'p_statement2_1','syntax.py',187),
  ('statement2 -> SEMICOLON','statement2',1,'p_statement2_2','syntax.py',192),
  ('atribstat1 -> expression','atribstat1',1,'p_atribstat1_1','syntax.py',197),
  ('atribstat1 -> allocexpression','atribstat1',1,'p_atribstat1_2','syntax.py',202),
  ('atribstat1 -> funccall','atribstat1',1,'p_atribstat1_3','syntax.py',207),
  ('funccall -> IDENT LPAREN paramlistcall RPAREN','funccall',4,'p_funccall','syntax.py',212),
  ('paramlistcall -> factor paramlistcall2','paramlistcall',2,'p_paramlistcall_1','syntax.py',217),
  ('paramlistcall -> <empty>','paramlistcall',0,'p_paramlistcall_2','syntax.py',222),
  ('paramlistcall1 -> COMMA paramlistcall','paramlistcall1',2,'p_paramlistcall1_1','syntax.py',228),
  ('paramlistcall1 -> <empty>','paramlistcall1',0,'p_paramlistcall1_2','syntax.py',233),
  ('paramlistcall2 -> LBRACKET numexpression RBRACKET lvalue1 paramlistcall1','paramlistcall2',5,'p_paramlistcall2_1','syntax.py',239),
  ('paramlistcall2 -> paramlistcall1','paramlistcall2',1,'p_paramlistcall2_2','syntax.py',244),
  ('printstat -> PRINT expression','printstat',2,'p_printstat','syntax.py',250),
  ('readstat -> READ expression','readstat',2,'p_readstat','syntax.py',255),
  ('returnstat -> RETURN returnstat1','returnstat',2,'p_returnstat','syntax.py',260),
  ('returnstat1 -> expression','returnstat1',1,'p_returnstat1_2','syntax.py',265),
  ('returnstat1 -> <empty>','returnstat1',0,'p_returnstat1_3','syntax.py',270),
  ('ifstat -> IF LPAREN expression RPAREN statement ifstat1','ifstat',6,'p_ifstat','syntax.py',276),
  ('ifstat1 -> ELSE statement','ifstat1',2,'p_ifstat1_1','syntax.py',281),
  ('ifstat1 -> <empty>','ifstat1',0,'p_ifstat1_2','syntax.py',286),
  ('forstat -> FOR LPAREN forstat1 SEMICOLON forstat2 SEMICOLON forstat1 RPAREN statement','forstat',9,'p_forstat','syntax.py',292),
  ('forstat1 -> IDENT forstat3','forstat1',2,'p_forstat1_1','syntax.py',297),
  ('forstat1 -> <empty>','forstat1',0,'p_forstat1_2','syntax.py',302),
  ('forstat2 -> expression','forstat2',1,'p_forstat2_1','syntax.py',308),
  ('forstat2 -> <empty>','forstat2',0,'p_forstat2_2','syntax.py',313),
  ('forstat3 -> LBRACKET numexpression RBRACKET lvalue1 ASSIGN atribstat1','forstat3',6,'p_forstat3_1','syntax.py',319),
  ('forstat3 -> ASSIGN atribstat1','forstat3',2,'p_forstat3_2','syntax.py',324),
  ('whilestat -> WHILE LPAREN expression RPAREN statement','whilestat',5,'p_whilestat','syntax.py',329),
  ('statelist -> INT listdcl IDENT statelist2','statelist',4,'p_statelist_1','syntax.py',334),
  ('statelist -> FLOAT listdcl IDENT statelist2','statelist',4,'p_statelist_2','syntax.py',339),
  ('statelist -> STRING listdcl IDENT statelist2','statelist',4,'p_statelist_3','syntax.py',344),
  ('statelist -> IDENT statelist3','statelist',2,'p_statelist_4','syntax.py',349),
  ('statelist -> PRINT expression SEMICOLON statelist1','statelist',4,'p_statelist_5','syntax.py',354),
  ('statelist -> READ IDENT statelist2','statelist',3,'p_statelist_6','syntax.py',359),
  ('statelist -> RETURN returnstat1 SEMICOLON statelist1','statelist',4,'p_statelist_7','syntax.py',364),
  ('statelist -> IF LPAREN expression RPAREN statement ifstat1 statelist1','statelist',7,'p_statelist_8','syntax.py',369),
  ('statelist -> FOR LPAREN forstat1 SEMICOLON forstat2 SEMICOLON forstat1 RPAREN statement statelist1','statelist',10,'p_statelist_9','syntax.py',374),
  ('statelist -> WHILE LPAREN expression RPAREN statement statelist1','statelist',6,'p_statelist_10','syntax.py',379),
  ('statelist -> LBRACE statelist RBRACE statelist1','statelist',4,'p_statelist_11','syntax.py',384),
  ('statelist -> BREAK SEMICOLON statelist1','statelist',3,'p_statelist_12','syntax.py',389),
  ('statelist -> SEMICOLON statelist1','statelist',2,'p_statelist_13','syntax.py',394),
  ('statelist -> IDENT LPAREN paramlistcall RPAREN SEMICOLON statelist1','statelist',6,'p_statelist_14','syntax.py',399),
  ('statelist1 -> INT listdcl IDENT statelist2','statelist1',4,'p_statelist1_1','syntax.py',404),
  ('statelist1 -> FLOAT listdcl IDENT statelist2','statelist1',4,'p_statelist1_2','syntax.py',409),
  ('statelist1 -> STRING listdcl IDENT statelist2','statelist1',4,'p_statelist1_3','syntax.py',414),
  ('statelist1 -> IDENT statelist3','statelist1',2,'p_statelist1_4','syntax.py',419),
  ('statelist1 -> PRINT expression SEMICOLON statelist1','statelist1',4,'p_statelist1_5','syntax.py',424),
  ('statelist1 -> READ IDENT statelist2','statelist1',3,'p_statelist1_6','syntax.py',429),
  ('statelist1 -> RETURN returnstat1 SEMICOLON statelist1','statelist1',4,'p_statelist1_7','syntax.py',434),
  ('statelist1 -> IF LPAREN expression RPAREN statement ifstat1 statelist1','statelist1',7,'p_statelist1_8','syntax.py',439),
  ('statelist1 -> FOR LPAREN forstat1 SEMICOLON forstat2 SEMICOLON forstat1 RPAREN statement statelist1','statelist1',10,'p_statelist1_9','syntax.py',444),
  ('statelist1 -> WHILE LPAREN expression RPAREN statement statelist1','statelist1',6,'p_statelist1_10','syntax.py',449),
  ('statelist1 -> LBRACE statelist RBRACE statelist1','statelist1',4,'p_statelist1_11','syntax.py',454),
  ('statelist1 -> BREAK SEMICOLON statelist1','statelist1',3,'p_statelist1_12','syntax.py',459),
  ('statelist1 -> SEMICOLON statelist1','statelist1',2,'p_statelist1_13','syntax.py',464),
  ('statelist1 -> IDENT LPAREN paramlistcall RPAREN SEMICOLON statelist1','statelist1',6,'p_statelist1_14','syntax.py',469),
  ('statelist1 -> <empty>','statelist1',0,'p_statelist1_15','syntax.py',474),
  ('statelist2 -> LBRACKET numexpression RBRACKET lvalue1 SEMICOLON statelist1','statelist2',6,'p_statelist2_1','syntax.py',480),
  ('statelist2 -> SEMICOLON statelist1','statelist2',2,'p_statelist2_2','syntax.py',485),
  ('statelist3 -> LBRACKET numexpression RBRACKET lvalue1 ASSIGN atribstat1 SEMICOLON statelist1','statelist3',8,'p_statelist3_1','syntax.py',490),
  ('statelist3 -> ASSIGN atribstat1 SEMICOLON statelist1','statelist3',4,'p_statelist3_2','syntax.py',495),
  ('allocexpression -> NEW types LBRACKET numexpression RBRACKET lvalue1','allocexpression',6,'p_allocexpression','syntax.py',500),
  ('expression -> numexpression expression1','expression',2,'p_expression','syntax.py',505),
  ('expression1 -> compoperator numexpression','expression1',2,'p_expression1_1','syntax.py',510),
  ('expression1 -> <empty>','expression1',0,'p_expression1_2','syntax.py',515),
  ('compoperator -> GT','compoperator',1,'p_compoperator_1','syntax.py',521),
  ('compoperator -> LT','compoperator',1,'p_compoperator_2','syntax.py',526),
  ('compoperator -> GE','compoperator',1,'p_compoperator_3','syntax.py',531),
  ('compoperator -> LE','compoperator',1,'p_compoperator_4','syntax.py',536),
  ('compoperator -> EQ','compoperator',1,'p_compoperator_5','syntax.py',541),
  ('compoperator -> NEQ','compoperator',1,'p_compoperator_6','syntax.py',546),
  ('numexpression -> term numexpression1','numexpression',2,'p_numexpression','syntax.py',551),
  ('numexpression1 -> addsub term','numexpression1',2,'p_numexpression1_1','syntax.py',556),
  ('numexpression1 -> <empty>','numexpression1',0,'p_numexpression1_2','syntax.py',561),
  ('addsub -> PLUS','addsub',1,'p_addsub_1','syntax.py',567),
  ('addsub -> MINUS','addsub',1,'p_addsub_2','syntax.py',572),
  ('term -> unaryexpr term1','term',2,'p_term','syntax.py',577),
  ('term1 -> multdiv unaryexpr term1','term1',3,'p_term1_1','syntax.py',582),
  ('term1 -> <empty>','term1',0,'p_term1_2','syntax.py',587),
  ('multdiv -> MULTIPLY','multdiv',1,'p_multdiv_1','syntax.py',593),
  ('multdiv -> DIVIDE','multdiv',1,'p_multdiv_2','syntax.py',598),
  ('multdiv -> REM','multdiv',1,'p_multdiv_3','syntax.py',603),
  ('unaryexpr -> addsub factor','unaryexpr',2,'p_unaryexpr_1','syntax.py',608),
  ('unaryexpr -> factor','unaryexpr',1,'p_unaryexpr_2','syntax.py',613),
  ('factor -> int_constant','factor',1,'p_factor_1','syntax.py',618),
  ('factor -> float_constant','factor',1,'p_factor_2','syntax.py',623),
  ('factor -> string_constant','factor',1,'p_factor_3','syntax.py',628),
  ('factor -> null_constant','factor',1,'p_factor_4','syntax.py',633),
  ('factor -> IDENT lvalue1','factor',2,'p_factor_5','syntax.py',638),
  ('factor -> LPAREN numexpression RPAREN','factor',3,'p_factor_6','syntax.py',643),
  ('lvalue1 -> LBRACKET numexpression RBRACKET lvalue1','lvalue1',4,'p_lvalue1_1','syntax.py',649),
  ('lvalue1 -> <empty>','lvalue1',0,'p_lvalue1_2','syntax.py',654),
]
