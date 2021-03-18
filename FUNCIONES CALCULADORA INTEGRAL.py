import os

def Sueldo_Basico_Dias_Asistidos(float,int):
  # USUARIO INGRESA OPERACION COMPLETA PARA SABER SUELDO BASICO POR DIAS ASISTIDOS , BONO NOCTURNO POR DIAS ASISTIDOS , HORAS EXTRAS ASISTIDAS
  Sueldo_Basico_Flotante = ((float(input("INGRESE SUELDO BASICO DEL MERCADO ACTUAL"))))
  Sueldo_Basico_Entero = (((int(input("INGRESE DIAS ASISTIDOS")))))
  Flotante_Sueldo_Basico = float(Sueldo_Basico_Flotante)
  Entero_Sueldo_Basico = int(Sueldo_Basico_Entero)
  Operacion_Sueldo_Basico_Dias_Asistidos = (Flotante_Sueldo_Basico /30) * Entero_Sueldo_Basico
  # USUARIO INGRESA OPERACION COMPLETA PARA SABER BONO NOCTURNO POR DIAS ASISTIDOS
  Sueldo_Bono_Nocturno_Dias_Asistidos = (((int(input("INGRESE DIAS BONO NOCTURNO ASISTIDOS")))))
  Operacion_Bono_Nocturno_Dias_Asistidos = (Sueldo_Basico_Flotante * 30 / 100 /30) *  Entero_Sueldo_Basico
  Entero_Bono_Nocturno = int(Sueldo_Bono_Nocturno_Dias_Asistidos)
  # USUARIO INGRESA OPERACION COMPLETA PARA SABER HORAS EXTRAS ASISTIDAS
  Sueldo_Horas_Extras_Asistidas = (((int(input("INGRESE HORAS EXTRAS ASISTIDAS")))))
  Entero_Sueldo_Horas_Extras = int(Sueldo_Horas_Extras_Asistidas)
  Operacion_Horas_Extras_Asistidas = (Sueldo_Basico_Flotante /30 /12) * Sueldo_Horas_Extras_Asistidas
  # USUARIO INGRESA OPERACION COMPLETA PARA SABER SUELDO BASICO CESTA TIKET POR DIAS ASISTIDOS
  Sueldo_Basico_Cesta_Tiket = (((float(input("INGRESE SUELDO BASICO CESTA TIKET DEL MERCADO ACTUAL")))) / 30)
  Sueldo_Basico_Cesta_Tiket_Dias_Asistidos = (((int(input("INGRESE DIAS ASISTIDOS")))))
  Operacion_Sueldo_Basico_Cesta_Tiket_Dias_Asistidos = Sueldo_Basico_Cesta_Tiket  * Sueldo_Basico_Cesta_Tiket_Dias_Asistidos
  Entero_Sueldo_Basico_Cesta_Tiket = int(Sueldo_Basico_Cesta_Tiket_Dias_Asistidos)
  # ESTA OPERACION ES LA SUMA FINAL DE TODOS LOS VALORES ANTERIORES
  Suma_Sueldo_Basico_Final = Operacion_Sueldo_Basico_Dias_Asistidos + Operacion_Bono_Nocturno_Dias_Asistidos + Operacion_Horas_Extras_Asistidas + Operacion_Sueldo_Basico_Cesta_Tiket_Dias_Asistidos
  if Entero_Sueldo_Basico >=0 and Entero_Bono_Nocturno and Entero_Sueldo_Horas_Extras >=0 and Entero_Sueldo_Basico_Cesta_Tiket >=0:
    if Entero_Sueldo_Basico <=35 and Entero_Bono_Nocturno <=35 and Entero_Sueldo_Horas_Extras <=110 and Entero_Sueldo_Basico_Cesta_Tiket <=31:
      return print("SUELDO BASICO POR DIAS ASISTIDOS ES {}".format(int(Operacion_Sueldo_Basico_Dias_Asistidos))) , print("BONO NOCTURNO POR DIAS ASISTIDOS ES {}".format(int(Operacion_Bono_Nocturno_Dias_Asistidos))) , print("HORAS EXTRAS ASISTIDAS ES {}".format(float(Operacion_Horas_Extras_Asistidas))) , print("SUELDO BASICO CESTA TIKET POR DIAS ASISTIDOS ES {}".format(int(Operacion_Sueldo_Basico_Cesta_Tiket_Dias_Asistidos))) , print("SUELDO BASICO FINAL ES {}".format(int(Suma_Sueldo_Basico_Final))) 
    else :
      return print("NUMERO DIAS ASISTIDOS SOLO PUEDEN SER DIGITOS DEL 0 AL 35 Y CESTA TIKET DEBEN SER NUMERO DEL MES") , print("Y BONO NOCTURNO UN VALOR MAXIMO DE 110 HORAS")
  else :
    return print("NUMERO DIAS ASISTIDOS NO PUEDEN SER NUMEROS NEGATIVOS")



Sueldo_Basico_Dias_Asistidos(float,int)

os.system("pause")