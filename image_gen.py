from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_image(prompt: str) -> str:
    rsp = client.images.generate(
        model="dall-e-3",
        prompt=f"High-quality blog header, {prompt}, "
               f"minimal text, modern flat illustration",
        n=1,
        size="1024x1024"
    )
    return rsp.data[0].url
