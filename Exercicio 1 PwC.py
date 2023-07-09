#Exercicio 1
#Lógica usada: Para inverter a ordem das palavras de uma frase, pensei em guarda-las ao contrário em uma lista e imprimir a lista

def reverter_ordem(palavra):
  #Divide as diferentes palavras da frase e as armazena em uma lista
  temp = palavra.split()                 
  #Inverte a ordem em que aparecem as palavras
  temp.reverse()      
  #Imprime palavra por palavra
  for i in temp:
    print(i, end=' ')                    
