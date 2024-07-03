from funciones import *
#--PERMITE CARGAR TODA LA DEPENDENCIAS DEL ARCHIVO FUNCIONES EL * Abarca todo
#--Igual que en SQL 

#---ES POR ESO QUE SE PUEDE LLAMAR A URL_VENTAS POR EJEMPLO QUE ESTA EN EL ARCHIVO FUNCIONES ACA.   Podriamos importar el archivo y hacer fn.llamar a la funcion pero queda mas ordenado asi. :) Tndriamos que hacerlo por cada Funcion y no es bonito.
#--LLAME A LA FUNCION DE MENU ACA PARA QUE SEA MAS FACIL ESTRUCTURAR EL CODIGO Y SEA FACILMENTE ENTENDIBLE(?)

def menu():
    menupal=True
    while menupal:
        ventas = cargar_datos_json(URL_VENTAS)
        empleados = cargar_datos_json(URL_EMPLEADOS)
        productos = cargar_datos_csv(URL_PRODUCTOS)
        print("\n===MENU PRINCIPAL===")
        print('****CAFETERIA*****')
        print("1. Precargar ventas")
        print("2. Crear Venta")
        print("3. Reporte de sueldos")
        print("4. Ver estadisticas")
        print("5. Salir")
        op=0
        try:
            op= int(input('Ingrese opcion --> '))
            if op>5 or op<1:
                print('Opcion fuera de rango')
        except:
            print('Opcion no valida.Ingrese de nuevo')
        if op==1:
            print('***'*5)
            print('Precargar ventas')#--ESTO DESPUES LLAMO A OTRA FUNCION QUE SE ENCARGUE DE PRECARGAR LAS VENTAS
            precargar_ventas(ventas,empleados,productos)
            print('***'*5)
        elif op==2:
            print('***'*5)
            print('Crear ventas')#--ESTO DESPUES LLAMO A OTRA FUNCION QUE SE ENCARGUE DE PRECARGAR DE CREAR LAS VENTAS
            crear_venta(ventas,empleados,productos)
            print('***'*5)
        elif op==3:
            print('***'*5)
            print('Reporte de sueldos') #--ESTO DESPUES LLAMO A OTRA FUNCION QUE SE ENCARGUE DE HACER UN REPORTE DE LOS SUELDOS
            reporte_sueldos(empleados,ventas)
            print('***'*5)
        elif op==4:
            print('***'*5)
            print('ver estadisticas')#--ESTO DESPUES LLAMO A OTRA FUNCION QUE SE ENCARGUE DE VER ESTADISTICAS
            ver_estadisticas(ventas)
            print('***'*5)
        elif op==5:#--OPCION PARA SALIR
            menupal=False 

#--ESTO ES PARA LOGRAR QUE ESTE SEA EL PROGRAMA(ARCHIVO) PRINCIPAL
#LOGRA QUE MENU SEA LA FUNCION PRINCIPAL ACA  

if __name__ == "__main__":
    menu()
