import schedule, time, datetime
from site_manager import all_sites
from writer import generate_article
from image_gen import generate_image
from wp_publisher import publish_post
from config import wp_credentials

def workflow():
    print("⏱", datetime.datetime.now(), "Ciclo avviato")
    for site in all_sites():
        topic = site["topic"]
        wp_url = site["wordpress_url"]
        creds = wp_credentials(site["alias"])
        if not creds["user"] or not creds["password"]:
            print(f"❌ Credenziali mancanti per {site['alias']}")
            continue

        article = generate_article(topic)
        img_url = generate_image(topic)
        publish_post(
            wp_url=wp_url,
            creds=creds,
            title=f"{topic} – {datetime.date.today()}",
            content=article,
            image_url=img_url
        )
    print("✅ Fine ciclo\n")

def start_scheduler():
    schedule.every().day.at("09:00").do(workflow)   # cambia se vuoi test
    while True:
        schedule.run_pending()
        time.sleep(30)
