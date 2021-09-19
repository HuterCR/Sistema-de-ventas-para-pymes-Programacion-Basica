##############################################
#       Programa de Sistema de Venta         #
# Creado y Desarrollado por los Estudiantes: #
#      Anthony Jhoan Vega Villalobos         #
#          Emanuel Chacon Salazar            #
#               Copyright  ©                 #
#   Version: Final                           #
##############################################

# PROCEDIMIENTOS DE INSTALACION DE LIBRERIAS REQUIRIDAS
# Para Windows
# INSTALAR LA LIBRERIA DE pandas,seaborn,matplotlib
# Para pandas: pip install pandas
# Para pandas: pip install seaborn 
# Para pandas: pip install matplotlib 


#importar Libreria
import os
import csv
import pandas
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from csv import reader


#Definicion de Valriables
BDReclamos ='Reclamos.csv'
BDInventario ='Inventario.csv'
Authentication ='admin'
BreakBucle = 0
SeleccionMenuPrincipal = 0
SeleccionMenuInventario = 0
SeleccionMenuVenta= 0
SeleccionMenuReporte = 0
SeleccionMenuReclamos = 0
BreakBucle = 0
NombredelProducto = str
CodigodelProducto = str
PrecioProducto = 0
CantidadDisponible = 0
NombreCliente = str
CedulaCliente = 0
TelefonoCliente	= 0
DireccionCliente = str
DesceuntoProducto = 0
TotalReclamos = 0
DescripcionReclamo = str
TotalPrecioProducto = 0

NombreCliente = str
CedulaCliente = int
TelefonoCliente = int
DireccionCliente = str
cantidad_unidad = int
codigo_producto = str
precio_producto = int
descripcion_producto = str
iva = int
total_pagar = int
productos = {}
total = int
subtotal = 0



#Texto Menus del sistem, Estos son Generados por Linea de exto lo cual se agrega multiples lineas con ''' y cerrando con '''
txtMenuPrincipal='''

** SISTEMA DE PYMES PARA VENTA DE CANFER ELECTRONICA **

******************************************************************                                                                
*          *****Selecione el Modulo segun requiera*****          *         
******************************************************************
*                                                                *                                                                
*                1. Modulo Inventario                            * 
*                2. Modulo Ventas y Facturacion                  *
*                3. Generar Reportes Generales                   *
*                4. Sistemna de Reclamos                         *
*                        0. Salir                                *
*                                                                *
******************************************************************
'''
txtMenuPrincipalInventario='''
****************************************************************************************
*                               *****MENU INVENTARIO*****                              *
****************************************************************************************
*                                                                                      *
*       1.  Ver invetario ------------------ 0. Salir a menu principal                 *
*       2.  Producto Nuevo                                                             *
*       3.  Modificar Producto                                                         *
*       5.  Buscar Producto por Código                                                 *
*       6.  Filtrar Producto por Nombre                                                *
*       7.  Ingresar Producto                                                          *
*                                                                                      *
****************************************************************************************
'''
txtMenuPrincipalVenta = '''
******************************************************************                                                               
*              *****Modulo de Venta de Producto*****             *
******************************************************************
*                                                                *                                                               
*                   1. Facturacion                               *
*                   2. Inventario Disponible                     *
*                   0. Salir al Menu Principal                   *
*                                                                *
******************************************************************
'''
txtMenuPrincipalReporte = '''
******************************************************************                                                                
*        *****Modulo de Reportes Generales de Sistema*****       *
****************************************************************** 
*                                                                *                                                               
*            1. Promedio de ventas en general                    *
*            2. Promedio de ventas por cada producto             *
*            3. Venta más alta realizada                         *
*            4. Productos Agotados                               *
*            5. Productos disponibles                            *
*            0. Salir al Menu Principal                          *
*                                                                *
******************************************************************
'''
txtMenuPrincipalReclamos = '''
******************************************************************                                                                
*            *****Modulo de Reclamos de Sistema*****             *      
******************************************************************           
*                                                                *
*               1. Crear Reporte de Reclamo de Cliente           *
*               2. Consultar Reclamo Existente                   *
*               0. Salir al Menu Principal                       *
*                                                                *
******************************************************************
'''

