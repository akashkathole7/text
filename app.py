import streamlit as st
from transformers import AutoModelWithLMHead, AutoTokenizer


st.title("Text Summarization using GPT-2")
text = st.text_input("Enter the text you want to summarize below:")

  

def generate_summary(text):
    input_ids = tokenizer.encode(text[:1024], return_tensors='pt')
    output = model.generate(input_ids, max_length=MAX_LENGTH, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(output[0], skip_special_tokens=True)
    return summary




if __name__ == '__main__':
    st.write('Loading model...')
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    model = AutoModelWithLMHead.from_pretrained("gpt2")
    st.write('Model loaded!')
    st.write('Enter the text you want to summarize below:')
    user_input = st.text_input("")
    if user_input:
        summary = generate_summary(user_input)
        st.write(summary)

