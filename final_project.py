import sqlite3
import requests
from bs4 import BeautifulSoup


class DatabaseManager:
    def __init__(self, db_name="sites.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Створюємо таблицю, якщо її ще немає"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT UNIQUE
            )
        """)
        self.conn.commit()

    def add_site(self, url):
        """Додаємо сайт у базу"""
        try:
            self.cursor.execute("INSERT INTO sites (url) VALUES (?)", (url,))
            self.conn.commit()
            print("Сайт додано успішно!")
        except sqlite3.IntegrityError:
            print("⚠Такий сайт уже є у базі.")

    def get_sites(self):
        """Отримуємо список усіх сайтів"""
        self.cursor.execute("SELECT url FROM sites")
        return [row[0] for row in self.cursor.fetchall()]

    def clear_db(self):
        """Очищаємо базу даних"""
        self.cursor.execute("DELETE FROM sites")
        self.conn.commit()
        print("Базу очищено!")

class WebParser:
    def __init__(self):
        pass

    def count_word_occurrences(self, url, word):
        """Повертає кількість входжень слова на сторінці"""
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text().lower()
            return text.count(word.lower())
        except Exception as e:
            print(f"Не вдалося відкрити {url}: {e}")
            return 0

class UserInterface:
    def __init__(self):
        self.db = DatabaseManager()
        self.parser = WebParser()

    def menu(self):
        while True:
            print("\n=== МЕНЮ ===")
            print("1. Додати сайт")
            print("2. Очистити базу")
            print("3. Показати всі сайти")
            print("4. Пошук слова")
            print("5. Вихід")

            choice = input("Ваш вибір: ")

            if choice == "1":
                url = input("Введіть адресу сайту (https://...): ")
                self.db.add_site(url)
            elif choice == "2":
                self.db.clear_db()
            elif choice == "3":
                print("Сайти у базі:")
                for site in self.db.get_sites():
                    print(" -", site)
            elif choice == "4":
                self.search_word()
            elif choice == "5":
                print("До побачення!")
                break
            else:
                print("⚠Невірний вибір!")

    def search_word(self):
        word = input("Введіть слово для пошуку: ")
        sites = self.db.get_sites()

        if not sites:
            print("⚠У базі немає сайтів!")
            return

        results = []
        for site in sites:
            count = self.parser.count_word_occurrences(site, word)
            results.append((site, count))


        results.sort(key=lambda x: x[1], reverse=True)

        print("\n=== РЕЗУЛЬТАТИ ===")
        for site, count in results:
            print(f"{site} — {count} входжень")


def run():
    ui = UserInterface()
    ui.menu()


if __name__ == "__main__":
    run()

