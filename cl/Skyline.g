grammar Skyline;

root: (operacions);

operacions
    : '(' operacions ')'                # parenthesis
    | SUB operacions                    # mirall
    | operacions (PLUS|MUL) operacions  # unioInter
    | operacions MUL INT                # replicacio
    | operacions (PLUS|SUB) INT         # desplaçament
    | ID ASSIG operacions               # assignacio
    | sky                               # ident
    ;

sky : ID | creacions
    ;

creacions
    : simple
    | compost
    | aleatori
    ;

simple  : '(' INT ',' INT ',' INT ')'   //(xmin, alçada, xmax)
    ;

compost : '[' '(' INT ',' INT ',' INT ')' (',' '(' INT ',' INT ',' INT ')')* ']'    //[(xmin, alçada, xmax), ...]
    ;

aleatori: '{' INT ',' INT ',' INT ',' INT ',' INT '}'   //{n, h, w, xmin, xmax}
    ;

ASSIG : ':=';

ID : [a-zA-Z][a-zA-Z0-9]*;

MUL : '*';
SUB : '-' ;
PLUS : '+' ;

INT : [0-9]+ ;
WS : [ \t\r\n\f]+ -> skip;