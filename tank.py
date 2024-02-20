class Tank:
    def __init__(self, cor):
        self.cor = cor

    def atirar(self):
        print("Atirou.")

tank1 = Tank('Amarelo')

print(tank1.cor)
tank1.atirar()
