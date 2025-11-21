import os
import re
import requests
import traceback
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure Hugging Face API
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

def preprocess_input(text):
    """
    Applies basic preprocessing: lowercasing, punctuation removal, and tokenization.
    """
    text_lower = text.lower()
    text_clean = re.sub(r'[^\w\s]', '', text_lower)
    tokens = text_clean.split()
    return text_clean, tokens

def get_llm_response(question):
    if not HUGGINGFACE_API_KEY:
        return "Error: Hugging Face API Key not configured."
    
    try:
        # Using Zephyr-7B-Beta via direct API call for maximum compatibility
        api_url = "https://router.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta/v1/chat/completions"
        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
        
        payload = {
            "model": "HuggingFaceH4/zephyr-7b-beta",
            "messages": [{"role": "user", "content": question}],
            "max_tokens": 500,
            "stream": False
        }
        
        print(f"Sending request to Hugging Face API (Zephyr)...")
        response = requests.post(api_url, headers=headers, json=payload)
        
        if response.status_code != 200:
            error_msg = f"API Error {response.status_code}: {response.text}"
            print(error_msg)
            return error_msg
            
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        print("Error calling Hugging Face API:")
        traceback.print_exc()
        return f"Error: {str(e)} (Check terminal for details)"

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = None
    processed_question = None
    original_question = None
    
    if request.method == 'POST':
        original_question = request.form.get('question')
        
        if original_question:
            # Preprocess
            processed_text, tokens = preprocess_input(original_question)
            processed_question = f"{processed_text} (Tokens: {tokens})"
            
            # Get Response
            answer = get_llm_response(processed_text)
            
    return render_template('index.html', 
                           answer=answer, 
                           processed_question=processed_question,
                           original_question=original_question)

if __name__ == '__main__':
    app.run(debug=True)
