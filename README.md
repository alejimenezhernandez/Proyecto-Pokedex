# Proyecto-Pokedex
# Pokédex Este proyecto es una aplicación que permite obtener información sobre cualquier Pokémon utilizando la API de PokeAPI y guardar dicha información

obtener_datos_pokemon(nombre_pokemon):

Realiza una solicitud a la API de PokeAPI para obtener información sobre el Pokémon especificado.

Retorna un diccionario con los datos del Pokémon si la solicitud es exitosa.

guardar_datos_pokemon(pokemon):

Guarda los datos del Pokémon en un archivo JSON dentro de la carpeta pokedex.

Crea la carpeta pokedex si no existe.

main():

Solicita al usuario el nombre del Pokémon.

Llama a la función obtener_datos_pokemon y muestra la información obtenida.

Guarda la información en un archivo JSON si el Pokémon existe.
