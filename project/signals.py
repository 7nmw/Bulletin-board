from django.db.models.signals import post_save, m2m_changed, pre_save
from django.core.mail import send_mail, EmailMultiAlternatives
from .models import Responses, User, Notice, SubscribersCategory
from django.dispatch import receiver


#оповещение новом коментарии
@receiver(post_save, sender=Responses)
def notify_user_subscribe(sender, instance, created, **kwargs):
    if created:
        subject = f'Новый отклик'
    else:
        subject = f'Ваш отклик одобрен'

    send_mail(
        subject=subject,
        message=f'Вам оставлен новый отклик: {instance.text_responses}',
        from_email='win.c4ester@yandex.ru',
        recipient_list=[f'{instance.responses_comment.author_name.email}'],
    )


#оповещение новой статьи в категории
@receiver(post_save, sender=Notice)
def notify_user_subscribe(sender, instance, created, **kwargs):
    subject = f'Новый публикация'
    send_mail(
        subject=subject,
        message=f'Новая публикая в разделе: {instance.header}',
        from_email='win.c4ester@yandex.ru',
        recipient_list=[f'{instance.author_name.email}'],
    )

#оповещение о подписке на категорию
@receiver(post_save, sender=SubscribersCategory)
def notify_user_subscribe(sender, instance, created, **kwargs):
    subject = f'Подписка оформлена'
    send_mail(
        subject=subject,
        message=f'Вы успешно подписались на категорию: {instance.category.name_category}',
        from_email='win.c4ester@yandex.ru',
        recipient_list=[f'{instance.subscriber.email}'],
    )