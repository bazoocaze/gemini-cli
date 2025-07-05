import os
import sys
import argparse
import requests
import json

def get_headers():
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable is not set.")
        return None

    headers = {
        "X-Goog-Api-Key": api_key,
        "Content-Type": "application/json"
    }
    return headers

def chat(model_name, prompt=None):
    if prompt is None:
        prompt = sys.stdin.read().strip()

    headers = get_headers()
    if not headers:
        return 1

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent"
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
        return {'prompt': prompt, 'response': content}
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return 1

def list_models():
    headers = get_headers()
    if not headers:
        return 1

    url = "https://generativelanguage.googleapis.com/v1beta/models"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response_json = response.json()
        models = response_json.get('models', [])
        for model in models:
            print(model.get('name', '').replace('models/', ''))
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return 1

def main():
    parser = argparse.ArgumentParser(description='Interact with the Gemini API')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Chat command
    chat_parser = subparsers.add_parser('chat', help='Send a prompt to a model')
    chat_parser.add_argument('-m', '--model', default='gemini-2.5-flash', help='Model name (default: gemini-2.5-flash)')
    chat_parser.add_argument('--save', action='store_true', help='Save/append the chat result to history.jsonl')
    chat_parser.add_argument('prompt', nargs='?', help='The prompt to send')

    # List models command
    list_parser = subparsers.add_parser('list-models-ids', help='List available model IDs')

    args = parser.parse_args()

    if args.command == 'chat':
        result = chat(args.model, args.prompt)
        if isinstance(result, dict) and args.save:
            with open('history.jsonl', 'a') as f:
                json.dump(result, f)
                f.write('\n')
        return 0 if isinstance(result, dict) else result
    elif args.command == 'list-models-ids':
        return list_models() or 0

if __name__ == '__main__':
    sys.exit(main())
