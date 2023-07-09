#Exercicio 2
def deletar_duplicado(palavra):
  lista = []                             #Cria uma lista vazia para armazenar as letras conforme vão aparecendo
  for i in range(len(palavra)):          #Começa uma iteração pra cada letra da palavra/frase
    if palavra[i] in lista:              #Se a palavra já estiver na lista, será ignorada
      continue
    else:                                #Se não estiver na lista, sera impressa normalmente
      print(palavra[i], end='')
      lista.append(palavra[i])
#palavra = input()
#deletar_duplicado(palavra)
