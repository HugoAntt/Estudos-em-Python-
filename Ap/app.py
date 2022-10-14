
class Computador:

    def __init__(self, marca, modelo, ano, geracao):
        self.marca = ''
        self.modelo = ''
        self.ano = ''
        self.geracao = ''

    def ligar(self):
        print(
            f'Ligando o {self.marca} modelo {self.modelo} ano {self.ano} geracao {self.geracao}')

computador1 = Computador('Positivo', 'Xp', '2017', '5')
computador1.ligar()
