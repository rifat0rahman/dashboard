from xmlrpc.client import boolean
from django.db import models
import uuid

from django.forms import URLField
# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    paid = models.BooleanField(default=False)
    def __str__(self) -> str:
        return str(self.email)

class License(models.Model):
    license = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    website = models.URLField(max_length=1000,null=True,blank=True)
    expired = models.BooleanField(default = False)

    def __str__(self) -> str:
        return str(self.license)