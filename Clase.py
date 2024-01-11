
class coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo 
        self.arrancado = False
    def arrancar(self):
        self.arrancado = True
        print("El", self.marca, self.modelo, "Se ha arrancado")
    def parar(self):
        self.arrancado = True
        print("El", self.marca, self.modelo, "Se ha parado")

Tesla = coche("Tesla", "Model 3")

print(type(Tesla))
print(Tesla.marca)

print(Tesla.arrancado)
Tesla.arrancar()
print(Tesla.arrancado)
