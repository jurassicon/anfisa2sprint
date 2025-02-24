from django.db import models

from core.models import PublishedModel


class Title(models.Model):
    title = models.CharField('Название', max_length=256)

    class Meta:
        abstract = True


class Slag(models.Model):
    slug = models.SlugField('Слаг', max_length=64, unique=True)

    class Meta:
        abstract = True


class Category(PublishedModel, Title, Slag):
    output_order = models.PositiveSmallIntegerField(
        'Порядок отображения',
        default=100
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Topping(PublishedModel, Title, Slag):
    class Meta:
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топпинги'

    def __str__(self):
        return self.title


class Wrapper(PublishedModel, Title):
    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Уникальное название обёртки, не более 256 символов.'
    )
    class Meta:
        verbose_name = 'объект «Обёртка»'
        verbose_name_plural = 'Обёртки'

    def __str__(self):
        return self.title


class IceCream(PublishedModel, Title):
    description = models.TextField(verbose_name = 'Описание')
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name = 'Обёртка'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория'
    )
    toppings = models.ManyToManyField(Topping, verbose_name = 'Топпинги')
    is_on_main = models.BooleanField(default=False, verbose_name = 'На главную')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженое'
        ordering = ('title',)

    def __str__(self):
        return self.title