#Declaracion de Funciones:

def LimpiarTerminal():
    commando = 'clear'
    if os.name in ('nt', 'dos'): 
        commando = 'cls'
    os.system(commando)

def PromedioMensual():
    resul=[]
    temp=0
    TotalVentas=0
    datos=pd.read_csv('ReportFacturas.csv',header=0,index_col=0)
    print(f'\nSistema de reporte promedio anual general de las ventas realizadas:')
    print(datos['Total_Compra'])
    with open('ReportFacturas.csv') as File:  
        reader = csv.DictReader(File)
        for row in reader:
            temp= row['Total_Compra']
            resul.append(temp)

    for a in resul:
        TotalVentas+=int(a)
    input(f'\nPromedio de Ventas Anual General es: ₡{int(TotalVentas/12)} \nPrecione una tecla para continuar...')

def SalidaProductoBDDVenta(codigo,cantidad_unidades):
    result=[]
    egresos=cantidad_unidades
    with open(BDInventario)as File:
        reader=csv.DictReader(File)
        for row in reader:
            if row['codigo']==codigo:
                row['codigo']=row['codigo']
                row['ubicacion']=row['ubicacion']
                row['descripcion']=row['descripcion']
                row['unidad']=row['unidad']
                row['stock_minimo']=row['stock_minimo']
                row['cantidad_inicial']=row['cantidad_inicial']
                row['ingresos']=row['ingresos']
                verificar=int(str(row['egresos']))
                temp=int(str(egresos))
                total_egresos=0
                if verificar>0:
                    total_egresos=verificar+temp
                    temp1=str(total_egresos)
                    row['egresos']=temp1
                else:
                    row['egresos']=egresos
                row['perdidas']=row['perdidas']
                a=int(str(row['cantidad_inicial']))
                b=int(str(row['ingresos']))
                c=int(str(row['egresos']))
                d=int(str(row['perdidas']))
                operacion=(a+b)-(c+d)
                total=int(str(operacion))
                stock=int(str(row['stock_minimo']))
                if total <= stock:
                    temp=str(total)
                    observaciones="Solicitar Material"
                    row['total']=temp
                    row['observaciones']=observaciones
                else:
                    observaciones="Stok a favor"
                    row['total']=total
                    row['observaciones']=observaciones
                row['observacion_perdida']=row['observacion_perdida']
                row['precio_unidad']=row['precio_unidad']
            result.append(row)    
    with open(BDInventario,'w')as File:
        fieldnames=['codigo','ubicacion','descripcion','unidad','stock_minimo','cantidad_inicial','ingresos','egresos','perdidas','total','observaciones','observacion_perdida','precio_unidad']
        writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
        writer.writeheader()
        writer.writerows(result)


