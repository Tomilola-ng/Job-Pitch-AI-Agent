"""Main module for AI-agent."""


def main():
    """Main function for AI-agent."""
    while True:
        # Enable the user to chat with the AI
        user_input = input('You: ')

        if user_input == 'exit':
            break

        response = {'response': "Testing"}  # handle_input(user_input)

        print('AI:', response['response'])


if __name__ == "__main__":
    main()
