%{
#include <stdio.h>
#include <string.h>
#include "bison.tab.h"
%}

%%

[ \t\n]                 
[w | a | s | d][w | a | s | d | 0-9]    return IDENTIFIER;
[0-9]+                                  return INTEGER;
"dddd"                                  return EQUAL;
"ddda"                                  return CEQ;
"dadd"                                  return CLT;
"ddad"                                  return CGT;
"awaw"                                  return LPAREN;
"wawa"                                  return RPAREN;
"awww"                                  return LBRACE;
"wwwa"                                  return RBRACE;
"aaww"                                  return COMMA;
"addd"                                  return PLUS;
"aadd"                                  return MINUS;
"daad"                                  return MUL;
"ddaa"                                  return DIV;
"wwaa"                                  return SEMICOLON;
"dada"                                  return NOT;
"adda"                                  return OR;
"adad"                                  return AND;
"saaa"                                  return PRINTF;
"aaaa"                                  return SCANF;
"aaas"                                  return WHILE;
"aasa"                                  return IF;
"asaa"                                  return ELSE;
"aass"                                  return DEF;
"saas"                                  return RETURN;
.                                       printf("Unknown !n"); yyterminate();

%%