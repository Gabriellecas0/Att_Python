from lista import Lista

minha_lista = Lista(5)


print("--- TESTE ADICIONAR ---")
print(minha_lista.adicionar(10))  
print(minha_lista.adicionar(20))  
print(minha_lista.adicionar(30))  

print("--- TESTE OBTER ---")
print(f"Elemento na posição 1: {minha_lista.obter(1)}")  
print(f"Elemento na posição 5 (inválida): {minha_lista.obter(5)}")  


print("--- TESTE PESQUISAR ---")
print(f"Posição do 30: {minha_lista.pesquisar(30)}")  
print(f"Posição do 99 (não existe): {minha_lista.pesquisar(99)}")  


print("--- TESTE INSERIR ---")
print(minha_lista.inserir(1, 15)) 
print(f"Novo elemento na posição 1: {minha_lista.obter(1)}")  
print(f"Elemento que foi empurrado para a posição 2: {minha_lista.obter(2)}") 


print("--- TESTE REMOVER ---")
print(minha_lista.remover(0))  
print(f"Novo elemento da posição 0: {minha_lista.obter(0)}")  


print("--- TESTE REMOVER NÚMERO ---")
print(minha_lista.remover_num(30))  
print(f"Procurando 30 após remoção: {minha_lista.pesquisar(30)}") 