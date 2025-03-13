import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

def app():
    st.set_page_config(page_title="Meu Título Personalizado", page_icon="🤡", layout="centered")
    st.markdown(
        """
        <h1 style="text-align: center;">Converse com o palhaço 🤡</h1>
        <hr>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h5 style="text-align: center;">Escreva e intereja com este chat divertido 😛</h5>
        <hr>
        """,
        unsafe_allow_html=True
    )

    mensagem_usuario = st.chat_input('Digite aqui sua mensagem')
    if mensagem_usuario:
        if 'mensagens' in st.session_state:
            mensagens = st.session_state['mensagens']
        else: 
            mensagens = []
            st.session_state['mensagens'] = mensagens

        mensagens.append(
            {
                'usuario':'user',
                'texto': mensagem_usuario
            }
        )

        # mensagem de resposta do assistente
        # resposta = random.choice(lista_resposta)
        resposta = fazer_pegunta(mensagem_usuario)
        mensagens.append(
            {
                'usuario':'assistant',
                'texto': resposta
            }
        )
        
        for mensagem in mensagens:
            # colocar a mensagem do usuário na tela
            with st.chat_message(mensagem['usuario']):
                st.write(mensagem['texto'])

def fazer_pegunta(pergunta):

    load_dotenv()
    os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
    model = ChatOpenAI(
        model='gpt-4o-mini',
        max_tokens=100
    )
    template = '''
    Você é um chat engraçado e divertido. Intereja com o usuário de maneira engraça e irônica. Conte piadas, pegunte coisas engraçadas
    {input}
    '''

    prompt_template = PromptTemplate.from_template(
        template=template
    )

    prompt = prompt_template.format(
        input=pergunta
    )


    response = model.invoke(prompt)

    
    return response.content           

app()

