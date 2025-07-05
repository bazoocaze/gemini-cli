# Gemini CLI

Gemini CLI is a command-line interface for interacting with Google's Generative Language API. It allows you to send prompts to various models and retrieve responses.

## Features

- Send prompts to different models
- List available model IDs
- Save chat history to a file

## Installation

1. Clone the repository:

```bash
git clone https://github.com/bazoocaze/gemini-cli.git
cd gemini-cli
```

2. Install dependencies using pipenv:

```bash
pipenv install
```

3. Set up your environment variables by creating a `.env` file with your API key:

```
GEMINI_API_KEY=your_api_key_here
```

## Usage

### Chat Command

Send a prompt to a model and get a response:

```bash
gemini_cli chat -m gemini-2.5-flash "What is the capital of France?"
```

Save the chat history to `history.jsonl`:

```bash
gemini_cli chat --save -m gemini-2.5-flash "What is the capital of France?"
```

### List Models Command

List all available model IDs:

```bash
gemini_cli list-models-ids
```

## Shell Completion

This project includes shell completion for Bash.

To enable it, source the `gemini_cli_autocomplete.sh` file in your shell configuration (e.g., `.bashrc`, `.zshrc`):

```bash
source /path/to/gemini-cli/gemini_cli_autocomplete.sh
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