def ModuloVenta():
    global BreakBucle, add_more, subtotal
    CantProducto=[]
    while True:
        add_more=""
        LimpiarTerminal()
        print(txtMenuPrincipalVenta)
        SeleccionMenuVenta =  input('Ingrese la accion a realizar: ')
        if (SeleccionMenuVenta == '0'):
            break
        elif (SeleccionMenuVenta == '1'):
            while BreakBucle==0:
                LimpiarTerminal()#lIMPIA LA CONSOLA 
                print('Facturacion Cliente Final, llenar los datos solicitados')
                FechaVenta = str(input('Ej. DD/MM/AAA \nIngrese Fecha:'))
                NombreCliente = str(input('\nNombre de Cliente:\n'))
                CedulaCliente = int(input('\nCedula Fisica/Juridica:\n'))
                TelefonoCliente = int(input('\nNumero de Telefono:\n'))
                DireccionCliente = str(input('\nDirrecion de Cliente:\n'))
                BreakBucle = int(input('Los datos Ingresados con correctos? \n1.SI - 0.Modificar Datos \nIngrese Seleccion: '))
            while add_more!='0':
                codigo=input('Codigo de producto a agregar: ')
                if ExisteCodigo(codigo)=="No existe":
                    input('---- Error el codigo que desea agregar no existe ----')
                else:
                    with open(BDInventario,'r') as File:
                        reader=csv.DictReader(File, delimiter=",")
                        for row in reader:
                            if row['codigo']==codigo:
                                cantidad_unidades = int(input('Cantidad: '))
                                codigo_producto = str(row['codigo'])
                                precio_producto = int(row['precio_unidad'])
                                descripcion_producto = str(row['descripcion'])
                                print(f'\nProducto {descripcion_producto}, Catidad: {cantidad_unidades},Precio por Unidad {precio_producto} Agregado\n')
                                add_more = str(input('Precione Enter para Agregar mas Producto o Precione 0 para finalizar: '))
                                productos[descripcion_producto] = [codigo_producto,descripcion_producto, cantidad_unidades, precio_producto, cantidad_unidades*precio_producto]
                                SalidaProductoBDDVenta(codigo,cantidad_unidades)
                                if add_more == "0":
                                    for i in productos.keys():
                                        subtotal += cantidad_unidades * productos[i][3]
                                        CantProducto.append(str(productos[i][2]))
                                    
            iva = subtotal * 0.13
            total = int(subtotal+iva)                        
            print(f'\n\nEstimad@ {NombreCliente} a continuacion se le adjunta detalle de la factura: \n')
            print("Productos: ", list(productos.keys()))
            ListProducto = list(productos.keys())
            ContProducto = list(CantProducto)
            print(f'Sub Total: {subtotal}\nIVA: {iva}\nPrecio total a pagar: {total}')
            input('\nPrecione una tecla para Finalizar y vovler al menu...')
            with open ('ReportFacturas.csv','a')as File:
                File.write('\n'+str(FechaVenta)+','+str(NombreCliente)+','+str(CedulaCliente) +','+str(TelefonoCliente)+','+str(DireccionCliente)+','+str(ListProducto)+','+str(ContProducto)+','+str(total))
        elif (SeleccionMenuVenta == '2'):
            ReporteInventarioTotal()

def ModuloReporte():
     while True: 
            LimpiarTerminal()
            print(txtMenuPrincipalReporte)
            SeleccionMenuReporte =  input('Ingrese la accion a realizar: ')
            if (SeleccionMenuReporte == '0'):
                break
            elif (SeleccionMenuReporte == '1'):
                PromedioMensual()
            elif (SeleccionMenuReporte == '2'):
                input('Promedio de Venta Por Producto')
            elif (SeleccionMenuReporte == '3'):
                input('Venta mas Alta Realizada')
            elif (SeleccionMenuReporte == '4'):
                ReporteStockMinimo()
            elif (SeleccionMenuReporte == '5'):
                ReporteInventarioTotal()

def ModuloReclamo():
    while True:
            global BreakBucle
            LimpiarTerminal()
            print(txtMenuPrincipalReclamos)
            SeleccionMenuReclamos =  input('Ingrese la accion a realizar: ')
            if (SeleccionMenuReclamos == '0'):
                break
            elif (SeleccionMenuReclamos == '1'):
                while BreakBucle == 0:
                    LimpiarTerminal() 
                    print('Modulo de reclamos, llenar los datos solicitados del cliente.')
                    NuevoReclamo()
                    BreakBucle = int(input('Los datos Ingresados con correctos? \n1.SI - 0.Modificar Datos \nIngrese Seleccion: '))
                while BreakBucle == 0:
                    LimpiarTerminal()
                    DescripcionReclamo =str(input('Acontinuacion agrege el reclamo que desea solicitar: '))
                    BreakBucle = int(input('Los datos Ingresados con correctos? \n1.SI - 0.Modificar Datos \nIngrese Seleccion: '))
                BreakBucle=0
            elif (SeleccionMenuReclamos == '2'):
                LimpiarTerminal()
                print('**** SISTEMA CONSULTA RECLAMO ****\n\nSe Muestra a continuacion los Reclamos generados por el sistema hasta la fecha de Hoy.\nPrecione tecla al finalizar para terminar la consulta y volver al menu principal\n')
                VerReclamos()
                input()

