class Cuenta:
    def __init__(self):
        self.cuenta = 0.00

    def registrarIngreso(self,ingreso):
        self.cuenta+=ingreso
        print(f"\nSe ingresaron ${ingreso:.2f}.")
        print(f"\nEn su cuenta tiene ${self.cuenta:.2f}.")

    def registrarEgreso(self,egreso):
        self.cuenta-=egreso
        print(f"\nSe retiraron  ${egreso:.2f}.")
        print(f"\nEn su cuenta tiene ${self.cuenta:.2f}.")


class Ingreso:
    
    def __init__(self):
        self.ingreso = 0.00

    def Aingresos(self,montoI):
        self.ingreso += montoI
        return montoI



class Egreso:
    def __init__(self):
        self.egreso = 0.00

    def Aegresos(self,montoE):
        self.egreso -= montoE
        return montoE
       
CuentaP= Cuenta()
RegistrarI = Ingreso()
RegistrarE= Egreso()
while True:
    Menu = """\n¡Bienvenido a tu sistema de finanzas personas! Elige una opción:
    1-Registrar ingreso
    2-Registrar egreso
    3-Reporte de ingresos
    4-Reporte de egresos
    5-Reporte de transacciones
    6-Saldo de la cuenta
    7-Salir\n"""
    print(Menu)
    opcion = int(input("\n¿Qué opción eliges? "))
  
    if opcion==1:
        print("-"*100)
        ingreso = round(float(input("\n¿Qué monto quiere ingresar a la cuenta? ")),2)
        CuentaP.registrarIngreso(RegistrarI.Aingresos(ingreso))
        print("-"*100)
    elif opcion==2:
        print("-"*100)
        egreso = round(float(input("¿Qué monto quiere retirar? ")),2)
        CuentaP.registrarIngreso(RegistrarI.Aengresos(egreso))
        print("-"*100)
    elif opcion==3:
        IngresosT = RegistrarI.ingreso
        print("-"*100)
        print(f"Has ingresado ${IngresosT:.2f}")
        print("-"*100)
    elif opcion==4:
        EgresosT = RegistrarI.egreso
        print("-"*100)
        print(f"Has retirado ${EgresosT:.2f}")
        print("-"*100)
    elif opcion==5:
        ReporteIngresos = RegistrarI. ingreso
        ReporteEgresos = RegistrarE. egreso
        print("-"*100)
        Reportemsg = f"""Reporte de transacciones:
        Ingresos Totales: ${ReporteIngresos:.2f}
        Egresos Totales: ${ReporteEgresos:.2f}."""
        print(Reportemsg)
        print("-"*100)
    elif opcion==6:
        print("-"*100)
        saldo = CuentaP.cuenta
        print(f"Tu saldo disponible es de  ${saldo:.2f}.")
        print("-"*100)
    elif opcion == 7:
        print("Gracias por confiarnos tus finanzas. Te esperamos pronto")
        break
