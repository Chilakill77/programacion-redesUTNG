#Kevin
#Esta api te da el codigo html de la pagina que quieras
#ingresa la url de la pagina de la que quieras obtener su codigo html
import requests

def scrape_url(url):
    payload = {
        'api_key': '39214a8ad53530a95d94f6dcc20ed530',
        'url': url,
        'follow_redirect': False,
        'autoparse': True,
        'country_code': 'us',
        'device_type': 'desktop',
        'session_number': 1
    }

    response = requests.get('https://api.scraperapi.com/', params=payload)
    return response.text

if __name__ == "__main__":
    while True:
        # Pedir al usuario que ingrese la URL
        user_input = input("Ingresa la URL que deseas hacer scraping (o escribe 'salir' para salir): ")

        # Verificar si el usuario quiere salir
        if user_input.lower() == 'salir':
            print("Saliendo...")
            break

        # Realizar scraping con la URL proporcionada por el usuario
        scraped_data = scrape_url(user_input)

        print("Datos raspados:")
        print(scraped_data)
