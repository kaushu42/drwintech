from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()


class Person(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()

    def __repr__(self):
        return f'{self.name}: {self.email}'

    def __str__(self):
        return self.__repr__()
