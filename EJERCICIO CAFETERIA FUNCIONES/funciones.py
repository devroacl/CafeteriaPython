import json  #GUARDAR EL JSON
import csv   #GUARDAR EL CSV
import random as rd  #PARA SACAR NUMEROS AL AZAR
import math


URL_EMPLEADOS = 'empleado.json'
URL_CARGOS = 'cargos.json'
URL_VENTAS = 'ventas.json' 
URL_PRODUCTOS = 'productos.csv'

def cargar_datos_json(url):
    try:
        with open(url, 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        return []

def cargar_datos_csv(url):
    try:
        with open(url, 'r', encoding='utf-8') as file:
            return list(csv.DictReader(file))   
    except:
        return []

def guardar_ventas(ventas):
    with open(URL_VENTAS, 'w', encoding='utf-8') as file:
        json.dump(ventas, file, indent=4)

def precargar_ventas(ventas,empleados,productos):
    if not empleados: 
        print("No hay empleados cargados en el sistema")
        return 
    if not productos:
        print("No hay productos cargados en el sistema")
        return
    for i in range(80):
        venta = {
            "id_venta": f"V{len(ventas) + 101}",
            "empleado": rd.choice(empleados)['id_empleado'],
            "fecha": "2024-06-15",
            "total_venta": 0,
            "productos": [],
            "propina": 0
        }
        num_productos = rd.randint(1,5)
        for j in range(num_productos):
            producto_seleccionado = rd.choice(productos)
            cantidad = rd.randint(1,10)
            subtotal = int(producto_seleccionado['precio'])* cantidad
            venta['productos'].append({
                "id_producto": producto_seleccionado['id_producto'],
                "cantidad": cantidad,
                "precio_unitario": int(producto_seleccionado['precio']),
                "subtotal": subtotal
            })
            venta['total_venta'] = venta['total_venta'] + subtotal 
        ventas.append(venta)
    guardar_ventas(ventas)
    print("\n 80 ventas aleatorias precargadas")

def crear_venta(ventas,empleados,productos):
    while True:
        empleado_id = input("Ingrese el ID del empleado que realiza la venta (o 'C' para salir): ").upper()
        if empleado_id == 'C':
            print("Operacion cancelada.")
            return
        
        #Verificacion del ID empleado
        flag = False
        for e in empleados:
            if e['id_empleado'] == empleado_id:
                flag = True
                break
        
        if flag == True:
            break
        else:
            print("Empleado no encontrado. Porfavor, intente nuevamente")
    
    venta = {
        "id_venta": f"V{len(ventas) + 101}",
        "empleado": empleado_id,
        "fecha": "2024-06-15",
        "total_venta": 0,
        "productos": [],
        "propina": 0
    }
    while True:
        producto_id= input("Ingrese el ID del producto (o 'fin' para terminar):").upper()
        if producto_id.lower() == 'fin':
            break
        producto = None
        for p in productos:
            if p['id_producto'] == producto_id:
                producto = p
                break
        if producto is not None:
            cantidad = int(input("Ingrese la cantidad: "))
            subtotal = int(producto['precio'])*cantidad
            venta['productos'].append({
                "id_producto": producto_id,
                "cantidad": cantidad,
                "precio_unitario": int(producto['precio']),
                "subtotal": int(subtotal)
            })
            venta['total_venta'] = int(venta['total_venta']) + subtotal 
        else: 
            print("Producto no encontrado.")
    
    venta['propina'] = venta['total_venta'] * 0.1 #10% de propina
    ventas.append(venta)
    guardar_ventas(ventas)
    print("\nVenta creada y guardada exitosamente")




def calcular_sueldos(empleado, ventas):
    sueldo_base = empleado['sueldo_base']
    propinas = 0 
    for venta in ventas:
        if venta['empleado'] == empleado['id_empleado']:
            propinas = propinas + venta['propina']
    total_ventas = 0
    for venta in ventas: 
        if venta['empleado'] == empleado['id_empleado']:
            total_ventas = total_ventas + venta['total_venta']
            
    salud = sueldo_base * 0.07 
    afp = sueldo_base * 0.12
    bono = 0
    if total_ventas >2000000:
        bono = total_ventas * 0.05
    elif total_ventas > 1000000:
        bono = total_ventas * 0.02 
    elif total_ventas > 500000:
        bono = total_ventas * 0.01
    sueldo_liquido = (sueldo_base - salud -afp) + propinas + bono

    return {
        "sueldo_base": sueldo_base,
        "propinas": propinas,
        "salud": salud,
        "afp": afp,
        "bono": bono,
        "sueldo_liquido": sueldo_liquido
    }
    
def reporte_sueldos(empleados,ventas):
    #cabecera de la tabla
    print(f"{'Empleado' :>14} | {'Sueldo Bruto' :>12} | {'Propinas':>8} | {'Bono':>5} | {'Descuento Salud':>18} | {'Descuento AFP':>12} | {'Sueldo Líquido':>14}")
    print('-' * 103)
    
    for empleado in empleados: 
        sueldo = calcular_sueldos(empleado,ventas)
        print(f"{empleado['nombre']:>14} | {sueldo['sueldo_base']:>12} | {sueldo['propinas']:>8} | {sueldo['bono']:>5} | {round(sueldo['salud']):>18} | {round(sueldo['afp']):>13} | {round(sueldo['sueldo_liquido']):>14}")
    
def ver_estadisticas(ventas):
    if not ventas:
        print("No hay ventas para mostrar estadisticas")
        return

    ventas_ordenadas = ventas[:]
    for i in range(len(ventas_ordenadas)):
        for j in range(i + 1, len(ventas_ordenadas)):
            if ventas_ordenadas[i]['total_venta'] < ventas_ordenadas[j]['total_venta']:
                ventas_ordenadas[i], ventas_ordenadas[j] = ventas_ordenadas[j], ventas_ordenadas[i]
    
    print("\n5 Ventas mas altas:")
    for venta in ventas_ordenadas[:5]:
        print(f"ID Venta: {venta['id_venta']}, Total: {venta['total_venta']}, Empleado: {venta['empleado']}")
    
    print("\n5 Ventas mas bajas:")
    ventas_ordenadas_alrevez = ventas_ordenadas[::-1]
    for venta in ventas_ordenadas_alrevez[:5]:
        print(f"ID Venta: {venta['id_venta']}, Total: {venta['total_venta']}, Empleado: {venta['empleado']}")
    
    #Calcular la media geometrica de las ventas
    venta_valores = [venta['total_venta'] for venta in ventas]
    
    if len(venta_valores) == 0:
        print("No hay ventas para calcular la media geométrica.")
    else:
        media_geometrica = math.exp(sum(math.log(valor) for valor in venta_valores) / len(venta_valores))
        print(f"\nMedia Geometrica de las ventas: {round(media_geometrica)}")
