from django.db import models

# Create your models here.
from django.db import models
from viewflow.models import Process


class HelloWorldProcess(Process):
    text = models.CharField(max_length=150)
    approved = models.BooleanField(default=False)

class LparaProcess(Process):
    ref_table = models.CharField(max_length=150)
    reason = models.CharField(max_length=150)
    approved = models.BooleanField(default=False)
    appreciation_text = models.CharField(max_length=150)