#Exercicio 5
#Lógica usada: Pra saber se algum anagrama pode ser um palindromo, é preciso que todas as letras se repitam ao menos uma vez ou que 
#apenas uma letra não se repita. Com isso em mente, pensei em associar a cada letra o numero de vezes que ela se repete e armazenar numa lista. 
#Caso o numero 1 apareça duas vezes ou mais em qualquer lugar da lista, nenhum anagrama poderia formar um palindromo.


def anagrama_palindromo(palavra):
  #Cria uma lista vazia para comparação
  lista = [] 

   #Pra cada letra da apalavra, atribui o valor "1" á lista pra representar quantas vezes aparece
  for i in range(len(palavra)):
    lista.append(1) 

  #Pra cada elemento da palavra, percorre os elementos posteriores, verificando se são iguais. Caso sejam, incrementa seus respectivos valores atribuidos na lista
  for i in range(len(palavra)):
    for j in range(i+1,len(palavra)):
      if palavra[i] == palavra[j]:
        lista[i] += 1
        lista[j] += 1

  #Cria um verificador pra saber quantas vezes o numero 1 aparece na lista
  verificador = 0
  for i in lista:
    if i == 1:
      verificador += 1

  #Caso o numero 1 apareça mais de uma vez, retornamos Falso. Se não, retornamos Verdadeiro
  if verificador > 1:
    print("false")
  else:
    print("true")
        
#Teste da função
palavra = input()
anagrama_palindromo(palavra)
