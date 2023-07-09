#Exercicio 3
def subPalindromo(palavra):
    maiorpal = ''                              #Cria uma variável para armazenar e comparar palindromos conforme são descobertos
    for i in range(len(palavra)):              #Cria uma iteração da primeira à ultima letra da palavra
        for j in range(i+1,len(palavra)+1):    #Cria outra iteração que parte da letra imediatamente depois daquela selecionada na iteração anterior até a ultima letra da palavra
            temp = palavra[i:j]                #Cria uma variável temporária baseada nas iterações anteriores e assim percorrer todos os subconjuntos da palavra dada
            if temp == temp[::-1]:             #Compara a palavra com ela mesma ao contrário
                if len(temp)>len(maiorpal):    #Caso seja um palindromo maior que o já armazenado, armazena o maior
                    maiorpal = temp          
    print(maiorpal)
#palavra = input()
#subPalindromo(palavra)
