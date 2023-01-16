from __future__ import absolute_import

import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("core", include=["app.tasks"])


app.conf.beat_schedule = {
    "send_email_report": {
        "task": "app.tasks.send_email",
        "schedule": crontab(minute="*/1"),
    },
}


app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
