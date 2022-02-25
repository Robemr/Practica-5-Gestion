
def ordenarBurbuja(lista):
	for passnum in range(len(lista)-1,0,-1):
		for i in range(passnum):
			if lista [i]>lista[i+1]:
				temp = lista[i]
				lista[i] = lista[i+1]
				lista[i+1]=temp
lista = list()
numero = input("\n Cuántos números quieres ordenar? ")

for i in range(int(numero)):
	n=input("numero: ")
	lista.append(int(n))

print("\n Lista de números desordenados -> ")
print(lista)

ordenarBurbuja(lista)

print("\n Lista de números ordenados de menor a mayor-> ")
print(lista)
