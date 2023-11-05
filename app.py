import streamlit as st

from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def main():
    load_dotenv()
    st.set_page_config(
        page_title="NLP Wizard Chatbot",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.header(body="NLP Wizard Chatbot 🤖")
    st.chat_input(placeholder="Ask a question about your meeting transcript(s).")

    with st.sidebar:
        st.subheader("Your transcript(s)")
        pdf_docs = st.file_uploader("Upload your transcript PDFs here and click 'Process'", accept_multiple_files=True)
        
        if st.button("Process"):
            with st.spinner("Processing"):

                # get pdf text
                raw_text = get_pdf_text(pdf_docs)


                
if __name__ == "__main__":
    main()
