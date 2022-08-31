

class Agenda:
    def __init__(self):
        self.contactos = []
    def menu (self):
        print()
        menu =[
            ["Agenda Personal"],
            ["1- Añadir a contacto","Añadir"],
            ["2- Lista de contactos"],
            ["3- Buscar contacto"],
            ["4- Editar contacto"],
            ["5- Cerrar agenda "]
        ]
        for x in range(6):
            print(menu[x][0])
        opcion = int(input("Introduzca la opciondeseada: "))
        if opcion == 1:
            self.añadir()
        elif opcion == 1:
            self.lista()
        elif opcion == 3:
            self.buscar()
        elif opcion == 4:
            self.editar()   
        elif opcion == 5:
            print("Cerrando la agenda...")
            exit()

        self.menu()

    def añadir(self):
        print("Añadir un nuevo contacto ")
        nombre_contacto=input("Ingrese el nombre: ")
        telefono=int(input("Ingrese el telefono: "))
        email=input("introduzca el Email: ")
        #append() para agregar un elemento de cualquier tipo al final de una lista
        self.contactos.append({"nombre: ":nombre_contacto, "Telefon ":telefono, "Email ":email})
   
    def  lista_contactos (self):
        print("Lista de contactos")
        if len(self.contactos) == 0:
            print("Ustded aun no tiene contactos ")
        else :
            for x in range(len(self.contactos)):
                print(self.contactos[x]["Nombre"])

    def buscar(self):
        print("Buscador de contactos ")
        nombre_contacto = input("Introduzca el nombre del contacto: ")
        for x in range(len(self.contactos)):
            if nombre_contacto == self.contactos[x]["Nombre"]:
                print("Los datos del contacto son: ")
                print("Nombre: ",self.contactos[x]['nombre'])
                print("Telefono: ", self.contactos[x]["telefono"])
                print("Email: ", self.contactos[x]["Email"])
                return x 

    def editar(self):
        print("Editarcontactos ")
        data = self.buscar()
        condition = False
        while condition == False:
            print("Selecciona que quieres editar: ")
            print("1. Nombre")
            print("2. Teléfono")
            print("3. E-mail")
            print("4. Volver")
            opcion = int(input("Introduzca la opción deseada: "))
            if opcion == 1:
                    nombre_contacto = input("Introduzca el nuevo nombre: ")
                    self.contactos[data]['nombre'] = nombre_contacto
            elif opcion == 2:
                    telefono = input("Introduzca el nuevo teléfono: ")
                    self.contactos[data]['telf'] = telefono
            elif opcion == 3:
                    email = input("Introduzca el nuevo email: ")
                    self.contactos[data]['email'] = email
            elif opcion == 4:
                    condition = True
		
   
agenda=Agenda()
agenda.menu()