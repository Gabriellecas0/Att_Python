from no import No
class Lista_Ligada:
    def __init__(self):
        self.primeiro: No = None
        self.tamanho = 0

    def adicionar(self, item):
        """ Adiciona no fim da lista """
        novo_no = No(item)
        if self.primeiro is None:
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
        self.tamanho += 1

    def exibir(self):
        """ Exibe os itens da lista """

        no_atual = self.primeiro
        while no_atual:
            print(no_atual.item, end=" -> ")
            no_atual = no_atual.proximo
        print("null")

    def pesquisar(self, item):
        """Retorna True caso o item procurado exista na lista e False, em caso contrário."""
        atual = self.primeiro
        while atual:
            if atual.item == item:
                return True
            atual = atual.proximo
        return False

    def obter(self, posicao):
        """Retorna o item guardado em uma determinada posição da lista.
        Caso a posição não exista na lista, retorna None."""
        if posicao < 0 or posicao >= self.tamanho:
            return None
        atual = self.primeiro
        cont = 0
        while atual:
            if cont == posicao:
                return atual.item
            atual = atual.proximo
            cont += 1
        return None

    def inserir(self, posicao, item):
        """Adiciona um item em uma posição da lista empurrando os demais itens.
        Se a posição não é válida, retorna False. Se for válida, retorna True."""
        if posicao < 0 or posicao > self.tamanho:
            return False
        if posicao == 0:
            novo_no = No(item)
            novo_no.proximo = self.primeiro
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            contador = 0
            while contador < posicao - 1:
                atual = atual.proximo
                contador += 1
            
            novo_no = No(item)
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no

        self.tamanho += 1
        return True

    def remover(self, posicao):
        """Remove um item de uma posição da lista e retorna True.
        Caso a posição não exista, retorna False."""
        if posicao < 0 or posicao >= self.tamanho:
            return False
        if posicao == 0:
            self.primeiro = self.primeiro.proximo
        else:
            atual = self.primeiro
            contador = 0
            while contador < posicao - 1:
                atual = atual.proximo
                contador += 1
            atual.proximo = atual.proximo.proximo
        self.tamanho -= 1
        return True

    def remover_item(self, item):
        """Remove um item existente na lista e retorna True.
        Caso o item não seja encontrado, retorna False."""
        if self.primeiro is None:
            return False
        if self.primeiro.item == item:
            self.primeiro = self.primeiro.proximo
            self.tamanho -= 1
            return True
        atual = self.primeiro
        while atual.proximo:
            if atual.proximo.item == item:
                atual.proximo = atual.proximo.proximo
                self.tamanho -= 1
                return True
            atual = atual.proximo
        return False