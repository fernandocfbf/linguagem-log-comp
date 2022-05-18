#reference: https://rply.readthedocs.io/en/latest/users-guide/lexers.html

from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()
    
    def addTokens(self):
        #structure
        self.lexer.add('OPEN_KEY', r'\awww')
        self.lexer.add('CLOSE_KEY', r'\wwwa')
        self.lexer.add('SEMI_COLON', r'\wwaa')
        self.lexer.add('OPEN_PAR', r'\awaw')
        self.lexer.add('CLOSE_PAR', r'\wawa')
        self.lexer.add('COMMA', r'\aaww')

        #operators
        self.lexer.add('EQUAL', r'\dddd')
        self.lexer.add('EQUAL_EQUAL', r'\ddda')
        self.lexer.add('GREATER_THAN', r'\ddad')
        self.lexer.add('LESS_THAN', r'\dadd')
        self.lexer.add('PLUS', r'\addd')
        self.lexer.add('MINUS', r'\aadd')
        self.lexer.add('TIMES', r'\daad')
        self.lexer.add('DIVIDE', r'\ddaa')
        self.lexer.add('OR', r'\adda')
        self.lexer.add('AND', r'\adad')
        self.lexer.add('NOT', r'\dada')

        #reserved
        self.lexer.add('WHILE', r'\aaas')
        self.lexer.add('IF', r'\aasa')
        self.lexer.add('ELSE', r'\asaa')
        self.lexer.add('PRINTF', r'\saaa')
        self.lexer.add('SCANF', r'\aaaa')
        self.lexer.add('DEF', r'\aass')
        self.lexer.add('RETURN', r'\saas')

        #ignore
        self.lexer.ignore('\s+')

    def getLexer(self):
        self.addTokens()
        return self.lexer.build()