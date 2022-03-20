# Definimos una variable global
global_var = "This is a global variable"

def fun_1():
    # Definimos una variable local dentro de fun_1
    local_var_1 = "local_var_1 is local to fun_1"
    # Mostramos el valor de la variable global y de la local
    print(global_var)
    print(local_var_1)
    # return local_var_1

#fun_1()

def fun_2():
    # Mostramos la variable global
    print("Variable global fun_2")
    print(global_var)
    
    # Intentamos acceder a la variable local local_var_1,
    # lo que generará un error ya que no está definida
    # dentro de la función fun_2
    print(fun_1())

#fun_2()

def fun_3():
    # Asignamos la variable global_var
    global_var = "Now this is a local var!"
    # Mostramos el valor de global_var
    print(global_var)
    return global_var

fun_3()
print(global_var)
global_var = fun_3()
print(global_var)