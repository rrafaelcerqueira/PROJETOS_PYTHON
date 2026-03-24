import requests
import streamlit as st

st.title("Buscador Disney")

nome_personagem = st.text_input("Digite o nome do personagem (ex: Mickey, Mulan):")

if st.button("Buscar"):
    if nome_personagem:
        url = f"https://api.disneyapi.dev/character?name={nome_personagem}"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()
            
            if dados['data']:
                personagem = dados['data'][0]
                
                st.header(personagem['name'])
                
                if 'imageUrl' in personagem:
                    st.image(personagem['imageUrl'], width=300)
                
                filmes = personagem.get('films', [])
                if filmes:
                    st.subheader("Filmes:")
                    for filme in filmes:
                        st.write(f"- {filme}")
                
                series = personagem.get('tvShows', [])
                if series:
                    st.subheader("Séries de TV:")
                    for serie in series:
                        st.write(f"- {serie}")
            else:
                st.warning("Nenhum personagem encontrado.")
        else:
            st.error("Erro na comunicação com a API.")
    else:
        st.info("Por favor, digite um nome.")