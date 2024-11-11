from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=150, unique=True)  # Имя покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Баланс
    age = models.PositiveIntegerField()  # Возраст

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=255)  # Название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    size = models.DecimalField(max_digits=10, decimal_places=2)  # Размер файлов игры
    description = models.TextField()  # Описание (неограниченное количество текста)
    age_limited = models.BooleanField(default=False)  # Ограничение возраста 18+

    buyers = models.ManyToManyField(Buyer, related_name='games')  # Покупатель, обладающий игрой

    def __str__(self):
        return self.title