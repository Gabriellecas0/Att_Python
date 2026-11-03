#Só consegui testar usando o seu código de teste
from lista_ligada import Lista_Ligada

def test_adicionar_e_exibir():
    lista = Lista_Ligada()
    lista.adicionar(10)
    lista.adicionar(20)
    lista.adicionar(30)
    
    assert lista.tamanho == 3
    assert lista.exibir() == "10 -> 20 -> 30 -> null"

def test_pesquisar():
    lista = Lista_Ligada()
    lista.adicionar(5)
    lista.adicionar(15)
    
    assert lista.pesquisar(15) is True
    assert lista.pesquisar(99) is False

def test_obter():
    lista = Lista_Ligada()
    lista.adicionar(100)
    lista.adicionar(200)
    
    assert lista.obter(0) == 100
    assert lista.obter(1) == 200
    assert lista.obter(5) is None

def test_inserir():
    lista = Lista_Ligada()
    lista.adicionar(10)
    lista.adicionar(30)
    
    assert lista.inserir(1, 20) is True
    assert lista.exibir() == "10 -> 20 -> 30 -> null"
    assert lista.tamanho == 3
    assert lista.inserir(10, 50) is False

def test_remover():
    lista = Lista_Ligada()
    lista.adicionar(10)
    lista.adicionar(20)
    lista.adicionar(30)
    assert lista.remover(0) is True
    assert lista.exibir() == "20 -> 30 -> null"
    assert lista.remover(10) is False

def test_remover_item():
    lista = Lista_Ligada()
    lista.adicionar(5)
    lista.adicionar(10)
    lista.adicionar(15)
  
    assert lista.remover_item(10) is True
    assert lista.exibir() == "5 -> 15 -> null"
    assert lista.remover_item(99) is False
