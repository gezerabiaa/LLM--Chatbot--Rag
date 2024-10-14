import streamlit as st
from chatbot import load_knowledge_base, generate_with_rag


def main():
    st.title("Humanore Chatbot")
    knowledge_base = load_knowledge_base('knowledge_base.json')
    prompt = st.text_input("Bir soru sorun")

    if st.button("Submit"):
        # Call the function with RAG
        model_url = " "
        model = "llama3.1"

        if prompt:
            response_text = generate_with_rag(model_url, model, prompt, knowledge_base)
            st.write(response_text)
        else:
            st.write("error.")

if __name__ == "__main__":
    main()
 
