
%{
#include <stdio.h>
int yylex();
int yyerror(char *s);
%}

%token IDENTIFIER INTEGER 
%token EQUAL CEQ CLT CGT LPAREN RPAREN LBRACE RBRACE COMMA SEMICOLON
%token PLUS MINUS MUL DIV NOT OR AND
%token PRINT SCANF WHILE IF ELSE DEF RETURN



%start program

%%

program: block ;

block: LBRACE statement RBRACE;

statement: assigment SEMICOLON | print SEMICOLON |  SEMICOLON | block | while | if;

assigment: IDENTIFIER EQUAL relexpression;

print: PRINTF LPAREN relexpression RPAREN;

while: WHILE LPAREN relexpression RPAREN statement;

if: IF LPAREN relexpression RPAREN statement else;

else: ELSE statement |  ;

relexpression: term relexpression_part2;

relexpression_part2: CEQ expression | CGT expression | CLT expression | ;

expression: term expression_part2;

expression_part2: PLUS term | MINUS term | OR term | ;

term: factor term_part2;

term_part2: MUL factor | DIV factor | AND  factor | ;

factor: PLUS factor | MINUS factor | NOT factor | INTEGER | IDENTIFIER | LPAREN relexpression RPAREN | SCANF LPAREN RPAREN;

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