class MobilePhone():
    '''
    Docstring de una clase
    '''
    def __init__(self, phone):
        self.phone = phone # convertimos el parámetro de entrada como variable global a nivel de clase
        print("La clase MobilePhone ha inicializado")

    def install_app(self, appname):
        self.phone['apps'].append(appname)
        print(self.phone['apps'])
    
    def remove_app(self, appname):
        for pos,i in enumerate(self.phone['apps']):
            if i['name'] == appname:
                self.phone['apps'].pop(pos)
        print(self.phone['apps'])

# mobile
mobile = {
    "marca" : "Samsung",
    "SO": "Android",
    "version" : "5.6",
    "modelo" : "A22",
    "screen_size" : 7,
    "weight" : 200,
    "color" : "silver",
    "RAM" : 8,
    "memoria" : 512,
    "camara" : {
        "frontal" : {"resolution":"15MP"},
        "back" : [
            {"type": "zoom",
            "resolution": "25MP"},
            {"type": "macro",
            "resolution": "30MP"}
            ]
        },
    "bateria" : {"type" : "Lithium",
                "MaxCharge" : 4500,
                "charge":0.56},
    "apps" : [
        {
        "name" : "Whatsapp",
        "version" : "1.56.0",
        "memoria_ocupada" : "15Mb",
        "desarrollador" : "Meta"
        },
        {
        "name" : "Gmail",
        "version" : "123.56.0",
        "memoria_ocupada" : "105Mb",
        "desarrollador" : "Google"
        }
    ]
}

# Instanciamos a un objeto la clase MobilePhone
telefono = MobilePhone(mobile)

youtube = {
    "name" : "YouTube",
    "vers": "10.50",
    "desarrolador": "Google",
    "memoria_ocupada": "300Mb"
}

telefono.install_app(youtube)

telefono.remove_app(youtube)
