from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Author(models.Model):  # наследуемся от класса Model
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_name}'


class Category(models.Model):
    Types = [
        ('tanks', 'Танки'),
        ('Hill', 'Хилы'),
        ('DD', 'ДД'),
        ('Merchants', 'Торговцы'),
        ('Guildmasters', 'Гилдмастеры'),
        ('Questgivers', 'Квестгиверы'),
        ('Blacksmiths', 'Кузнецы'),
        ('Leatherworkers', 'Кожевники'),
        ('Potions', 'Зельевары'),
        ('Spell Masters', 'Мастера закленаний'),
    ]

    name_category = models.CharField(max_length=20, choices=Types, verbose_name='Тип')

    def __str__(self):
        return f'{self.name_category}'


class Notice(models.Model):
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя автора')  # связь «один ко многим» с моделью Author
    datetime_notice = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время поста')  # автоматически добавляемая дата и время создания;
    category_notice = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории')  # связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory);
    header = models.CharField(max_length=255, verbose_name='Заголовок') #  заголовок статьи/новости
    content = RichTextUploadingField(blank=True, null=True, verbose_name='Контент')

    def __str__(self):
        return f'{self.header}: {self.content}: {self.author_name}'

    def get_absolute_url(self):
        return reverse('notice', kwargs={'notice_id': self.pk})


class Responses(models.Model):
    responses_comment = models.ForeignKey(Notice, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Post;
    user_responses = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария')  #  связь «один ко многим» со встроенной моделью User ;
    text_responses = models.TextField(max_length=255, verbose_name='Текст комментария')  # текст комментария;
    datetime_responses = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время комментария')  # дата и время создания комментария;
    accepted = models.BooleanField(default=False, verbose_name='Принято/Отклонено')

    def __str__(self):
        return f'{self.text_responses}: {self.user_responses}: {self.responses_comment}: {self.accepted}'

    def get_absolute_url(self):
        return reverse('responses', kwargs={'pk': self.pk})


class SubscribersCategory(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Категории подписчиков'

    def __str__(self):
        return f'{self.category}: {self.subscriber}'

