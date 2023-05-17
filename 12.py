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
    
def bi_para_dec(string):
    pi = Pilha()
    for caractere in string:
        if caractere.isdigit():
            pi.inserir(int(caractere))
        
    decimal = 0       
    posicao = 0

    while not pi.is_empty():
        digito = pi.remover()
        decimal += digito * (10 ** posicao)
        posicao += 1
    
    return decimal

string = input("Digite uma string contendo números: ")
numero_decimal = bi_para_dec(string)
print("Número convertido em decimal é: ", numero_decimal)
