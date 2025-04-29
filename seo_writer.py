from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_article(topic):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sei un esperto SEO che scrive articoli ottimizzati."},
                {"role": "user", "content": f"Scrivi un articolo SEO di almeno 1000 caratteri sul tema: {topic}."}
            ]
        )
        article = response.choices[0].message.content
        return article
    except Exception as e:
        print("❌ Errore nella generazione dell'articolo:", e)
        return None
