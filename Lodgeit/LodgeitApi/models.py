from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Staff(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    username = models.CharField(max_length=50, blank=False)
    # company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    owner = models.BooleanField(default=False)
    notification = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username