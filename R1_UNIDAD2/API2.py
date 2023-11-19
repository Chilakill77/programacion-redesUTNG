#Kevin
#Esta api te da una lista de diferentes razas de gatos
#cada raza tiene un id, ingresa el id de la raza que tu quieres para 
#optener una imagen de ese gato e informacion de la raza
#Ejemplo: 54.-Siames


import requests

url = "https://api.thecatapi.com/v1/breeds"
api_key = "live_mboWMOWw8NEqPH1Nou9vOKa84bmjoKwDVNmOCJvdFTDbfZsekpmVPmAew4N9FqAU"
stored_breeds = []

def show_breed_info(index):
    if 0 <= index < len(stored_breeds):
        breed = stored_breeds[index]
        print(f"Breed Image: {breed['image']['url']}")
        print(f"Temperament: {breed.get('temperament')}")
        print(f"Wikipedia Link: {breed.get('wikipedia_url')}")
    else:
        print("Invalid index")

response = requests.get(url, headers={'x-api-key': api_key})

if response.ok:
    data = response.json()
    
    stored_breeds = [breed for breed in data if breed.get("image", {}).get("url")]

    breed_options = {}
    for i, breed in enumerate(stored_breeds):
        option_value = str(i)
        option_text = breed["name"]
        breed_options[option_value] = i  
        print(f"{option_value}: {option_text}")

    while True:
        user_input = input("Enter the number of the breed you want to see (or 'salir' to exit): ")
        
        if user_input.lower() == "salir":
            print("Goodbye!")
            break

        if user_input in breed_options:
            selected_index = breed_options[user_input]
            show_breed_info(selected_index)
        else:
            print("Invalid input. Please enter a valid breed number or 'salir'.")
else:
    print(f"Error fetching breeds: {response.status_code}")
