class contactos: 
    def __init__(self, nombre, apellido, direccion, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__correo = correo
        self.__telefonos = []
        self.__palabras = []
        
    
    def darNombre(self):
        return self.__nombre
    
    def darApellido(self):
        return self.__apellido
    
    def darDireccion(self):
        return self.__direccion
    
    def darCorreo(self):
        return self.__correo
    
    def darTelefonos(self):
        return self.__telefonos
    
    def darPalabras(self):
        return self.__palabras
    
    def cambiarDireccion(self, nDireccion):
        self.darDireccion = nDireccion 

    def cambiarCorreo(self, nCorreo):
        self.darCorreo = nCorreo
    
    def cambiarTelefonos(self, nTelefonos):
        self.darTelefonos = nTelefonos
    
    def agregarTelefono(self, nTelefono):
        if nTelefono not in self.__telefonos:
            self.__telefonos.append(nTelefono)

    def eliminarTelefono(self, telefono):
        if telefono in self.__telefonos:
            self.__telefonos.remove(telefono)

    def agregarPalabra(self, nPalabra):
        if nPalabra not in self.__palabras:
            self.__palabras.append(nPalabra)

    def eliminarPalabra(self, palabra):
        if palabra in self.__palabras:
            self.__palabras.remove(palabra)

    def contienePalabraClave(self, pClave):
        palabraClave = False
        if pClave in self.__palabras:
            palabraClave = True

        return palabraClave
