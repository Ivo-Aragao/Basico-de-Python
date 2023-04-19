#1ª Escreva um programa em Python que imprima a soma dos números de 1 a 10.

soma = 0
for i in range(1, 11):
    soma += i
print("A soma dos números de 1 a 10 é:", soma)

#2ª Escreva um programa em Python que imprima os números ímpares de 1 a 20.
for i in range(1, 21, 2):
    print(i)

#3ª num = int(input("Digite um número inteiro: "))

num = int(input("Digite um número inteiro: "))

if num % 2 == 0:
   print(num, "é par.")
else:
   print(num, "é ímpar.")     
   
#4ª num = int(input("Digite um número inteiro: "))

num = int(input("Digite um número inteiro: "))

if num > 0:
    print(num, "é positivo.")
elif num < 0:
    print(num, "é negativo.")
else:
    print(num, "é zero.")   

#5ª Escreva um programa em Python que leia dois números inteirose imprima o maior deles.     

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num1 > num2:
    print(num1, "é maior.")
else:
    print(num2, "é maior.")
    
#6ªEscreva um programa em Python que leia um número inteiro 
#e imprima a tabuada desse número (de 1 a 10). 

num = int(input("Digite um número inteiro: "))

for i in range(1, 11):
    print(num, "x", i, "=", num*i)    
    
#7ª Escreva um programa em Python que leia um número inteiro e imprima a sequência de Fibonacci até esse número.

num = int(input("Digite um número inteiro: "))

a, b = 0, 1
while b <= num:
    print(b, end=" ")
    a, b = b, a + b

#8ª Escreva um programa em Python que leia uma lista de números e imprima o maior e o menor número da lista.

num_list = []

n = int(input("Digite o tamanho da lista: "))

for i in range(n):
    num = int(input("Digite um número: "))
    num_list.append(num)

print("A lista é:", num_list)

maior = num_list[0]
menor = num_list[0]

for num in num_list:
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

print("O maior número da lista é:", maior)
print("O menor número da lista é:", menor)    

#9ª Escreva um programa em Python que leia uma lista de números e imprima a média dos números.

num_list = []

n = int(input("Digite o tamanho da lista: "))

for i in range(n):
    num = float(input("Digite um número: "))
    num_list.append(num)

print("A lista é:", num_list)

soma = sum(num_list)
media = soma / n

print("A média da lista é:", media)

# 10ª Escreva um programa em Python que leia uma lista de números e imprima apenas os números pares da lista.

num_list = []

n = int(input("Digite o tamanho da lista: "))

for i in range(n):
    num = int(input("Digite um número: "))
    num_list.append(num)

print("A lista é:", num_list)

print("Os números pares da lista são:")

for num in num_list:
    if num % 2 == 0:
        print(num)
        
#11ª Escreva um programa em Python que leia uma lista de números e imprima apenas os números ímpares da lista.

num_list = []

n = int(input("Digite o tamanho da lista: "))

for i in range(n):
    num = int(input("Digite um número: "))
    num_list.append(num)

print("A lista é:", num_list)

print("Os números ímpares da lista são:")

for num in num_list:
    if num % 2 != 0:
        print(num)
        
#12ª Escreva um programa em Python que leia uma lista de números e imprima a soma dos números.        
            
num_list = []

n = int(input("Digite o tamanho da lista: "))

for i in range(n):
    num = int(input("Digite um número: "))
    num_list.append(num)

print("A lista é:", num_list)

soma = sum(num_list)

print("A soma dos números é:", soma)

#13ª Escreva um programa em Python que leia uma lista de números e imprima a lista em ordem crescente.

num_list = []

n = int(input("Digite o tamanho da lista: "))

for i in range(n):
    num = int(input("Digite um número: "))
    num_list.append(num)

print("A lista original é:", num_list)

num_list.sort()

print("A lista em ordem crescente é:", num_list)

#14ª Escreva um programa em Python que leia uma lista de números e imprima a lista em ordem decrescente.

num_list = []

n = int(input("Digite o tamanho da lista: "))

for i in range(n):
    num = int(input("Digite um número: "))
    num_list.append(num)

print("A lista original é:", num_list)

num_list.sort(reverse=True)

print("A lista em ordem decrescente é:", num_list)

#15ª Escreva um programa em Python que leia uma lista de números e um número x e imprima se o número x está na lista.

num_list = []

n = int(input("Digite o tamanho da lista: "))

for i in range(n):
    num = int(input("Digite um número: "))
    num_list.append(num)

x = int(input("Digite um número para procurar na lista: "))

if x in num_list:
    print("O número", x, "está na lista!")
else:
    print("O número", x, "não está na lista!")