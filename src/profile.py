'''
Crear una clase que represente al perfil usuario que ademas tenga una relacion (herencia) con estas dos clases: 
    administrador 
    reportero (solo tiene lectura de datos). 
El usuario tiene objeto carrito de compras. 
El administrador puede ver a todos los usuarios y lo que tenga adentro. 
El reporter solo ve todos los carritos de compra.
'''
class userProfile:
    carrito_de_compras = []
    def __init__(self,userName,nombre,apellido,dni,telefono):
        self.userName = userName
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono

    def __str__(self):
        return "Nombre de Usuario: {}\nNombre: {}\nApellido: {}\nDNI: {}\nTelefono: {}\nCarrito de Compras: {}\n".format(self.userName,self.nombre,self.apellido,self.dni,self.telefono,self.carrito_de_compras)
    
class administrator(userProfile):
    pass

class reportero(userProfile): 
    pass

    
user = userProfile("GVega","Gustavo","Vega","52369741","5555-2525")
user1 = reportero("SVega","Sofia","Vega","123456789","5555-5555")
user2 = administrator("LVega","Lucia","Vega","78945621","5555-5535")

print(user)
print(user1)
print(user2)