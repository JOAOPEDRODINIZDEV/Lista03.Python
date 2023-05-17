class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self._topo = None
        self.tamanho = 0
   
    def __len__(self):
        return self.tamanho
   
    def is_empty(self):
        return self.tamanho == 0
   
    def inserir(self, valor):
        no = No(valor)
        no.proximo = self._topo
        self._topo = no
        self.tamanho += 1
   
    def remover(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        valor = self._topo.valor
        self._topo = self._topo.proximo
        self.tamanho -= 1
        return valor
   
    def topo(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self._topo.valor

def ordenarLista(lista):
    pilha = Pilha()
    for num in lista:
        while not pilha.is_empty() and pilha.topo() < num:
            lista.append(pilha.remover())
        pilha.inserir(num)
    listaOrdenada = []
    while not pilha.is_empty():
        listaOrdenada.append(pilha.remover())
    return listaOrdenada

lista = []
tam = int(input("Digite o tamanho da lista: "))

for i in range(tam):
    num = int(input("Digite os números da lista: "))
    lista.append(num)

listaOrdenada = ordenarLista(lista)
print("\nOrdem Crescente: \n", listaOrdenada)
