class coche:
    def __init__(self,color,marca,aceleracion):
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = 0
        self.ruedas = 4
        

        # getter
    def get_color(self):
        return self.color


    def get_marca(self):
        return self.marca

        
    def get_aceleracion(self):
        return self.aceleracion


    def get_velocidad(self):
        return self.velocidad


    def get_ruedas(self):
        return self.ruedas


        # setters
    def set_color(self,value):
        self.color = value


    def set_marca(self,value):
        self.marca = value

        
    def set_aceleracion(self,value):
        self.aceleracion = value


    def set_velocidad(self,value):
        self.velocidad = value


    def set_ruedas(self,value):
        self.ruedas = value



    def acelera(self):
        self.velocidad = self.velocidad+self.aceleracion
        

    def frena(self):
        v = self.velocidad-self.aceleracion
        if v < 0:
            v = 0
        self.velocidad = v
            


c1 = coche("Rojo","Chevrolet",20)


print (c1.ruedas)

print (c1.color)

print ("Aceleracion default: "+str(c1.get_aceleracion()))
c1.set_aceleracion(25)
print("Nueva Aceleracion: "+str(c1.get_aceleracion()))

c2 = coche("Negro","Ferrari",30)

c2.frena()

print("Nueva velocidad coche 2: "+str(c2.get_aceleracion()))
