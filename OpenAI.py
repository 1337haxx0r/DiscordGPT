import os

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

# Set your OpenAI API key
api_key = os.getenv('OPENAI_TOKEN')


conversation_history = [
    {
        'role': 'system',
        'content': 'You are a helpful assistant.',
    }
]

def generate_response(prompt):
    client = OpenAI(
        api_key=api_key
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
        stream=True
    )

    # return chat_completion.choices[0].message.content.strip()

    for chunk in chat_completion:
        content = chunk.choices[0].delta.content  # Direct access to content
        if content is not None:  # Filter out None values
            yield content



