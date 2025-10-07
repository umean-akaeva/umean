import logging
from datetime import date


logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


today = date.today()
formatted_date = today.strftime("%Y-%m-%d")


logging.info(f"Поточна дата: {formatted_date}")

print("Повідомлення записано у файл log.txt")
