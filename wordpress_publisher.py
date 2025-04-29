import requests
from config import WORDPRESS_URL, WORDPRESS_USER, WORDPRESS_PASSWORD

def upload_image_to_wordpress(image_url):
    try:
        image_data = requests.get(image_url).content
        filename = "immagine_articolo.jpg"
        headers = {
            'Content-Disposition': f'attachment; filename={filename}'
        }
        response = requests.post(
            f"{WORDPRESS_URL}/wp-json/wp/v2/media",
            headers=headers,
            data=image_data,
            auth=(WORDPRESS_USER, WORDPRESS_PASSWORD)
        )
        response.raise_for_status()
        media_id = response.json()['id']
        return media_id
    except Exception as e:
        print("❌ Errore nel caricamento immagine:", e)
        return None

def publish_to_wordpress(title, content, image_url):
    try:
        print("📝 Pubblicazione in corso...")
        media_id = upload_image_to_wordpress(image_url)

        data = {
            'title': title,
            'content': content,
            'status': 'publish',
            'featured_media': media_id if media_id else None
        }

        response = requests.post(
            f"{WORDPRESS_URL}/wp-json/wp/v2/posts",
            auth=(WORDPRESS_USER, WORDPRESS_PASSWORD),
            json=data
        )

        response.raise_for_status()
        post_id = response.json()['id']
        print(f"✅ Articolo pubblicato! ID: {post_id}")
    except Exception as e:
        print("❌ Errore nella pubblicazione su WordPress:", e)
