from src.constants.reserved import RESERVED_WORDS
from src.constants.tokens import ALL_TOKENS_TRANSLATED, IGNORE_TOKEN, POSSIBLE_DUAL_TOKENS_TRANSLATED
from src.constants.types import TYPES
from src.constants.valid_chars import VALID_CHARS
from src.classes.Token import Token

class Tokenizer:
    def __init__(self, origin, position, actual):
        self.origin = origin #input (string) 
        self.position = position #current position (int)
        self.actual = actual #current token (Token)

    def selectNext(self):
        '''
        input: empty
        output: Token type object (self.actual)
        description: read the next token from the input and update the actual and position atributes
        '''
        if self.position >= len(self.origin):
            self.actual = Token("EOF", "")
            return self.actual

        if self.origin[self.position] in IGNORE_TOKEN:
            self.position += 1
            if (self.position < len(self.origin)):
                while (self.origin[self.position] in IGNORE_TOKEN):
                    self.position += 1
                    if self.position >= len(self.origin):
                        break
                if (self.position < len(self.origin)): # is necessary to check again in case of space at the end of the expression
                    if (self.origin[self.position].isnumeric() and self.actual.type == "number"):
                        raise Exception("Invalid syntax")
            if (self.position >= len(self.origin)):  # if the expression ended, return EOF
                self.actual = Token("EOF", "")
                return self.actual
        
        current_token = self.origin[self.position]     
        
        if current_token == '"':
            self.position += 1
            candidate = ""
            while self.origin[self.position] != '"':
                candidate += self.origin[self.position]
                self.position += 1
            self.position += 1
            self.actual = Token("string", candidate)

        elif current_token.isnumeric():
            number = current_token
            self.position += 1
            if (self.position < len(self.origin)):
                while (self.origin[self.position].isnumeric()):
                    number += self.origin[self.position]
                    self.position += 1
                    if self.position >= len(self.origin):
                        break
            self.actual = Token("number", number)

        elif current_token in VALID_CHARS:
            variable = current_token
            self.position += 1
            if (self.position < len(self.origin)):
                while (self.origin[self.position] in VALID_CHARS):
                    variable += self.origin[self.position]
                    self.position += 1
                    if self.position >= len(self.origin):
                        break
            if variable in RESERVED_WORDS.keys():
                self.actual = Token("reserved", RESERVED_WORDS[variable])
            elif variable in TYPES.keys():
                self.actual = Token("type", TYPES[variable])
            elif variable in ALL_TOKENS_TRANSLATED:
                self.position += 1
                self.actual = Token(ALL_TOKENS_TRANSLATED[variable], "")
            else:
                self.actual = Token("identifier", variable)
        
        else:
            raise Exception("Character didn't recognize")
        return self.actual

 