import requests

def mostrar_personagens_carros():
    # URL inicial da API (listagem geral de personagens)
    url = "https://api.disneyapi.dev/character"
    
    print("Buscando personagens de 'Cars'... Isso pode levar alguns segundos.\n")
    
    while url:
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            personagens = data.get('data', [])
            
            # Se a resposta for uma lista, filtramos cada personagem
            if isinstance(personagens, list):
                for p in personagens:
                    # Verifica se 'Cars' aparece em qualquer um dos filmes do personagem
                    if any("Cars" in filme for filme in p.get('films', [])):
                        print(f"🚗 Nome: {p['name']}")
                        print(f"🎬 Filmes: {', '.join(p['films'])}")
                        print(f"🔗 Imagem: {p.get('imageUrl', 'Sem imagem')}")
                        print("-" * 30)
            
            # Pega a próxima página se existir
            url = data.get('info', {}).get('nextPage')
            
        except requests.exceptions.RequestException as e:
            print(f"Erro ao conectar: {e}")
            break

if __name__ == "__main__":
    mostrar_personagens_carros()
