import os
import sys
import argparse
import requests

def chat(model_name, prompt):
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable is not set.")
        return

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent"
    headers = {
        "X-Goog-Api-Key": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        response_json = response.json()
        content = response_json.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        print(content)
    else:
        print(f"Error: {response.status_code} - {response.text}")

def main():
    parser = argparse.ArgumentParser(description='Interact with the Gemini API')
    parser.add_argument('command', choices=['chat'], help='The command to execute')
    parser.add_argument('-m', '--model', required=True, help='Model name')
    parser.add_argument('prompt', nargs=argparse.REMAINDER, help='The prompt to send')
    args = parser.parse_args()

    if args.command == 'chat':
        prompt = ' '.join(args.prompt)
        chat(args.model, prompt)

if __name__ == '__main__':
    main()
