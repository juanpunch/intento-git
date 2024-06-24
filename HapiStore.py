import json
def agregarCliente():
    with open("compras.json",mode="r") as lecturaJson:
        leerJson = json.load(lecturaJson)

        nombre = input("Ingrese el nombre del nuevo cliente: ")
        credito = int(input("Ingrese el credito del nuevo cliente: "))
        cliente_nuevo = {
                "id": len(leerJson["clientes"]) + 1,
                "nombre": nombre,
                "credito": credito
            }
    
        leerJson["clientes"].append(cliente_nuevo)

    with open("compras.json",mode="w") as escrituraJson:
        json.dump(leerJson,escrituraJson,indent=4)
        print("Cliente agregado correctamente!")



def editarCiente():
    ide = int(input("ingrese su id para modificar"))
    nom = input("ingrese su nombre para modificar ")
    nombreedit = input("ingrese su nuevo nombre ")
    creditosedit = int(input("ingrese su nueva cantidad"))
    with open("compras.json",mode="r") as lecturaJson:
            leerJson = json.load(lecturaJson)
            contador =0
            for i in leerJson["clientes"]:
                if i ["id"] == ide and i ["nombre"]== nom:
                    print("encontrado")
                    break
                contador +=1

            leerJson["clientes"][contador]["nombre"] = nombreedit
            leerJson["clientes"][contador]["credito"] = creditosedit

    with open("compras.json",mode="w") as escrituraJson:
        json.dump(leerJson,escrituraJson,indent=4)
        print("Cliente editado correctamente!")


def eliminar_cliente():
    ide = int(input("Ingrese el ID del cliente a eliminar: "))
    nom = input("Ingrese el nombre del cliente a eliminar: ")
    with open("compras.json", mode="r") as lecturajson:
        lecjson = json.load(lecturajson)
           
    for i in lecjson["clientes"]:
            if i["id"] == ide and i["nombre"] == nom:
                lecjson["clientes"].remove(i)
                print("cliente eliminado ")
                break
    with open("compras.json", mode="w") as escriturajson:
        json.dump(lecjson, escriturajson, indent=4)

def listar_clientes():
     with open("compras.json", mode="r") as lecturajson:
        lecjson = json.load(lecturajson)

        lecedit = lecjson["clientes"]
        
        for i in lecedit:
             print(i)

def agregar_productos():
    with open("compras.json",mode="r") as lecturajson:
        lecjson = json.load(lecturajson)
        nomproduc = input("Ingrese el nombre del nuevo producto ")
        nuevo_precio = input("ingrese el precio del nuevo producto ")
        
        productos_nuevo = {
            "id": len(lecjson["productos"])+1,
            "nombre":nomproduc,
            "precio":nuevo_precio
        }

        lecjson["productos"].append(productos_nuevo)

    with open("compras.json",mode="w") as escriturajson:
        json.dump(lecjson,escriturajson)








def menu_mantenedores():
    while True:
        opcion = 0
        print("""
****************************
1) Mantenedor de productos
2) Mantenedor de clientes
3) Mantenedor de vendedores
4) Mantenedor de voletas
5) Para salir 
****************************""")
        opcion = int(input("ingrese una opcion "))
        if opcion ==1:
            print("")
        elif opcion == 2:
            menu_mantenedores_clientes()
        elif opcion == 3:
            print("")
        elif opcion == 4:
            print("")
        elif opcion == 5:
             return(print(" a salido "))
        else:
            print("Ingrese una opcion valida del 1 al 5")
   

    
    
def menu_mantenedores_clientes():
    while True:

        print("""
****************************
1) agregar clientes
2) editar clientes
3) Eliminar clientes
4) Listar clientes
5) Salir
****************************""")
        opcion = 0
        opcion = int(input("ingrese una opcion "))
        if opcion ==1:
            agregarCliente()
        elif opcion == 2:
            editarCiente()
        elif opcion == 3:
            eliminar_cliente()
        elif opcion == 4:
            listar_clientes()
        elif opcion == 5:
            return(print("Usted a salido "))
        else:
            print("Ingrese una opcion valida del 1 al 5")
    


def menu_mantenedores_productos():
    while True:
        print("""
****************************
1) agregar Productos
2) editar Productos
3) Eliminar Productos
4) Listar  Productos
****************************
""")
        opcion = 0
        opcion = int(input("ingrese una opcion "))
        if opcion ==1:
            print("")
        elif opcion == 2:
            print("")
        elif opcion == 3:
            print("")
        elif opcion == 4:
            print("")
        elif opcion == 5:
            return(print("Usted a salido "))
        else:
            print("Ingrese una opcion valida del 1 al 5")
    



