
import requests
import json
import os

def obtener_datos_pokemon(nombre_pokemon):
    try:
    #Hacer la solicitud a la API
        url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
        respuesta = requests.get(url)
        respuesta.raise_for_status() #Levanta la exepción si la solicitud fue incorrecta

    #Verificar si la solicitud es exitosa y extraer datos
        datos = respuesta.json()
        pokemon = {
            "nombre" : datos["name"],
            "peso" : datos["weight"],
            "tamaño" : datos["height"],
            "movimientos" : [movimiento["move"]["name"] for movimiento in datos["moves"]],
            "habilidades" : [habilidad["ability"]["name"] for habilidad in datos["abilities"]],
            "tipos" : [tipo["type"]["name"] for tipo in datos["types"]],
            "imagen" : datos["sprites"]["front_default"]
        }
        return pokemon
    except requests.RequestException as e:
        print(f"Error al obetener datos del Pokémon: {e}") #Manejo de Errores
        return None

#Función para guardar los datos del Pokémon
def guardar_datos_pokemon(pokemon):
    #Crear la carpeta 'pokedex' si no existe
    if not os.path.exists("pokedex"):
        os.makedirs("pokedex")

    #Guardar los datos del Pokémon en un archivo JSON dentro de la carpeta
    with open(f'pokedex/{pokemon["nombre"]}.json', "w") as archivo:
        json.dump(pokemon,archivo,indent=4)

def main():
    #Solicitar al usuario el nombre del Pokémon
    nombre_pokemon = input("Introduce el nombre del Pokemon: ")
    #Obtener los datos del Pokémon
    pokemon = obtener_datos_pokemon(nombre_pokemon)

    if pokemon: 
        #Imprimir los datos Obtenidos
        print(f'Nombre: {pokemon["nombre"]}') 
        print(f'Peso: {pokemon["peso"]} hectogramos') 
        print(f'Tamaño: {pokemon["tamaño"]} decímetros') 
        print(f'Movimientos: {", ".join(pokemon["movimientos"][:5])} (y más)') 
        print(f'Habilidades: {", ".join(pokemon["habilidades"])}') 
        print(f'Tipos: {", ".join(pokemon["tipos"])}') 
        print(f'Imagen: {pokemon["imagen"]}')

        #Guardar los datos del Pokémon
        guardar_datos_pokemon(pokemon)
    else:
        print("El Pokémon no existe. Prueba con otro nombre")

if __name__ == "__main__":
    main()

        guardar_datos_pokemon(pokemon)
    else:
        print("El Pokémon no existe. Prueba con otro nombre")

if __name__ == "__main__":
    main()

       
