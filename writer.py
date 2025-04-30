from openai import OpenAI
import os

# Inizializza il client OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_article(topic):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Sei un esperto di scrittura SEO. Scrivi un articolo dettagliato, chiaro e coinvolgente."},
                {"role": "user", "content": f"Scrivi un articolo SEO di almeno 1000 caratteri sul tema: {topic}"}
            ],
            temperature=0.7,
            max_tokens=800  # ~1000 caratteri
        )
        article = response.choices[0].message.content
        return article
    except Exception as e:
        print(f"❌ Errore nella generazione dell'articolo: {e}")
        return ""
