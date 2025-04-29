import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_image(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            model="dall-e-3",
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url

    except Exception as e:
        print("❌ Errore nella generazione immagine:", e)
        return "https://via.placeholder.com/1024"  # immagine di fallback
