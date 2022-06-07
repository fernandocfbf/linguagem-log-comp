
%{
#include <stdio.h>
int yylex();
int yyerror(char *s);
%}

%token IDENTIFIER INTEGER 
%token EQUAL CEQ CLT CGT LPAREN RPAREN LBRACE RBRACE COMMA SEMICOLON
%token PLUS MINUS MUL DIV NOT OR AND
%token PRINTF SCANF WHILE IF ELSE DEF RETURN

%start program

%%

program: block ;

block: 
    LBRACE statement RBRACE;

statement: 
    assigment SEMICOLON |
    print SEMICOLON     |
    block               |
    while               |
    if                  |
    SEMICOLON;

assigment: 
    IDENTIFIER EQUAL relexpression;

print: 
    PRINTF LPAREN relexpression RPAREN;

while: 
    WHILE LPAREN relexpression RPAREN statement;

if: 
    IF LPAREN relexpression RPAREN statement else;

else: 
    ELSE statement |
    ;

relexpression: 
    expression CEQ expression |
    expression CGT expression |
    expression CLT expression |
    ;

expression: 
    term PLUS term |
    term MINUS term |
    term OR term |
    term;

term: 
    factor      |
    factor MUL factor  |
    factor DIV factor  |
    factor AND factor |
    ;

factor: 
    PLUS factor                 |
    MINUS factor                |
    NOT factor                  |
    INTEGER                     |
    IDENTIFIER                  |
    LPAREN relexpression RPAREN |
    SCANF LPAREN RPAREN;

%%


int yyerror(char *s)
{
	printf("Syntax Error on line %s\n", s);
	return 0;
}

int main()
{
    yyparse();
    return 0;
}