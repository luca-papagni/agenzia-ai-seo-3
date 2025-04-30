from openai import OpenAI
import os

# Inizializza il client OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_image(topic):
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=f"Immagine rappresentativa per un articolo sul tema: {topic}",
            n=1,
            size="1024x1024"
        )
        image_url = response.data[0].url
        return image_url
    except Exception as e:
        print(f"❌ Errore nella generazione dell'immagine: {e}")
        return ""
