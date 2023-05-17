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
    
def bi_para_dec(binario):
    pi = Pilha()
    for digito in binario:
        pi.inserir(int(digito))
        
    decimal = 0       
    potencia = 0

    while not pi.is_empty():
        digito = pi.remover()
        decimal += digito * (2 ** potencia)
        potencia += 1
    
    return decimal

binario = input("Digite um número binario: ")
numero_decimal = bi_para_dec(binario)
print("Número convertido em decimal é: ", numero_decimal)


















        
        
    



