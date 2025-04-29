import schedule
import time
from seo_writer import generate_article
from image_generator import generate_image
from wordpress_publisher import publish_to_wordpress
from site_manager import load_sites

def workflow():
    print("⏱ Avvio generazione articoli per tutti i siti...")

    sites = load_sites()

    for site in sites:
        topic = "Tendenze SEO 2025"  # In futuro dinamico
        article = generate_article(topic)
        image_url = generate_image(topic)

        publish_to_wordpress(
            title=f"Nuovo articolo: {topic}",
            content=article,
            image_url=image_url,
            wordpress_url=site['wordpress_url'],
            wordpress_user=site['wordpress_user'],
            wordpress_password=site['wordpress_password']
        )

    print("✅ Tutti gli articoli pubblicati!")

def start_scheduler():
    schedule.every().day.at("09:00").do(workflow)

    print("🟢 Scheduler attivo. In attesa del prossimo ciclo...")

    while True:
        schedule.run_pending()
        time.sleep(60)
