from openai import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def main():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a short poem about PyCharm."}
    ]
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",  # Specify the model
        messages=messages,
        max_tokens=50  # Limit the response length
)
        print("OpenAI response:")
        print(response.choices[0].message.content.strip())
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
