from pathlib import Path
from docxtpl import DocxTemplate
import streamlit as st
import os

def criar_cv(): 
  
    with st.form(key='col1', clear_on_submit=True):
   
        nome = st.text_input("Nome")
        naturalidade = st.text_input("Local de Nascimento")
        data = st.text_input("Data de Nascimento")
        residencia = st.text_input("Residencia")
        telefone = st.text_input("Numero de Telefone")
        email = st.text_input("Email:")
        nivel = st.text_input("Formaçoes Literarias")
        formacao = st.text_area("Formaçoes Profissionais")
        experiencias = st.text_area("Experiencias")
        habilidade = st.text_area("Habilidades")
        referencias= st.text_area("Referencias")
        #foto = st.file_uploader("carregar uma foto")

        path_documento = Path(__file__).parent/"curriculun.docx"
        modelo = DocxTemplate(path_documento)
        context ={'nome':nome,
                  'naturalidade':naturalidade,
                  'data':data,
                  'residencia':residencia,
                  'telefone':telefone,
                  'nivel':nivel,
                  'formacao':formacao,
                  'experiencias':experiencias,
                  'habilidade':habilidade,
                  'referencias':referencias,
                  'email':email}
        modelo.render(context)
        #pasta = st.text_input("Nome do documento")
        documento_novo = st.text_input("Nome do documento:")
        desktop_path = os.path.expanduser("~/Desktop")
        modelo.save(os.path.join(desktop_path, f"{documento_novo}.docx"))
       
      
        
        botao = st.form_submit_button("Criar Novo CV")
        if botao  ==True:
            st.success("O documento foi Criado com Sucesso")
                    
criar_cv()