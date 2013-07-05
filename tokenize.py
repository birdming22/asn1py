import automata

def generate_tokens(lines):
    token_list = []
    lnum = 0

    endDFA = automata.DFA([], [])
   
    line = ''
    for line in lines:
        print line
        lnum = lnum + 1
        endmatch = endDFA.recognize(line)
        print endmatch

