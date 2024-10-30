from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Staff(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    username = models.CharField(max_length=50, blank=False)
    owner = models.BooleanField(default=False)
    notification = models.BooleanField(default=True)

    # Add unique `related_name` values to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name="staff_user_groups",  # Avoids clash with `auth.User.groups`
        blank=True,
        help_text="The groups this user belongs to."
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name="staff_user_permissions",  # Avoids clash with `auth.User.user_permissions`
        blank=True,
        help_text="Specific permissions for this user."
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username