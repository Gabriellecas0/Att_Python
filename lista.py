class Lista:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.array = [None] * capacidade
        self.tamanho = 0

    def adicionar(self, numero):
        if self.tamanho < self.capacidade:
            self.array[self.tamanho] = numero
            self.tamanho += 1
            return True
        return False

    def pesquisar(self, numero):
        for i in range(self.tamanho):
            if self.array[i] == numero:
                return i
        return -1

    def obter(self, posicao):
        if posicao >= 0 and posicao < self.tamanho:
            return self.array[posicao]
        return None

    def inserir(self, posicao, numero):
        if self.tamanho >= self.capacidade:
            return False

        if posicao < 0 or posicao > self.tamanho:
            return False

        for i in range(self.tamanho, posicao, -1):
            self.array[i] = self.array[i - 1]

        self.array[posicao] = numero
        self.tamanho += 1
        return True

    def remover(self, posicao):
        if posicao < 0 or posicao >= self.tamanho:
            return False

        for i in range(posicao, self.tamanho - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.tamanho - 1] = None
        self.tamanho -= 1
        return True

    def remover_num(self, numero):
        posicao = self.pesquisar(numero)
        if posicao != -1:
            return self.remover(posicao)
        return False