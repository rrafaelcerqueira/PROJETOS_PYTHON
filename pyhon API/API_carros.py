import requests

def mostrar_personagens_carros():
    url = "https://api.disneyapi.dev/character"
    
    print("Buscando personagens de 'Cars'... Isso pode levar alguns segundos.\n")
    
    while url:
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            personagens = data.get('data', [])
            
            if isinstance(personagens, list):
                for p in personagens:
                    if any("Cars" in filme for filme in p.get('films', [])):
                        print(f"🚗 Nome: {p['name']}")
                        print(f"🎬 Filmes: {', '.join(p['films'])}")
                        print(f"🔗 Imagem: {p.get('imageUrl', 'Sem imagem')}")
                        print("-" * 30)
                        
            url = data.get('info', {}).get('nextPage')
            
        except requests.exceptions.RequestException as e:
            print(f"Erro ao conectar: {e}")
            break

if __name__ == "__main__":
    mostrar_personagens_carros()
