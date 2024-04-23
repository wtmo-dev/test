import time
from celery import shared_task
from django.conf import settings
import requests

@shared_task
def add(user_id, approval_request_data):
    # res = requests.get(f"{settings.TOSS_HR_SYSTEM}/people/{user_id}")
    # res.raise_for_status()
    # person_data = res.json()
    # approval_request_data.update(person_data)
    
    return approval_request_data

@shared_task
def ppp():
    print("1111111111111")
    time.sleep(5)
    return {"success": "159456"}


@shared_task
def add(user_id, approval_request_data):
    res = requests.get(f"{settings.TOSS_HR_SYSTEM}/people/{user_id}")
    res.raise_for_status()
    person_data = res.json()
    approval_request_data.update(person_data)
    return approval_request_data