from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_image(prompt):
    try:
        response = client.images.generate(
            model="dall-e-2",
            prompt=f"Immagine in stile SEO sul tema: {prompt}",
            n=1,
            size="1024x1024"
        )
        image_url = response.data[0].url
        return image_url
    except Exception as e:
        print("❌ Errore nella generazione immagine:", e)
        return None
