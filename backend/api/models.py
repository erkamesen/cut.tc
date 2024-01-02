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


# class Profil(User):
#     status = models.CharField(max_length=10,
#                                 choices=STATUS,
#                                 default="Normal",
#                                )
#     class Meta:
#         verbose_name = "Profil"
#         verbose_name_plural = "Profils"

#     def __str__(self):
#         return self.username


class Code(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    base_url = models.CharField(max_length=1000)
    short_code = models.CharField(max_length=50)
    total_click = models.IntegerField(default=0)
    order_type = models.CharField(max_length=50, choices=ORDERS, default="Next")
    redirect_url_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Code"
        verbose_name_plural = "Codes"

    def __str__(self):
        return self.base_url


class RedirectURL(models.Model):
    code = models.ForeignKey(
        Code, on_delete=models.CASCADE, related_name="code")
    redirect_url = models.CharField(max_length=1000)
    total_redirect = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "RedirectURL"
        verbose_name_plural = "RedirectURLs"

    def __str__(self) -> str:
        return self.redirect_url
