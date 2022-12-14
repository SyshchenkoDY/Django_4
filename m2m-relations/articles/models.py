from django.db import models


class Tag(models.Model):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    name = models.CharField(max_length=30, verbose_name='Тег')

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tag, through='Scope', related_name='tags_scope',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, verbose_name='Тег', on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(Tag, default=False)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


