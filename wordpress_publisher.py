import requests

def upload_image_to_wordpress(image_url, wordpress_url, wordpress_user, wordpress_password):
    try:
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        filename = "immagine_articolo.jpg"
        headers = {
            'Content-Disposition': f'attachment; filename={filename}',
            'Content-Type': 'image/jpeg'
        }

        media_url = wordpress_url.rstrip("/") + "/wp-json/wp/v2/media"

        response = requests.post(
            media_url,
            headers=headers,
            data=image_response.content,
            auth=(wordpress_user, wordpress_password)
        )
        response.raise_for_status()
        
        media_id = response.json().get('id')
        return media_id
    except Exception as e:
        print("❌ Errore nel caricamento immagine:", e)
        return None

def publish_to_wordpress(title, content, image_url, wordpress_url, wordpress_user, wordpress_password):
    try:
        print(f"📝 Pubblicazione su: {wordpress_url}")
        media_id = upload_image_to_wordpress(image_url, wordpress_url, wordpress_user, wordpress_password)

        data = {
            'title': title,
            'content': content,
            'status': 'publish'
        }

        if media_id:
            data['featured_media'] = media_id

        post_url = wordpress_url.rstrip("/") + "/wp-json/wp/v2/posts"

        response = requests.post(
            post_url,
            auth=(wordpress_user, wordpress_password),
            json=data
        )

        response.raise_for_status()
        post_id = response.json()['id']
        print(f"✅ Articolo pubblicato su {wordpress_url}! ID: {post_id}")
    except Exception as e:
        print("❌ Errore nella pubblicazione su WordPress:", e)
