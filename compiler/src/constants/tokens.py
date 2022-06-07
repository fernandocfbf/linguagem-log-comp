EXPRESSION_TOKENS = {
    "addd": "+", #+
    "aadd": "-",    #-
    "adda": "||",  #||
    #".": ".",    #.
}

TERM_TOKENS = {
    "daad": "*",   #*
    "ddaa": "/",   #/
    "adad": "&&"  #&&
}

RELEXPRESSION_TOKENS = {
    "ddda": "==", #==
    "ddad": ">",   #>
    "dadd": "<",   #<
}

ALL_TOKENS ={
    "addd": "+",  #+
    "aadd": "-",  #-
    "daad": "*",  #*
    "ddaa": "/",  #/
    " ": " ",  #" "
    "awaw": "(",  #(
    "wawa": ")",  #)
    "awww": "{",  #{
    "wwwa": "}",  #}
    "wwaa": ";",  #;
    "dddd": "=",  #=
    "ddda": "==", #==
    "ddad": ">",  #>
    "dadd": "<",  #<
    "adad": "&&", #&&
    "adda": "||", #||
    "dada": "!",  #!
    #".": ".",  #.
    "aaww": ","   #,
}

POSSIBLE_DUAL_TOKENS = {
    "=": "=", #=
    "|": "|", #|
    "&": "&", #&
}

IGNORE_TOKEN = [" ", "\n"]