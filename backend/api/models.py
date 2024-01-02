from django.db import models
from django.contrib.auth.models import User
# Create your models here.




STATUS = [
    ("Normal", "Normal"),
    ("Premium", "Premium"),
]

ORDERS = [
    ("Next", "Next"),
    ("Day", "Day"),
    ("Week", "Week"),
    ("Month", "Month"),
    ("Solar", "Solar"),
    ("Random", "Random"),
]


class Profil(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profil",
    )

    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default="Normal",
                              )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.user.username


class BaseURL(models.Model):
    base_url = models.CharField(max_length=1000)
    short_code = models.CharField(max_length=50)
    total_click = models.IntegerField(default=0)
    order_type = models.CharField(max_length=50, choices=ORDERS, default="Next")
    redirect_url_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "BaseURL"
        verbose_name_plural = "BaseURLs"

    def __str__(self):
        return self.base_url


class RedirectURL(models.Model):
    base_url = models.ForeignKey(
        BaseURL, on_delete=models.CASCADE, related_name="redirect_url")
    redirect_url = models.CharField(max_length=1000)
    total_redirect = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "RedirectURL"
        verbose_name_plural = "RedirectURLs"

    def __str__(self) -> str:
        return self.redirect_url
