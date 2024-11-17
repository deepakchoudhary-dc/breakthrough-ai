import openai
from config import OPENAI_API_KEY

openai.api_key = "AIzaSyAm5O1BC4RZqptmvlGKbA2LViIDuIaLDYk"  # Use the key from config

def extract_information(search_results, entity, prompt_template):
    prompt = prompt_template.format(company=entity, results=search_results)
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        print(f"Error in extract_information: {e}")
        return None
