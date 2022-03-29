class Tienda:
    """Estructura general de las tiendas"""
    def __init__(self,estructura,nombre="sin nombre",direccion="sin dirección"):
        self.tipo = "Electrodomésticos"
        self.abierta = True
        self.estructura = estructura
        self.nombre = nombre
        self.direccion = direccion

    def aprovisionamiento(self,inputs):
        """función que agrega las compras de electrodomésticos a la tienda
        ------------------
        args: list"""
        self.estructura["electrodomesticos"] = inputs
        return f"se han añadido los electrodomésticos:\n {inputs}"

    def horario(self,disponibilidad):
        """cambia la disponibilidad de la tienda, cerrado o abierto
        --------------
        args: bool"""
        self.abierta = disponibilidad
        if self.abierta == True:
            return f"La tienda ha sido abierta"
        else:
            return f"La tienda ha sido cerrada"
    
    def contratacion(self,num_empleados):
        """actualiza los empleados de la tienda
        -------------
        args: int"""
        self.estructura["empleados"] += num_empleados
        return f"los empleados han sido actualizados en {num_empleados}"

    def añadir_ventas(self,venta):
        """actualiza las ventas de cada trimestre
        ----------
        args: int"""
        self.estructura["ventas"].append(venta)
        return f"has actualizado las ventas correctamente"
    
    def ventas_totales(self):
        return sum(self.estructura["ventas"])

    def ventas_medias(self,trimestre=0):
        """nos da las ventas medias por empleado en cada trimestre, si no se
        indica nada, las devuelve por año
        ----------------------------
        args: int (1=Q1,2=Q2,3=Q3, default=0 (año))"""
        media = 0
        periodo = ""
        if trimestre == 1:
            media = self.estructura["ventas"][0]/self.estructura["empleados"]
            periodo = "Q1"
        elif trimestre == 2:
            media = self.estructura["ventas"][1]/self.estructura["empleados"]
            periodo = "Q2"
        elif trimestre == 3:
            media = self.estructura["ventas"][2]/self.estructura["empleados"]
            periodo = "Q3"
        else:
            media = self.ventas_totales()/self.estructura["empleados"]
            periodo = "año"
        return f"las ventas medias han sido {media} en el {periodo}"

    def presentacion(self):
        """Nos hace una presentación de la tienda con su nombre y con su
        dirección"""
        return f"La tienda {self.nombre} se encuentra en {self.direccion}"

    def ultimas_ventas(self):
        """Nos devuelve las ventas del último mes registrado"""
        return self.estructura["ventas"][-1]

    def proyeccion_marketing(self,x):
        """Realiza una proyección de las ventas según la inversión en Márketing
        ----------------------
        args: x = int (inversión en márketing)"""
        lista = self.estructura["ventas"]
        for i in range(len(lista)):
            if x < 1000:
                lista[i] = 1.2 * lista[i]
            else:
                lista[i] = 1.5 * lista[i]
        ventas_aumentadas = sum(self.estructura["ventas"])
        return f"las ventas totales serían de {ventas_aumentadas}"