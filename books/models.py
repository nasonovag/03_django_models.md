from django.db import models
# Модель Автора
class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

# Жанры (предопределенные)
GENRE_CHOICES = [
    ('fiction', 'Художественная литература'),
    ('non-fiction', 'Нон-фикшн'),
    ('sci-fi', 'Научная фантастика'),
]

# Модель Книги
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)

    def __str__(self):
        return self.title