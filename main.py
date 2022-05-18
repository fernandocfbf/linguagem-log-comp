from src.classes.Lexer import Lexer

text_input = "saaa"

lexer = Lexer().getLexer()
tokens = lexer.lex(text_input)
print(tokens)
for token in tokens:
    print(token)