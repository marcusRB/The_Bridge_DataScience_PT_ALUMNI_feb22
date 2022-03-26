# Implementar la clase "Tienda"
class Tienda:
    """
    docstring de la clase tienda
    """
    def __init__(self, 
    tipo = "Electrodomésticos", 
    abierta = True, 
    nombre = "", 
    direccion = "", 
    num_empleados = 0,
    ventas = [0, 0, 0]):
    
        self.tipo = tipo
        self.abierta = abierta
        self.nombre = nombre
        self.direccion = direccion
        self.num_empleados = num_empleados
        self.ventas = ventas
    
    def venta_meses(self):
        return sum(self.ventas)

    def media_ventas(self):
        return (self.venta_meses() / self.num_empleados)

    def nombre_tienda(self):
        return f"Nombre: {self.nombre} Dirección: {self.direccion}"

    def venta_ult_mes(self):
        return self.ventas[-1]

    def proyectar_ventas(self, x):
        ventas_proyectadas = []
        if x < 1000:
            for i in self.ventas:
                ventas_proyectadas.append(1.2 * i)
        else:
            for i in self.ventas:
                ventas_proyectadas.append(1.5 * i)
        
        self.ventas = ventas_proyectadas
        return self.ventas

