from Contactos import Contactos

class ListaDeContactos:
    def __init__(self):
        self.__listaDeContactos = []

    
    def darTodosLosContactos(self):
        return self.__listaDeContactos
    
    def buscarContactosPalabraClave(self, pClave):
        return self.__listaDeContactos[self.__listaDeContactos.index(pClave)]
            

    def agregarContacto(self, nombre, apellido, direccion, correo):
        agregado = False
        nuevo = Contactos(nombre, apellido, direccion, correo)
        if nombre not in self.__listaDeContactos:
            self.__listaDeContactos.append(nuevo)
            agregado = True
            
        return agregado 
        
    def eliminarContacto(self, nombre):
        eliminado = False
        if nombre in self.__listaDeContactos:
            self.__listaDeContactos.remove(nombre)
            eliminado = True
        return eliminado
    
    def modificarContacto(self, nombre, apellido, direccion, correo):
        modificado = False
        for contacto in self.__listaDeContactos: 
            if Contactos.darNombre() == nombre:
                Contactos.darApellido() == apellido:

            
            
            
            