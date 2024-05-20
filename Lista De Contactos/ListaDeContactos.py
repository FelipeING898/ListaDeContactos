from Contactos import Contactos

class ListaDeContactos:
    def __init__(self):
        self.__listaDeContactos = []

    
    def darTodosLosContactos(self):
        return self.__listaDeContactos
    
    def buscarContactosPalabraClave(self, pClave):
        return self.__listaDeContactos[self.__listaDeContactos.index(pClave)]
            

    
