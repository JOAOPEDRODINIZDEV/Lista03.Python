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
    
def string_para_binario(string):
    pi = Pilha()
    for digito in string:
        pi.inserir(int(digito))
    
    numero_binario = ""
    while not pi.is_empty():
        digito = pi.remover()
        numero_binario += str(digito)
    
    return numero_binario

string = input("Digite uma string contendo números: ")
numero_binario = string_para_binario(string)
print("Número binário convertido:", numero_binario)
