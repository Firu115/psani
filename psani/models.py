from django.db import models

class Lekce(models.Model):
    id = models.IntegerField()
    pismena = models.CharField(max_length=50)
    jmeno = models.CharField(max_length=10)

    class Meta:
        app_label = 'psani'

    def __str__(self) -> str:
        return self.jmeno


class Uzivatel(models.Model):
    id = models.IntegerField()
    email = models.CharField(max_length=254)
    lekce = models.CharField()

    class Meta:
        app_label = 'psani'

    def get_lekce(self) -> list:
        arr = []
        cislo = ""

        for i in self.lekce:
            if i != ",":
                cislo += i
            else:
                arr.append(int(cislo))
                cislo = ""
        return arr
