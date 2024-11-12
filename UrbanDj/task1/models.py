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


# >>> from task1.models import Buyer
# >>> Buyer.objects.create(name='Nagibator404', balance = 100.00, age =17)
# <Buyer: Nagibator404>
# >>> Buyer.objects.create(name='Dima', balance = 200.00, age =32)
# <Buyer: Dima>
# >>> Buyer.objects.create(name='Petr Prohorov', balance = 300.00, age =20)
# <Buyer: Petr Prohorov>
# >>> from task1.models import Game
# >>> Game.objects.create(title='Mario', cost=52.52, size = 30.00, description = 'Old game', age_limited =False)
# <Game: Mario>
# >>> Game.objects.create(title='Mortal Combat', cost=152.20, size = 130.00, description = 'best game', age_limited =True)
# <Game: Mortal Combat>
# >>> Game.objects.create(title='Football', cost=100.00, size = 20.00, description = 'popular game', age_limited =True)
# <Game: Football>
# >>> buyer1 = Buyer.objects.get(id=1)
# >>> buyer2 = Buyer.objects.get(id=2)
# >>> buyer3 = Buyer.objects.get(id=3)
# >>> game1 = Game.objects.get(id=1)
# >>> game2 = Game.objects.get(id=2)
# >>> game3 = Game.objects.get(id=3)
# >>> game1.buyers.set([buyer1, buyer2, buyer3])
# >>> game2.buyers.set([buyer2, buyer3])
# >>> game3.buyers.set([buyer3])
