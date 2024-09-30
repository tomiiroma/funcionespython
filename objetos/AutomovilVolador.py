import Automovil 

import Automovil
class AutomovilVolador(Automovil):
    def __init__(self, ruedas=6):
        super().__init__(ruedas)
        self.esta_volando = True

    def is_volando(self):
        return self.esta_volando
    
    def set_is_volando(self,value):
        self.esta_volando = value

    def vuela(self):
        self.is_volando()
    
    def aterriza(self):
        self.set_is_volando(False)
