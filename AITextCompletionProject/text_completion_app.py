from dotenv import load_dotenv
import os
import cohere

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def get_completion(prompt, temperature=0.7, max_tokens=150):
    try:
        response = co.generate(
            model='command',
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

prompt = input("Enter a prompt: ")
response = get_completion(prompt)
print("\nAI Response:\n", response)