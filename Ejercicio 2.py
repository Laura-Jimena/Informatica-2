
class Paciente:
    def __init__(self):
        self.__nombre=""
        self.__cedula=0
        self.__genero=""
        self.__servicio=""


    def nom_pac(self,nom):
        self.__nombre=nom
    def ced_pac(self,id):
        self.__cedula=id
    def gen_pac(self,gen):
        self.__genero=gen
    def serv_pac(self,serv):
        self.__servicio=serv
    
    def ver_nom_pac(self):
        return self.__nombre
    def ver_ced_pac(self):
        return self.__cedula
    def ver_gen_pac(self):
        return self.__genero
    def ver_serv_pac(self):
        return self.__servicio



class Sistema():
    def __init__(self):
        self.__pac=[]
        self.__num_pac=len(self.__pac)

    def nuevo_paciente(self):
        nom=input("Ingrese el nombre completo del paciente: ")
        id=int(input("Ingrese el documento de identidad del paciente: "))
        gen=input("Ingrese el género del paciente: ")
        serv=input("Ingrese el servicio al que va a acceder el paciente: ")

        p=Paciente()
        p.nom_pac(nom)
        p.ced_pac(id)
        p.gen_pac(gen)
        p.serv_pac(serv)
        self.__pac.append(p)
        self.__num_pac=int(len(self.__pac))

    def ver_paciente(self):
        doc=int(input("Ingrese el número de documento del paciente: "))
        for Paciente in self.__pac:
            if doc==Paciente.ver_ced_pac():
                print("PACIENTE ENCONTRADO.")
                print( "Nombre: " + Paciente.ver_nom_pac())
                print("Documento: "+ str(Paciente.ver_ced_pac()))
                print("Género: "+ Paciente.ver_gen_pac())
                print("Servicio: "+ Paciente.ver_serv_pac())

    def ver_num_pac(self):
        return self.__num_pac 
    

Sist_de_gest= Sistema()

print ("""Bienvenido al sistema de gestion de pacientes:
Seleccione la opción correspondiente:""")
while True:
    opc=int(input("""1.Ingresar un nuevo paciente.
    2.Ver los datos de un paciente.
    3. Ver el número de pacientes.
    4. Salir."""))
    if opc==1:
        Sist_de_gest.nuevo_paciente() 
        continue
    elif opc==2:
        Sist_de_gest.ver_paciente()
        continue
    elif opc==3:
        print("El número de pacientes es: "+ str(Sist_de_gest.ver_num_pac()))
    elif opc==4:
        print("Saliendo del sistema...")
        break
    else: 
        print ("Ingrese una opción valida.")
        continue
