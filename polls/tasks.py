from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_email_task(subject, message, from_email):
    send_mail(subject, message, settings.NOREPLY_EMAIL, [from_email])

# def send_email_task(subject, message, from_email, send_at):
#     now_utc = datetime.now(timezone.utc)
#     send_at = send_at.astimezone(timezone.utc)
#     if send_at > now_utc:
#         delay = (send_at - now_utc).total_seconds()
#         send_mail.apply_async(args=[subject, message, settings.NOREPLY_EMAIL, [from_email]], countdown=delay)
