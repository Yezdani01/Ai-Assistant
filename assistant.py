from openai from OpenAI
key = "your-api-key"

messages = []

cliendt = OpenAI(

    api_key=key
)

def completion(message):
    global messages
    messages.append(
        {
            "role": "user", 
            "content": message

         }
    )

    chat_completion = client.chat.completions.create(messages=messages, model="gpt-3.5-turbo")

    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }

    if __name__ == "__main__":
        print(f"Jarvis: Hi I am Jarvis, your AI assistant. How can I help you today?\n")
        while True:
            user_question = input()
            print(f"User: {user_question}")
            completion(user_question)
