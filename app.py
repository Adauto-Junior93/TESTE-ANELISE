import streamlit as st

st.set_page_config(page_title="Coração do Adauto", page_icon="💖")

st.title("💖 Coração do Adauto 💖")

nome = st.text_input("Qual o seu nome?")

if nome:

    if nome.lower().strip() == "anelise":

        senha = st.text_input("Digite a senha secreta:", type="password")

        if senha:

            if senha == "281193":
                st.success("Acesso liberado ❤️")

                comida = st.text_input("Qual sua comida favorita?")
                idade = st.number_input("Qual sua idade?", step=1, min_value=0)

                if comida and idade:
                    st.markdown("## 💌 RESULTADO 💌")
                    st.write("**Nome:**", nome)
                    st.write("**Idade:**", idade)

                    if comida.lower().strip() == "lasanha":
                        st.success("A gente combina 😍🍕")
                    else:
                        st.info("Prefiro lasanha com você 😄")

                    st.markdown("### ❤️ Amor da vida do Adauto ❤️")

            else:
                st.error("Senha incorreta!")

    else:
        st.error("Acesso negado 🚫")
