from datetime import datetime
import pytz 

#Hay base de datos para cualquier zona horarioa

bogota_tz = pytz.timezone("America/Bogota")
bogota = datetime.now(bogota_tz)
print(f"Bogota: {bogota.strftime('%d/%m/%Y, %H:%M:%S')}")

mexico_tz = pytz.timezone("America/Mexico_City")
mexico = datetime.now(mexico_tz)
print(f"Mexico: {mexico.strftime('%d/%m/%Y, %H:%M:%S')}")

caracas_tz = pytz.timezone("America/Caracas")
caracas = datetime.now(caracas_tz)
print(f"Caracas: {caracas.strftime('%d/%m/%Y, %H:%M:%S')}")

