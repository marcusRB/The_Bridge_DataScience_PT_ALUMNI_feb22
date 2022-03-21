# Definimos la función outer_fun en el ámbito global
y = 1 # porque me daba la gana de crear una variable global aquí


def outer_fun():

    # Definimos la función inner_fun_1 dentro de outer_fun
    def inner_fun_1():
        # Definimos la variable my_var_if1 dentro inner_fun_1
        my_var_if1 = "This is defined in inner_fun_1"
        # Mostramos el valor de la variable de outer_fun x y la variable
        # global y
        print("Inner fun 1 x:\t{}".format(x))
        print("Inner fun 1 y:\t{}".format(y))

    # Definimos la función inner_fun_2 dentro de outer_fun
    def inner_fun_2():
        # Definimos y mostramos una nueva variable x local a inner_fun_2
        # con valor 5
        x = 5
        print("Inner fun 2 x:\t{}".format(x))

    # Definimos la función inner_fun_3 dentro de outer_fun
    def inner_fun_3():
        # Indicamos que utilizaremos la variable x no local
        # (definida en outer_fun)
        nonlocal x
        # Modificamos y mostramos el valor de x
        x = 7
        print("Inner fun 3 x:\t{}".format(x))

    # Definimos la función inner_fun_4 dentro de outer_fun
    def inner_fun_4():
        try:
            # Intentamos acceder a la variable my_var_if1 definida dentro
            # de inner_fun_1 (lo que generará una excepción)
            print(my_var_if1)
        except NameError:
            print("Error: undefined variable")

    # Mostramos el valor de la variable global y
    print("Outer fun 1 y:\t{}".format(y))

    # Definimos una variable local a outer_fun de nombre x y valor 3
    x = 3
    # Vamos mostrando el valor de x y ejecutando las funciones internas,
    # para ver el efecto que tienen sobre x
    print("Outer fun x:\t{}".format(x))
    inner_fun_1()
    print("Outer fun x:\t{}".format(x))
    inner_fun_2()
    print("Outer fun x:\t{}".format(x))
    inner_fun_3()
    print("Outer fun x:\t{}".format(x))
    inner_fun_4()

outer_fun()