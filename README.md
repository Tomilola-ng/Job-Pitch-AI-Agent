# AI Agent Setup

AI Agent for automating digital tasks.

## Requirements

- Python 3.13 or higher
- OpenAI API key
- Git
- [UV](https://github.com/astral-sh/uv) : An extremely fast Python package and project manager

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Tomilola-ng/ai-agent-setup.git
```

2. Install the required dependencies:

```bash
uv sync
```

3. Create a `.env` file in the root directory of the project and add your OpenAI API key:

```bash
OPENAI_API_KEY=your_api_key_here
```

## Usage

To use the AI Agent, you need to set up an OpenAI API key in the `.env` file. You can get an API key from the OpenAI website.

Once you have the API key, you can run the AI Agent by executing the following command:

```bash
uv main.py
```

This will start the AI Agent and it will ask you a question and wait for your response.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
