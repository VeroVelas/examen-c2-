
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'FOR ID IGUAL IMPRIMIR INCREMENTO INT LLAVEDER LLAVEIZQ MENORIGUAL NUMERO PARENDER PARENIZQ PUNTOYCOMAprograma : lista_declaracioneslista_declaraciones : lista_declaraciones declaracion\n                           | declaraciondeclaracion : declaracion_variable\n                   | sentenciadeclaracion_variable : INT ID PUNTOYCOMAsentencia : sentencia_for\n                 | sentencia_imprimir\n                 | sentencia_expresionsentencia_for : FOR PARENIZQ inicializacion PUNTOYCOMA condicion PUNTOYCOMA incremento PARENDER LLAVEIZQ lista_sentencias LLAVEDERinicializacion : ID IGUAL NUMEROcondicion : ID MENORIGUAL NUMEROincremento : ID INCREMENTOlista_sentencias : lista_sentencias sentencia\n                        | sentenciasentencia_imprimir : IMPRIMIR PARENIZQ expresion PARENDER PUNTOYCOMAsentencia_expresion : expresion PUNTOYCOMAexpresion : ID'
    
_lr_action_items = {'INT':([0,2,3,4,5,8,9,10,14,18,19,29,40,],[6,6,-3,-4,-5,-7,-8,-9,-2,-17,-6,-16,-10,]),'FOR':([0,2,3,4,5,8,9,10,14,18,19,29,37,38,39,40,41,],[11,11,-3,-4,-5,-7,-8,-9,-2,-17,-6,-16,11,11,-15,-10,-14,]),'IMPRIMIR':([0,2,3,4,5,8,9,10,14,18,19,29,37,38,39,40,41,],[12,12,-3,-4,-5,-7,-8,-9,-2,-17,-6,-16,12,12,-15,-10,-14,]),'ID':([0,2,3,4,5,6,8,9,10,14,16,17,18,19,23,29,30,37,38,39,40,41,],[7,7,-3,-4,-5,15,-7,-8,-9,-2,21,7,-17,-6,27,-16,33,7,7,-15,-10,-14,]),'$end':([1,2,3,4,5,8,9,10,14,18,19,29,40,],[0,-1,-3,-4,-5,-7,-8,-9,-2,-17,-6,-16,-10,]),'PUNTOYCOMA':([7,13,15,20,25,26,28,34,],[-18,18,19,23,29,30,-11,-12,]),'PARENDER':([7,22,32,36,],[-18,25,35,-13,]),'LLAVEDER':([8,9,10,18,29,38,39,40,41,],[-7,-8,-9,-17,-16,40,-15,-10,-14,]),'PARENIZQ':([11,12,],[16,17,]),'IGUAL':([21,],[24,]),'NUMERO':([24,31,],[28,34,]),'MENORIGUAL':([27,],[31,]),'INCREMENTO':([33,],[36,]),'LLAVEIZQ':([35,],[37,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'lista_declaraciones':([0,],[2,]),'declaracion':([0,2,],[3,14,]),'declaracion_variable':([0,2,],[4,4,]),'sentencia':([0,2,37,38,],[5,5,39,41,]),'sentencia_for':([0,2,37,38,],[8,8,8,8,]),'sentencia_imprimir':([0,2,37,38,],[9,9,9,9,]),'sentencia_expresion':([0,2,37,38,],[10,10,10,10,]),'expresion':([0,2,17,37,38,],[13,13,22,13,13,]),'inicializacion':([16,],[20,]),'condicion':([23,],[26,]),'incremento':([30,],[32,]),'lista_sentencias':([37,],[38,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> lista_declaraciones','programa',1,'p_programa','app.py',61),
  ('lista_declaraciones -> lista_declaraciones declaracion','lista_declaraciones',2,'p_lista_declaraciones','app.py',65),
  ('lista_declaraciones -> declaracion','lista_declaraciones',1,'p_lista_declaraciones','app.py',66),
  ('declaracion -> declaracion_variable','declaracion',1,'p_declaracion','app.py',73),
  ('declaracion -> sentencia','declaracion',1,'p_declaracion','app.py',74),
  ('declaracion_variable -> INT ID PUNTOYCOMA','declaracion_variable',3,'p_declaracion_variable','app.py',78),
  ('sentencia -> sentencia_for','sentencia',1,'p_sentencia','app.py',86),
  ('sentencia -> sentencia_imprimir','sentencia',1,'p_sentencia','app.py',87),
  ('sentencia -> sentencia_expresion','sentencia',1,'p_sentencia','app.py',88),
  ('sentencia_for -> FOR PARENIZQ inicializacion PUNTOYCOMA condicion PUNTOYCOMA incremento PARENDER LLAVEIZQ lista_sentencias LLAVEDER','sentencia_for',11,'p_sentencia_for','app.py',92),
  ('inicializacion -> ID IGUAL NUMERO','inicializacion',3,'p_inicializacion','app.py',98),
  ('condicion -> ID MENORIGUAL NUMERO','condicion',3,'p_condicion','app.py',102),
  ('incremento -> ID INCREMENTO','incremento',2,'p_incremento','app.py',106),
  ('lista_sentencias -> lista_sentencias sentencia','lista_sentencias',2,'p_lista_sentencias','app.py',110),
  ('lista_sentencias -> sentencia','lista_sentencias',1,'p_lista_sentencias','app.py',111),
  ('sentencia_imprimir -> IMPRIMIR PARENIZQ expresion PARENDER PUNTOYCOMA','sentencia_imprimir',5,'p_sentencia_imprimir','app.py',118),
  ('sentencia_expresion -> expresion PUNTOYCOMA','sentencia_expresion',2,'p_sentencia_expresion','app.py',122),
  ('expresion -> ID','expresion',1,'p_expresion','app.py',126),
]
