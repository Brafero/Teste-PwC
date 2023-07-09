#Exercicio 4
#Lógica usada: Em um parágrafo, a primeira palavra e todas as que sucedem ".", "!" ou "?" devem ter a primeira letra maiúscula.
#Com isso, pensei em verificar se o último caracter de cada palavra é uma pontuação, o que implicaria que a próxima palavra
#deve ter a primeira letra maiúscula. 


def primeira_maiuscula(frase):
  #Divide a frase em uma lista pra analisar mais facilmente cada palavra
  temp = frase.split()       
  
  #Cria uma variável de comparação para saber quando deve ser maísuscula
  check = 1       

  #Pra cada uma das palavras na lista, verifica se a variável de comparação indica que deve ser maiúscula e imprime a palavra de acordo, 
  #ajustando a variável caso utilizada
  for i in temp:                                     
    if check == 1:                                   
      print(i.capitalize(), end=' ')                 
      check = 0                                      
    else:                                         
      print(i, end=' ')      

    #Verifica se o ultimo caracter é pontuação e ajusta a variável caso seja
    if i[-1] == '.' or i[-1] == '!' or i[-1] == '?':
      check = 1                                     

#Teste da função
frase = input()
primeira_maiuscula(frase)
