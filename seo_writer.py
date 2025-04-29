import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_article(topic):
    prompt = f"""
Scrivi un articolo SEO completo e originale sul tema: {topic}.
L'articolo deve essere in italiano, avere almeno 1000 caratteri, e includere:
- Un titolo H1
- Un'introduzione coinvolgente
- Almeno 2 sottotitoli H2 con paragrafi coerenti
- Uno stile chiaro, informativo e professionale

Non includere frasi tipo "Ecco a te", "In questo articolo ti mostrerò" o cose troppo generiche.
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1000
        )

        articolo = response["choices"][0]["message"]["content"]
        return articolo

    except Exception as e:
        print("❌ Errore nella generazione dell'articolo:", e)
        return f"Errore nella generazione dell'articolo su: {topic}"
