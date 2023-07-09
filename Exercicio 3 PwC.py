#Exercicio 3
#Lógica usada: Para verificar os SubPalindromos de uma palavra, eles devem ser um subconjunto da palavra original e ser um Palindromo
#Pensei em percorrer os elementos da palavra formando subconjuntos cada vez maiores e verificando se são palindromos
#Caso fossem, também deveria verificar qual fosse o maior deles, então criei uma variável pra guardar somente o maior palindromo que encontrasse

def subPalindromo(palavra):
    #Cria uma variável para armazenar e comparar palindromos conforme são descobertos
    maiorpal = ''       
    
    #Cria uma iteração para percorrer da primeira à ultima letra da palavra e outra iteração para comparar essa letra com todas as posteriores progressivamente
    for i in range(len(palavra)):             
        for j in range(i+1,len(palavra)+1):  
            #Cria uma variável temporária para verificar se as letras contidas formam um palindromo
            temp = palavra[i:j]                
            if temp == temp[::-1]:   
                #Caso seja um palindromo maior que o já armazenado, apaga o anterior e armazena o novo
                if len(temp)>len(maiorpal):    
                    maiorpal = temp       
    #Devolve o palindromo armazenado
    print(maiorpal)

#Teste da função
palavra = input()
subPalindromo(palavra)
