"""
/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
 */
"""
import requests
response = requests.get("https://pokeapi.co/api/v2/pokemon/1")
if response.status_code == 200:
    print(response.text)
else:
    print(f"Error en la petición {response.status_code}")

#Extra
def get_pokemon_info(pokemon):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    if response.status_code == 200:
        data = response.json()
        print(f"Nombre: {data['name']}")

#get_pokemon_info("Palkia")
pokemon = input("Ingrese el nombre o número del Pokémon: ")

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
if response.status_code == 200:
    data = response.json()
    print(f"Nombre: {data['name']}")
    print(f"Id: {data['id']}")
    print(f"Peso: {data['weight']}")
    print(f"Altura: {data['height']}")
    for type in data['types']:
        print(f"Tipo: {type['type']['name']}")
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")
    if response.status_code == 200:
        url = response.json()["evolution_chain"]["url"]
        response = requests.get(url)
        if response.status_code == 200: 
            data = response.json()
            print("Evoluciones:")
            print(f"Nombre: {data['chain']['species']['name']}")
            
            
            def get_evolution_chain(data):
                print(f"Nombre: {data['species']['name']}")
                if "evolves_to" in data:
                    for evolution in data["evolves_to"]:
                        get_evolution_chain(evolution)
            get_evolution_chain(data['chain'])
        else:
            print(f"Error en la petición {response.status_code}")

    else:
        print(f"Error en la petición {response.status_code}")
    print("Juegos:")
    response_games = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    data_games = response_games.json()
    if response_games.status_code == 200:
        for game in data_games['game_indices']:
            print(game['version']['name'])
else:
    print(f"Error en la petición {response.status_code}")


