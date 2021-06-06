from __future__ import absolute_import, unicode_literals

from celery import shared_task 
from celery.decorators import task
from celery.utils.log import get_task_logger

from django.core.files.storage import default_storage
from fileutils.models import Upload as FileUploads
# from upload.upload_handler import digest
from .score import sensitivity
import urllib.request

logger = get_task_logger(__name__)

@task(name="calc_score")
def calc_score(fil):
    pending_files = FileUploads.objects.filter(score=None)
    for f in pending_files:
        try:
            blob = f.file.read().decode('utf-8')
            score = sensitivity(blob)
        except:
            score = -1
        f.score = score
        f.save()
    return 1