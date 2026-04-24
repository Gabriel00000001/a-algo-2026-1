def palindromo(n):

    # caso base
    if len(n) <= 1:
        return True

    # se primeiro e último forem diferentes
    if n[0] != n[-1]:
        return False
    
    # chamada recursiva com a parte do meio
    return palindromo(n[1:-1])



if palindromo("radar"):
    print("é um palindromo")
else:
    print("Não é um palindromo")




   
    
    
