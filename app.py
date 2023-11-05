import streamlit as st

def main():
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
