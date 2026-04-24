def recursao(n): # função recursão 

    #caso base
    if n == 1:
        return 2
    
    #função recursiva
    return (2 * recursao(n - 1)) + n**2

#validador da entrada do usuário
while True:
    try: 
        numero = int(input("digite um número maior que 0: "))

        if numero <= 0:
            print("diga somente número maior que 0")
        else:
            break

    except ValueError:
        print("informe somente números")

#imprime o resultado para o usuário
resultado = recursao(numero)
print(f"O resultado da recursao: {resultado}")