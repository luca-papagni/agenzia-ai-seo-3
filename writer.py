from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_article(topic: str) -> str:
    rsp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system",
             "content": "Sei un copywriter SEO professionista."},
            {"role": "user",
             "content": f"Scrivi un articolo di almeno 1 000 caratteri, "
                        f"ben formattato (H1, H2, paragrafi), sul tema: {topic}"}
        ],
        temperature=0.7,
        max_tokens=900
    )
    return rsp.choices[0].message.content
