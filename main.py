import os
import sys
import requests

def chat(model_name, prompt):
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable is not set.")
        return

    url = f"https://api.gemini.com/v1/models/{model_name}/chat"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == '__main__':
    if len(sys.argv) != 4 or sys.argv[1] != 'chat' or sys.argv[2] != '-m':
        print("Usage: python main.py chat -m nome_do_modelo prompt")
    else:
        model_name = sys.argv[3]
        prompt = ' '.join(sys.argv[4:])
        chat(model_name, prompt)
