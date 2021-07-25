# Sonia da Trindade
# 24 07 21


# This is an interpreter.
# This is the main file of this program.


# Tokenizer
# Parser
# Evaluator
# Node class
# Test files


def main():

    expression = input(">>> ")
    #print(expression)

    tokens = tokenize(expression)

    parse(tokens)
    

main()