def NuevoReclamo():
    codigo = input('Ingrese codigo de reclamo: ')
    numero_cedula = input('Ingrese Numero de Cedula del Cliente: ')
    nombre_cliente = input('Ingrese Nombre de Cliente: ')
    descripcion_reclamo = input('Ingrese descripcion del reclamo: ')
    fecha_compra = input('Ingese fecha de compra: ')
    with open (BDReclamos,'a')as File:
        File.write('\n'+codigo+','+numero_cedula +','+nombre_cliente+','
        +descripcion_reclamo+','+fecha_compra)
    
def VerReclamos():
    dx=pd.read_csv(r'Reclamos.csv',index_col=0)
    print(dx)
    print('\nPrecione una tecla para continuar...')

def ExisteCodigo(codigo): 
    with open(BDInventario,encoding ='latin-1')as File:
        reader = csv.DictReader(File)
        for row in reader:
            if(codigo == row['codigo']):
                return row
        return "No existe"

def VerInventario():
    df=pd.read_csv(r'Inventario.csv',index_col=0)
    print(df)

def ProductoNuevo():
    codigo = input('Ingrese codigo de producto nuevo: ')
    if ExisteCodigo(codigo)=="No existe":
        ubicacion=input('Ingrese ubicación: ')
        descripcion=input('Ingrese descripción: ')
        unidad=input('Ingrese unidad de medida: ')
        stock_minimo=input('Ingese stock minimo: ')
        cantidad_inicial=input('Ingrese cantidad inicial: ')
        ingresos="0"
        egresos="0"
        perdidas="0"
        total="0"
        precio_unidad=input('Ingrese el precio de venta: ₡')
        observaciones="NINGUNO"
        observaciones_perdida="NINGUNO"
        with open (BDInventario,'a')as File:
            File.write('\n'+codigo+','+ubicacion+','+descripcion+','+unidad+','+stock_minimo+','+cantidad_inicial+','+ingresos+','+egresos+','+perdidas+','+total+','+observaciones+','+observaciones_perdida+','+precio_unidad)
    else:
        print("****Error el codigo ya existe****")

def ModificarProducto(): 
    codigo=input('Ingrese codigo modificar: ')
    if ExisteCodigo(codigo)=="No existe":
        input('----Error el codigo que desea modificar no existe----')
    
    else:
        ubicacion=input('Ingrese ubicacion: ')
        descripcion=input('Ingrese descripción: ')
        unidad=input('Ingrese unidad: ')
        modificarBDD(codigo,ubicacion,descripcion,unidad)

def modificarBDD(codigo,ubicacion,descripcion,unidad,precio_unidad):
    result=[]
    with open(BDInventario)as File:
        reader=csv.DictReader(File)
        for row in reader:
            if row['codigo']==codigo:
                row['codigo']=codigo
                row['ubicacion']=ubicacion
                row['descripcion']=descripcion
                row['unidad']=unidad
                row['stock_minimo']=row['stock_minimo']
                row['cantidad_inicial']=row['cantidad_inicial']
                row['ingresos']=row['ingresos']
                row['egresos']=row['egresos']
                row['perdidas']=row['perdidas']
                a=int(str(row['cantidad_inicial']))
                b=int(str(row['ingresos']))
                c=int(str(row['egresos']))
                d=int(str(row['perdidas']))
                operacion=(a+b)-(c+d)
                total=int(str(operacion))
                stock=int(str(row['stock_minimo']))
                if total <= stock:
                    temp=str(total)
                    observaciones="Solicitar Material"
                    row['total']=temp
                    row['observaciones']=observaciones
                    row['precio_unidad']=precio_unidad
                else:
                    observaciones="Stok a favor"
                    row['total']=total
                row['observaciones']=observaciones
                row['observacion_perdida']=row['observacion_perdida']
            result.append(row)
        
    with open(BDInventario,'w')as File:
        fieldnames=['codigo','ubicacion','descripcion','unidad','stock_minimo','cantidad_inicial','ingresos','egresos','perdidas','total','observaciones','observacion_perdida','precio_unidad']
        writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
        writer.writeheader()
        writer.writerows(result)

