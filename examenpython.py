#Creamos el archivo
import json
import requests

class Empleados:        
    def mostrar(self):
        self.archivo = open("empleados.txt", "r", encoding="utf-8")
        lista = self.archivo.read().split('\n')
        empleado1 = lista[0].split(sep=', ')
        
        
        diccionarioEmpleado1 = {"firstname": empleado1[0],"surname": empleado1[1],
                                "country":{"name": empleado1[2],
                                            "airports": [{"name":empleado1[4]}]},
                                "languageName": [{"name": empleado1[3]}]}  
        
        resp1 = requests.post('http://localhost:8090/apiv1/employee/add', json=diccionarioEmpleado1)

        print(resp1)
        print(resp1.json())
        
        return diccionarioEmpleado1


#Mandar traer los métodos
empleados1 = Empleados()
empleados1.mostrar()
