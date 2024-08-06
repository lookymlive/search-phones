import requests
import phonenumbers
from phonenumbers import geocoder, carrier

def obtener_informacion_telefono(numero_telefono):
    try:
        # Parsear el número de teléfono
        numero = phonenumbers.parse(numero_telefono, "AR")  # Cambia "US" al código de tu país si es necesario

        # Obtener la ubicación geográfica del número
        ubicacion = geocoder.description_for_number(numero, "es")
        # Obtener el proveedor de servicios del número
        proveedor = carrier.name_for_number(numero, "es")

        print(f"Información del número {numero_telefono}:")
        print(f"Ubicación: {ubicacion}")
        print(f"Proveedor: {proveedor}")

        # Aquí puedes agregar más lógica para obtener información de otras APIs
        # Ejemplo: usar alguna API de validación de teléfonos
        # response = requests.get("URL_DE_API", params={"numero": numero_telefono})
        # data = response.json()
        # print(data)

    except Exception as e:
        print(f"Error al procesar el número de teléfono: {e}")

# Ejemplo de uso
obtener_informacion_telefono("+5493412737492")
