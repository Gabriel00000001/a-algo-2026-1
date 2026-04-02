'''     
Algorimto Merge sort
T(n) = 2T(n/2) + n

*(2*T(n/2)): Representa as duas chamadas recursivas,onde é divido ao meio.
*(n): Representa a etapa de intercalação, onde precisar caminhar cada elemento para ordenar.

Árvore de recorrência

          (n)
    (n/2)     (n/2)
(n/4)  (n/4) (n/4)  (n/4)
....
(1)

*A árvore vai dividindo por 2 a cada altura para chegar até o caso base(1).
*Para saber quantos passos precisa para chegar a 1 seria n/2^h.
*Como o h representa a altura da árvore e quantas vezes foi dividido para ficar 1 então usa logarítmo para isolar o "h"
*h = log2(n).
*Como tem o esforço de juntar as partes, o "n" representaria essa etapa.
*Então o cálculo final é T(n) = O(nlog2(n)).


Multiplicação de matrizes
 *Como o algoritmo tem três laços "for" aninhados  que cada um repete n vezes, a complexidade
 seria a multiplicação dos n (n x n x n).
 *O cálculo final: T(n) = O(n^3).


Funções Recursivas(Teorema Mestre)

T(n) = 2T(n/4) + √n
*Parâmetros: a = 2; b = 4 .
*F(n) = √n.
*Valor crítico: n^log4(2) = n^1/2 = √n.
*Como o valor crítico é igual à F(n), vai para o caso 2. O cálculo final é O(√nlog(n)).


T(n) = 2T(n/4) + n
*Parâmetro: a = 2; b = 4.
*F(n) = n.
*Valor crítico: n^log4(2) = n^1/2 = √n.
*Como o valor crítico é diferente de F(n), vai para o caso 3. O cálculo final é O(n).


T(n) = 16T(n/4) + n^2 
*Parâmetro: a = 16; b = 4.
*F(n) = n^2.
*Valor crítico: n^log4(16) = n^2.
*Como o valor crítico é igual à F(n), vai para o caso 2. O cálculo final é O(n^2log(n)).
 

'''