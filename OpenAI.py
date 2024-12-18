from openai import OpenAI

# Set your OpenAI API key
openai_api_key = ("")


conversation_history = [
    {
        'role': 'system',
        'content': 'You are a helpful assistant.',
    }
]

def generate_response(prompt):
    client = OpenAI(
        api_key=openai_api_key
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                'role': 'system',
                'content': 'You are helpful assistant. Give your best response.',
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o",
    )

    return chat_completion.choices[0].message.content.strip()

