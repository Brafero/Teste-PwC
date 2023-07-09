#Exercicio 4
#Lógica usada: Em um parágrafo, a primeira palavra e todas as que sucedem ".", "!" ou "?" devem ter a primeira letra maiúscula.
#Com isso, pensei em verificar se o último caracter de cada palavra é uma pontuação, o que implicaria que a próxima palavra
#deve ter a primeira letra maiúscula. 


def primeira_maiuscula(frase):
  temp = frase.split()                               #Divide a frase em uma lista pra analisar mais facilmente cada palavra
  check = 1                                          #Cria uma variável de comparação para saber quando deve ser maísuscula
  for i in temp:                                     #Pra cada uma das palavras...
    if check == 1:                                   #Verifica se deve ser maiuscula
      print(i.capitalize(), end=' ')                 #Caso seja, imprime a letra maiuscula...
      check = 0                                      #E define o valor da comparação para 0
    else:                                            #Caso não deva ser maiuscula...
      print(i, end=' ')                              #Imprime a palavra normalmente
    if i[-1] == '.' or i[-1] == '!' or i[-1] == '?': #Se a palavra termina com alguma pontuação...
      check = 1                                      #A próxima palavra será maiuscula

#frase = input()
#primeira_maiuscula(frase)
