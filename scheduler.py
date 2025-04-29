import schedule
import time
from seo_writer import generate_article
from image_generator import generate_image
from wordpress_publisher import publish_to_wordpress

def workflow():
    print("⏱ Avvio generazione articolo...")
    
    topic = "tendenze SEO 2025"  # In futuro sarà dinamico
    article = generate_article(topic)
    image_url = generate_image(topic)

    publish_to_wordpress(
        title=f"Nuovo articolo: {topic}",
        content=article,
        image_url=image_url
    )

    print("✅ Pubblicazione completata!")

def start_scheduler():
    schedule.every().day.at("09:00").do(workflow)

    print("🟢 Scheduler attivo. In attesa del prossimo ciclo...")

    while True:
        schedule.run_pending()
        time.sleep(60)
