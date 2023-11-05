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
        st.button("Process")
if __name__ == "__main__":
    main()
