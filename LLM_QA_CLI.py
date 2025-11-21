import os
import re
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def preprocess_input(text):
    """
    Applies basic preprocessing: lowercasing, punctuation removal, and tokenization.
    Returns the cleaned text and the list of tokens.
    """
    # 1. Lowercasing
    text_lower = text.lower()
    
    # 2. Punctuation removal
    text_clean = re.sub(r'[^\w\s]', '', text_lower)
    
    # 3. Tokenization (simple whitespace split)
    tokens = text_clean.split()
    
    return text_clean, tokens

def get_llm_response(question, api_key):
    """
    Sends the question to the Hugging Face API and returns the response.
    """
    try:
        # Using Hugging Face Router endpoint (OpenAI-compatible)
        api_url = "https://router.huggingface.co/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # Using Gemma 2 model
        payload = {
            "model": "google/gemma-2-9b-it",
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ],
            "max_tokens": 500,
            "temperature": 0.7
        }
        
        response = requests.post(api_url, headers=headers, json=payload, timeout=30)
        
        if response.status_code != 200:
            return f"API Error {response.status_code}: {response.text}"
            
        result = response.json()
        
        # Extract answer from OpenAI-compatible response
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"].strip()
        elif "error" in result:
             return f"API Error: {result['error']}"
        else:
            return f"Unexpected response format: {result}"
    except Exception as e:
        return f"Error communicating with Hugging Face API: {e}"

def main():
    print("--- NLP Q&A System CLI (Hugging Face Powered) ---")
    
    # Get API Key
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    if not api_key:
        api_key = input("Please enter your Hugging Face API Key: ").strip()
    
    if not api_key:
        print("API Key is required to proceed.")
        return

    while True:
        print("\n--------------------------------------------------")
        user_input = input("Enter your question (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
        
        if not user_input.strip():
            continue

        # Preprocessing
        print("\n[Processing]...")
        cleaned_text, tokens = preprocess_input(user_input)
        print(f"Processed Question: {cleaned_text}")
        print(f"Tokens: {tokens}")
        
        # Construct Prompt (Using the original or cleaned text - usually original is better for LLMs, 
        # but we'll use the cleaned one to demonstrate the pipeline if strictly required. 
        # However, for best results, I'll send the original but acknowledge the processing.)
        # Let's send the original for better context understanding by the LLM, 
        # as removing punctuation can hurt semantic understanding.
        # But to strictly follow "process it, sends it", I will send the cleaned text.
        
        print("\n[Sending to Hugging Face]...")
        answer = get_llm_response(cleaned_text, api_key)
        
        print("\n[Answer]:")
        print(answer)

if __name__ == "__main__":
    main()
