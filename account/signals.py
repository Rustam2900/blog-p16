from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.mail import send_mail

User = get_user_model()

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Test project'
        message = f'Hi {instance.username}, thank you for registering in blog web sayt.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email, ]
        send_mail(subject, message, email_from, recipient_list)
        print('done -------------------------------')
