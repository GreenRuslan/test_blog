from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Аффтар",
        on_delete=models.CASCADE
    )
    title = models.CharField("Текст заголовка", max_length=130)
    text_short = models.TextField("Краткое описание", max_length=400)
    text = models.TextField("Текст статьи")
    date_create = models.DateTimeField("Дата создания поста", auto_now=True)
    description = models.CharField("Описание всего этого добра", max_length=200)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title


class Comments(models.Model):

    user = models.ForeignKey(
        User,
        verbose_name="Юзверь",
        on_delete=models.CASCADE
    )
    pos = models.ForeignKey(
        Post,
        verbose_name="Пост",
        on_delete=models.CASCADE
    )
    text = models.TextField("Коммент")
    created = models.DateTimeField("Дата коммента", auto_now=True, null=True)
    moderation = models.BooleanField("Модерация", default=False)

    class Meta:
        verbose_name="Коммент"
        verbose_name_plural="Комменты"

        def __str__(self):
            return "{}".format(self.user)
