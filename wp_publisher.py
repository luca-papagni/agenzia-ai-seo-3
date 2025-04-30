import requests

def _upload_media(image_url: str, wp_url: str, user: str, pwd: str) -> int | None:
    try:
        img_resp = requests.get(image_url, timeout=30)
        img_resp.raise_for_status()
        headers = {
            "Content-Disposition": 'attachment; filename="header.jpg"',
            "Content-Type": "image/jpeg"
        }
        endpoint = wp_url.rstrip("/") + "/wp-json/wp/v2/media"
        r = requests.post(endpoint,
                          auth=(user, pwd),
                          headers=headers,
                          data=img_resp.content, timeout=60)
        r.raise_for_status()
        return r.json().get("id")
    except Exception as e:
        print("⚠️  Upload immagine fallito:", e)
        return None

def publish_post(wp_url: str, creds: dict,
                 title: str, content: str, image_url: str):
    media_id = _upload_media(image_url, wp_url, **creds)

    post_data = {
        "title": title,
        "content": content,
        "status": "publish"
    }
    if media_id:
        post_data["featured_media"] = media_id

    endpoint = wp_url.rstrip("/") + "/wp-json/wp/v2/posts"
    r = requests.post(endpoint, auth=tuple(creds.values()),
                      json=post_data, timeout=60)
    r.raise_for_status()
    post_id = r.json()["id"]
    print(f"✅ Pubblicato su {wp_url} (ID {post_id})")
