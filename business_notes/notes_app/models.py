from django.db import models
from datetime import datetime, timedelta
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User

class Note(models.Model):
    active = "Активно"
    delay = "Отложено"
    done = "Выполнено"
    conditions = [(active,"Активно"), (delay,"Отложено"), (done,"Выполнено")]

    title = models.CharField(max_length=200, verbose_name="Заголовок")
    message = models.TextField(default='', verbose_name="Описание")
    public = models.BooleanField(default=False, verbose_name="Опубликовать")
    importance = models.BooleanField(default=True, verbose_name="Важность")
    condition = models.CharField(max_length=50, choices=conditions, verbose_name="Состояние")
    create_at = models.DateTimeField(default=datetime.now() + timedelta(days=1), verbose_name="Время создания")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Запись №{self.id}"

    class Meta:
        verbose_name = _("запись")
        verbose_name_plural = _("записи")


