import os
from openai import OpenAI
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def translate_to_spanish_with_groq(text):
    """
    Translates the given text to Spanish using the Groq API.

    Parameters:
    text (str): The text to be translated.

    Returns:
    str: The translated text.
    """
    
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "llama3-8b-8192",  # or another available Groq model
        "messages": [
            {
                "role": "system",
                "content": "You are a translator. Translate the following text to Spanish. Return ONLY the translation, without any explanation."
            },
            {
                "role": "user",
                "content": text
            }
        ],
        "temperature": 0.3
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        translated_text = response.json()['choices'][0]['message']['content']
        return translated_text
    
    except requests.exceptions.RequestException as e:
        print(f"Error during translation: {e}")
        return None

# translated_text = translate_to_spanish("Hello, how are you?")

# print(translated_text)

def translate_to_spanish_with_xAI(text):
    """
    Translates the given text to Spanish using the xAI API.

    Parameters:
    text (str): The text to be translated.

    Returns:
    str: The translated text.
    """
    
    # Get the XAI API key from environment variables
    XAI_API_KEY = os.getenv("XAI_API_KEY")
    
    # Check if API key exists
    if not XAI_API_KEY:
        raise ValueError("GROK_API_KEY not found in environment variables")

    # Initialize the OpenAI client with XAI configuration
    client = OpenAI(
        api_key=XAI_API_KEY,
        base_url="https://api.x.ai/v1",
    )
    
    # Create a chat completion request
    completion = client.chat.completions.create(
         model = "grok-beta",
         messages = [
            {
                "role": "system",
                "content": "You are a Spanish translator. Translate the text exactly as provided, maintaining the original meaning and tone."
            },
            {
                "role": "user",
                "content": f"Translate this to Spanish: {text}"
            },
        ],
    )

    try:
        # Extract the translated text from the response
        translated_text = completion.choices[0].message.content
        return translated_text
    
    except:
        # Handle any errors during translation
        print("Error during translation:")
        return None

def translate_to_spanish_with_ollama(text):
    """
    Translates the given text to Spanish using Ollama API with a small language model.

    Parameters:
    text (str): The text to be translated.

    Returns:
    str: The translated text.
    """
    import requests
    
    url = "http://localhost:11434/api/generate"
    
    data = {
        "model": "llama3.2:1b", # You can also use other models like "llama2"
        "prompt": f"Translate this {text} to Spanish. Return ONLY the translation, nothing else.",
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        translated_text = response.json()['response']
        return translated_text.strip()
        
    except requests.exceptions.RequestException as e:
        print(f"Error during translation: {e}")
        return None

   

# Example usage:
# translated_text = translate_text_to_spanish("Hello, how are you?")

# Example usage:
# translated_text = translate_to_spanish_with_ollama("Hello, how are you?")
# print(translated_text)
# print(type(translated_text))