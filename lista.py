def pesquisar(lista, tamanho, numero):
    for i in range(tamanho):
        if lista[i] == numero:
            return True
    return False

lista = [3, 5, 8, 10, 15]
tamanho = 5

print(f"Achou o 10 ? = {pesquisar(lista, tamanho, 10)}") 
print(f"Achou o 3  ? = {pesquisar(lista, tamanho, 3)}")   
print(f"Achou o 6  ? = {pesquisar(lista, tamanho, 6)}")   
print(f"Achou o 1  ? = {pesquisar(lista, tamanho, 1)}")   