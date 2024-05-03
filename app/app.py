# This is for demo purposes only and not designed for production use

import streamlit as st
import requests
import json
import os

model_url = os.getenv('INFERENCE_SERVER')
model_name = os.getenv('MODEL_NAME')

st.title('Chat using vLLM and ' + model_name)

question = st.text_input('Ask a question, for example: Tell me a joke')

if len(question.strip())==0:
    question="Tell me a joke"

question_json = {
        "model": "/mnt/models/",
        "prompt": question,
        "max_tokens": 100,
        "temperature": 0
    }

model_path="/v1/completions"

r = requests.post(model_url+model_path, json=question_json, verify=False)

model_output = ""
if r.status_code < 400:
    response_dict = json.loads(r.text)
    model_output = response_dict["choices"][0]["text"]
else:
    model_output = "Text generation request failed"

# Display output on the Web page
formatted_output = f"""
    **Response:** {question} \
    *{model_output}*</i>
    """
st.markdown(formatted_output, unsafe_allow_html=True)