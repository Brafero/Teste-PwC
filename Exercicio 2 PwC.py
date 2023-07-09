#Exercicio 2
#Lógica usada: Para evitar que uma letra se repita, basta verificar se a letra já apareceu e não imprimi-la caso tenha aparecido

def deletar_duplicado(palavra):
   #Cria uma lista vazia para armazenar as letras conforme vão aparecendo
  lista = []         

  #Começa uma iteração pra cada letra da palavra/frase
  for i in range(len(palavra)):       
    #Se a palavra já estiver na lista, será ignorada
    if palavra[i] in lista:              
      continue
    #Se não estiver na lista, sera impressa normalmente
    else:                               
      print(palavra[i], end='')
      lista.append(palavra[i])

#Teste da Função
palavra = input()
deletar_duplicado(palavra)
