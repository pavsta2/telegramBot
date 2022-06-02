from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

BLOGS = [
    {
        "pk": 1,
        "title": "Blog title 1"
    },
    {
        "pk": 2,
        "title": "Blog title 2"
    },

]

class Note(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    message = models.TextField(default='', verbose_name='Текст статьи')
    public = models.BooleanField(default=False, verbose_name="Опубликовать")
    create_at = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='Время обновления')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Запись №{self.id}"

    class Meta:
        verbose_name = _("запись")
        verbose_name_plural = _("записи")


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    class Ratings(models.IntegerChoices):
        WITHOUT_RATING = 0, _("Без оценки")
        GOOD = 5, _("хорошо")
        BAD = 2, _("плохо")
    rating = models.IntegerField(default=Ratings.WITHOUT_RATING, choices=Ratings.choices)

    def __str__(self):
        return f"{self.get_rating_display()}: {self.author}"



