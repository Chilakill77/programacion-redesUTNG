#Kevin
#INGRESa un valor por ejemplo, HP (HPQ), Groupon Inc. (GRPN), IBM (IBM) 
#para obtener su cotizacion en la bolsa Segun el dia
import requests
api_key = "TGFSI2VP3ZL0SVZB"

while True:
    symbol = input("Ingrese el símbolo de la acción que desea consultar (o 'exit' para salir): ")
    if symbol.lower() == 'exit':
        print("Saliendo del programa.")
        break 
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
    print(f"URL de la solicitud: {url}")
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        print(data)
    else:
        print(f"Error en la solicitud. Código de estado: {r.status_code}")
        print(r.text)
