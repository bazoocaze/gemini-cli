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

def list_models():
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable is not set.")
        return

    url = "https://generativelanguage.googleapis.com/v1beta/models"
    headers = {
        "X-Goog-Api-Key": api_key,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response_json = response.json()
        models = response_json.get('models', [])
        for model in models:
            print(model.get('name', ''))
    else:
        print(f"Error: {response.status_code} - {response.text}")

def main():
    parser = argparse.ArgumentParser(description='Interact with the Gemini API')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Chat command
    chat_parser = subparsers.add_parser('chat', help='Send a prompt to a model')
    chat_parser.add_argument('-m', '--model', required=True, help='Model name')
    chat_parser.add_argument('prompt', help='The prompt to send')

    # List models command
    list_parser = subparsers.add_parser('list-models-ids', help='List available model IDs')

    args = parser.parse_args()

    if args.command == 'chat':
        chat(args.model, args.prompt)
    elif args.command == 'list-models-ids':
        list_models()

if __name__ == '__main__':
    sys.exit(main())