def EliminarProducto():
    codigo=input('Ingrese codigo a eliminar: ')
    if ExisteCodigo(codigo)=="No existe":
        input('----Error el codigo que desea eliminar no existe----')
    else:
        eleccion=input('Si esta seguro si=S no=N? ')
        if eleccion=='S' or eleccion=='s':
            EstadoElimandoBDD(codigo) 

def EstadoElimandoBDD(codigo):
    result=[]
    AuthenticationUser = str(input('Ingrese Contraseña Administradora : '))
    if AuthenticationUser  == Authentication:
        with open(BDInventario)as File:
            reader=csv.DictReader(File)
            for row in reader:
                if row['codigo']!=codigo:
                    result.append(row)
        with open(BDInventario,'w')as File:
            fieldnames=['codigo','ubicacion','descripcion','unidad','stock_minimo','cantidad_inicial','ingresos','egresos','perdidas','total','observaciones','observacion_perdida','precio_unidad']
            writer=csv.DictWriter(File,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(result)
    else:
        input('Contraseña Usuario Previligiado no existe----')

def BuscarProducto():
    codigo=input('Ingrese codigo de producto a buscar: ')
    if ExisteCodigo(codigo)=="No existe":
        input('----Error el codigo que desea eliminar no existe----')
    else:
        BuscarBDD(codigo) 

def BuscarBDD(codigo):
    result=[]
    with open(BDInventario)as File:
        reader=csv.DictReader(File)
        for row in reader:
            if row['codigo']==codigo:
                print('' + str(row['codigo'])+'\t' + str(row['ubicacion'])+'\t'+ str(row['descripcion'])+'\t' + str(row['unidad'])+'\t'+'\t' + str(row['stock_minimo'])+'\t' + str(row['cantidad_inicial'])+'\t' + str(row['ingresos'])+'\t' + str(row['egresos'])+'\t' + str(row['perdidas'])+'\t' + str(row['total'])+'\t' + str(row['observaciones'])+'\t' + str(row['observacion_perdida'])+'\t' + str(row['precio_unidad']))
                input('\nPreccione una tecla para continuar...')

def BuscarPorNombre():
    df=pd.read_csv(r'Inventario.csv',index_col=0)
    palabra=str(input('Ingrese el nombre a filtrar: '))
    print(df[df['descripcion'].str.contains(palabra)])
    input('\nPreccione una tecla para continuar...')

def IngresarProducto():
    codigo=input('Ingrese codigo de producto a ingresar: ')
    if ExisteCodigo(codigo)=="No existe":
        input('----Error el codigo que desea eliminar no existe----')
    else:
        IngresarProductoBDD(codigo) 

def IngresarProductoBDD(codigo): 
    result=[]
    print('Datos del producto') 
    BuscarBDD(codigo)
    ingresos=input('Cantidad a ingresar a bodega: ')
    with open(BDInventario,index_col=0)as File:
        reader=csv.DictReader(File)
        for row in reader:
            if row['codigo']==codigo:
                row['codigo']=row['codigo']
                row['ubicacion']=row['ubicacion']
                row['descripcion']=row['descripcion']
                row['unidad']=row['unidad']
                row['stock_minimo']=row['stock_minimo']
                row['cantidad_inicial']=row['cantidad_inicial']
                verificar=int(str(row['ingresos']))
                temp=int(str(ingresos))
                total_ingreso=0
                if verificar>0:
                    total_ingreso=verificar+temp
                    temp1=str(total_ingreso)
                    row['ingresos']=temp1
                else:
                    row['ingresos']=ingresos         
                row['egresos']=row['egresos']
                row['perdidas']=row['perdidas']
                a=int(str(row['cantidad_inicial']))
                b=int(str(row['ingresos']))
                c=int(str(row['egresos']))
                d=int(str(row['perdidas']))
                operacion=(a+b)-(c+d)
                total=int(str(operacion))
                stock=int(str(row['stock_minimo']))
                if total <= stock:
                    temp=str(total)
                    observaciones="Solicitar Material"
                    row['total']=temp
                    row['observaciones']=observaciones
                else:
                    observaciones="Stok a favor"
                    row['total']=total
                    row['observaciones']=observaciones
                row['observacion_perdida']=row['observacion_perdida']
            result.append(row)    
    with open(BDInventario,'w')as File:
        fieldnames=['codigo','ubicacion','descripcion','unidad','stock_minimo','cantidad_inicial','ingresos','egresos','perdidas','total','observaciones','observacion_perdida','precio_unidad']
        writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
        writer.writeheader()
        writer.writerows(result)
    
def SalidaDeProducto():
    codigo=input('Ingrese codigo de producto para darle salida: ')
    if ExisteCodigo(codigo)=="No existe":
        input('----Error el codigo que desea eliminar no existe----')
    else:
        SalidaProductoBDD(codigo) 

def SalidaProductoBDD(codigo):
    result=[]
    print('Datos del producto') 
    BuscarBDD(codigo)
    egresos=input('Cantidad de salida de bodega: ')
    with open(BDInventario)as File:
        reader=csv.DictReader(File)
        for row in reader:
            if row['codigo']==codigo:
                row['codigo']=row['codigo']
                row['ubicacion']=row['ubicacion']
                row['descripcion']=row['descripcion']
                row['unidad']=row['unidad']
                row['stock_minimo']=row['stock_minimo']
                row['cantidad_inicial']=row['cantidad_inicial']
                row['ingresos']=row['ingresos']
                verificar=int(str(row['egresos']))
                temp=int(str(egresos))
                total_egresos=0
                if verificar>0:
                    total_egresos=verificar+temp
                    temp1=str(total_egresos)
                    row['egresos']=temp1
                else:
                    row['egresos']=egresos
                row['perdidas']=row['perdidas']
                a=int(str(row['cantidad_inicial']))
                b=int(str(row['ingresos']))
                c=int(str(row['egresos']))
                d=int(str(row['perdidas']))
                operacion=(a+b)-(c+d)
                total=int(str(operacion))
                stock=int(str(row['stock_minimo']))
                if total <= stock:
                    temp=str(total)
                    observaciones="Solicitar Material"
                    row['total']=temp
                    row['observaciones']=observaciones
                else:
                    observaciones="Stok a favor"
                    row['total']=total
                    row['observaciones']=observaciones
                row['observacion_perdida']=row['observacion_perdida']
                row['precio_unidad']=row['precio_unidad']
            result.append(row)    
    with open(BDInventario,'w')as File:
        fieldnames=['codigo','ubicacion','descripcion','unidad','stock_minimo','cantidad_inicial','ingresos','egresos','perdidas','total','observaciones','observacion_perdida','precio_unidad']
        writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
        writer.writeheader()
        writer.writerows(result)

def ReporteStockMinimo():
    df=pd.read_csv(r'Inventario.csv',index_col=0)
    print(df[df['observaciones'].str.contains("Solicitar Material")])
    input('\nPrecione Una Tecla Para Continuar...')

def ReporteInventarioTotal():
    df=pd.read_csv(r'Inventario.csv',index_col=0)
    ord=df.sort_values(by=['descripcion','precio_unidad'])[['descripcion','precio_unidad']]
    print(ord)
    input('\nPrecione Una Tecla Para Continuar...')

def ReporteParcialStock():
    df=pd.read_csv(r'Inventario.csv',index_col=0, encoding='latin-1',engine='python')
    print(df[df['observaciones'].str.contains("Stok a favor")])
    input('\nPrecione Una Tecla Para Continuar...')

def RellenarEspacios():
    codigo=input('Ingrese codigo de producto a rellenar: ')
    if ExisteCodigo(codigo)=="No existe":
        input('----Error el codigo que desea eliminar no existe----')
    else:
        RellenarEspaciosBDD(codigo) 

def RellenarEspaciosBDD(codigo):
    result=[]
    with open(BDInventario,index_col=0)as File:
        reader=csv.DictReader(File)
        ubicacion="Vacio"
        descripcion="Vacio"
        unidad="Vacio"
        stock_minimo="0"
        cantidad_inicial="0"
        ingresos="0"
        egresos="0"
        perdidas="0"
        total="0"
        observaciones="Vacio"
        observaciones_perdida="Vacio"
        for row in reader:
            #Compara el codigo hasta encontrar lugar vacio
            if row['codigo']==codigo:
                row['codigo']=row['codigo']
                if row['ubicacion'] =="":
                    row['ubicacion']=ubicacion
                else:
                    row['ubicacion']=row['ubicacion']
                if row['descripcion']=="":
                    row['descripcion']=descripcion
                else:
                    row['descripcion']=row['descripcion']
                if row['unidad']=="":
                    row['unidad']=unidad
                else:
                    row['unidad']=row['unidad']
                if row['stock_minimo']=="":
                    row['stock_minimo']=stock_minimo
                else:
                    row['stock_minimo']=row['stock_minimo']
                if row['cantidad_inicial']=="":
                    row['cantidad_inicial']=cantidad_inicial
                else:
                    row['cantidad_inicial']=row['cantidad_inicial']
                if row['ingresos']=="":
                    row['ingresos']=ingresos
                else: 
                    row['ingresos']
                if row['egresos']=="":
                    row['egresos']=egresos
                else:
                    row['egresos']=row['egresos']
                if row['perdidas']=="":
                    row['perdidas']=perdidas
                else: 
                    row['perdidas']=row['perdidas']
                if row['total']=="":
                    row['total']=total
                else:
                    row['total']=row['total']
                if row['observaciones']=="":
                    row['observaciones']=observaciones
                else:
                    row['observaciones']=row['observaciones']
                if row['observacion_perdida']=="":
                    row['observacion_perdida']=observaciones_perdida
                else: 
                    row['observacion_perdida']=row['observacion_perdida']
            result.append(row)
        
    with open(BDInventario,'w',index_col=0)as File:
        fieldnames=['codigo','ubicacion','descripcion','unidad','stock_minimo','cantidad_inicial','ingresos','egresos','perdidas','total','observaciones','observacion_perdida']
        writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
        writer.writeheader()
        writer.writerows(result)

while True: 
    LimpiarTerminal()
    print(txtMenuPrincipal)
    SeleccionMenuPrincipal =  input('Introduzca el número de la opción deseada: ')
    if (SeleccionMenuPrincipal == '0'):
        LimpiarTerminal()
        break 
    elif (SeleccionMenuPrincipal == '1'):
        while True:
            LimpiarTerminal()
            print(txtMenuPrincipalInventario)
            option = input('Introduzca el número de la opción deseada: ')
            if option == '0':
                break
            elif option == '1':
                LimpiarTerminal()
                VerInventario()
                input('Precione una tecla para volver al menu anterior')
            elif option == '2':
                LimpiarTerminal()
                ProductoNuevo()
            elif option == '3':
                LimpiarTerminal()
                ModificarProducto()
            elif option == '4':
                LimpiarTerminal()
                EliminarProducto()
            elif option == '5':
                LimpiarTerminal()
                BuscarProducto()
            elif option == '6':
                LimpiarTerminal()
                BuscarPorNombre()
            elif option == '7':
                LimpiarTerminal()
                IngresarProducto()
    elif (SeleccionMenuPrincipal == '2'): 
        ModuloVenta()
    elif (SeleccionMenuPrincipal == '3'):
        ModuloReporte()
    elif (SeleccionMenuPrincipal == '4'): 
        ModuloReclamo()
    else: 
        input('ERROR EN SELECIONAR LA OPCIONES DEL MODULO VUELVE A INTENTARLO \n \nPrecione una tecla para continuar....')
