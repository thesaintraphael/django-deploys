from django.core.mail import EmailMessage

from celery import shared_task
from celery.utils.log import get_task_logger

from core.env import get_env_variable


logger = get_task_logger("core")


@shared_task
def send_email():
    logger.info("Executing periodic task")

    email_to = get_env_variable("EMAIL_TO")

    EmailMessage(subject="Test email", body="This is a test email", to=(email_to,))

    logger.info("Email is sent")
