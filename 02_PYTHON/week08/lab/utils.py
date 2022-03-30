# Definición clase Perro y Cat de forma genérica
# Si nos fijamos en los métodos, son iguales e idénticos para
# las dos clases

# class Dog(object):
#     '''
#     Docstring: describir de que va la clase y funciones
#     Admite parámetros 

#     '''
#     def __init__(self, raza, sex, name='Unnamed'):
#         print('Woof, Woof...un cachorrito ha nacido')
#         self.species = "perro"
#         self.raza = raza
#         self.sex = sex
#         self.name = name

#     def present(self):
#         return f"""\n
#         Woof, woof..Hola mi nombre es {self.name}, soy un\n
#         {self.species} y soy un/a {self.sex}!
#         """
    
#     def baptize(self, new_name):
#         self.name = new_name


# class Cat(object):
#     def __init__(self, raza, sex, name='Unnamed'):
#         self.raza = raza
#         self.sex = sex
#         self.name = name
#         self.species = "gato"
#         print('Meow...un cachorrito ha nacido')

#     def present(self):
#         return f"""\n
#         Meow..Hola mi nombre es {self.name}, soy un\n
#         {self.species} y soy un/a {self.sex}!
#         """
    
#     def baptize(self, new_name):
#         self.name = new_name


# Hablaremos entonces de Herencia de clases cuando
# existen patrones, es decir, métodos iguales para el resto
# de clases

class Pet(object):

    def __init__(self, sex, name="Unnamed"):
        self.sex = sex
        self.name = name
        self.species = "mascota"
    
    def speak(self):
        return "Generic Pet sound"

    def present(self):
        return f"Hello. I am a {self.sex} {self.species} named {self.name}"

class Cat(Pet):
    
    def __init__(self, sex, color, name="Unnamed"):
        super().__init__(sex, name)
        self.species = "gato"
        self.color = color