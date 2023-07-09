#Exercicio 1
def reverter_ordem(palavra):
  temp = palavra.split()                 #Divide as diferentes palavras da frase e as armazena em uma lista
  temp.reverse()                         #Inverte a ordem das palavras, deixando como o enunciado pede
  for i in temp:
    print(i, end=' ')                    #Imprime palavra por palavra
palavra = input()
reverter_ordem(palavra)




#Exercicio 2
def deletar_duplicado(palavra):
  lista = []                             #Cria uma lista vazia para armazenar as letras conforme vão aparecendo
  for i in range(len(palavra)):          #Começa uma iteração pra cada letra da palavra/frase
    if palavra[i] in lista:              #Se a palavra já estiver na lista, será ignorada
      continue
    else:                                #Se não estiver na lista, sera impressa normalmente
      print(palavra[i], end='')
      lista.append(palavra[i])
palavra = input()
deletar_duplicado(palavra)




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
palavra = input()
subPalindromo(palavra)




#Exercicio 4
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

frase = input()
primeira_maiuscula(frase)




#Exercicio 5
def anagrama_palindromo(palavra):
  lista = []
  for i in range(len(palavra)):
    lista.append(1)
  for i in range(len(palavra)):
    for j in range(i+1,len(palavra)):
      if palavra[i] == palavra[j]:
        lista[i] += 1
        lista[j] += 1
  verificador = 0
  for i in lista:
    if i == 1:
      verificador += 1
  if verificador < 2:
    print("true")
  else:
    print("false")
        

palavra = input()
anagrama_palindromo(palavra)
