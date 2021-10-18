import random

class ChuteNumero:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 10
        self.valor_gerado = 0
        self.valor_digitado = 0

    def iniciar(self):
        self.gerador_numero()
        print("O número aleatório foi gerado. Tente adivinhar... \n")
        try:
            while self.valor_digitado != self.valor_gerado:
                self.valor_digitado = int(input("Digite o número: \n"))
                if self.valor_digitado > self.valor_gerado:
                    print("Digite um valor menor \n")
                elif self.valor_digitado < self.valor_gerado:
                    print("Digite um valor maior \n")
            
            print("Parabéns, você acertou o número!")
        except:
            print("Favor digitar apenas valores válidos")


    def gerador_numero(self):
        self.valor_gerado = random.randint(self.valor_minimo, self.valor_maximo)


chute = ChuteNumero()
chute.iniciar()

