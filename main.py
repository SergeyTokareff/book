class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.reviews = []

    def __repr__(self):
        return (f"Book(title='{self.title}', author='{self.author}', year='{self.year}', genre='{self.genre}')")

    def __str__(self):
        reviews_str = "\n".join(self.reviews) if self.reviews else "Відгуки відсутні"
        return (f"{self.title} {self.author} {self.year} {self.genre}\n"
                f"Відгуки:\n{reviews_str}")


    def add_review(self, review):
        self.reviews.append(review)

book1 = Book(title="Жар", author="Рейвен Кеннеді", year="2023", genre="Фентезі")
book2 = Book(title="Освічена", author="Тара Вестовер", year="2024", genre="Біографічна проза")
book3 = Book(title="Годинник Аріадни", author="Анна Багряна", year="2023", genre="Фантастика")

book1.add_review("Клас")
book1.add_review("Крута книга!")
book2.add_review("Дивовижно!!!")
book2.add_review("Чудово")
book2.add_review("Дуже сподобалось")
book3.add_review("Класно")
book3.add_review("Рекомендую почитати")
book3.add_review("Автор молодець")

print(repr(book1))
print(str(book2))


print(book1)
print(book2)
print(book3)