from chatbot import *

a.fala

print(' ')

print("Qual é o seu nome?")
nome = input('>:')
nome = nome.title()

print(' ')


while True:
  if nome ==  'Izabela':
    print(f'Esse é o nome da minha criadora muito prazer {nome}')
    break

  elif nome == 'Eliete':
    print(f"Esse é o mesmo nome da dona da loja muito prazer {nome}")
  else:
    print(f"Muito prazer {nome}")
    break




print(' ')

b.question1()
leed = int(input('>:'))

print(' ')

if leed == 1:
  print("Venha visitar nossa loja e São Jose da Lapa \n Rua Presidente Costa e Silva")
elif leed == 2:
  print("siga nosso instagram @tatatattata")
elif leed == 3:
  print("Venha visitar nossa loja e São Jose da Lapa \n Rua Presidente Costa e Silva siga nosso instagram @tatatattata ")

if leed>=4:
  print('Eu não entende')


print(' ')

c.question2()
serviço = int(input(">:"))

print(' ')

if serviço == 1:
  print("Por favor Aguarde Eliete responder para ela citar o catalogo")



elif serviço == 2:
  print('Qual o tema da festa?')
  festa = input('>:')
  print("Por favor Aguarde Eliete responder")

elif serviço == 3:
  print("qual tipo de personalização? \n 1- foto \n 2- logo \n 3- personalizado")
  blusa = int('>:')
  print("Por favor Aguarde Eliete responder")

if serviço >=4:
  print("Não entende")

print(" ")


print('espero que o atendimento tenha sido agradavel. Até mais')
  
  