from collections.abc import Iterable
from typing import Any
from django.db import models

# Create your models here.



class URLs(models.Model):
    base_url = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    total_click = models.PositiveIntegerField(default=0)
    
    def __str__(self)  -> str:
        return self.base_url
    
    
    class Meta:
            db_table = 'URLs'
            managed = True
            verbose_name = 'URL'
            verbose_name_plural = 'URLs'

    
class Redirects(models.Model):
    redirect_url = models.CharField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)
    base_url = models.ForeignKey(URLs, on_delete=models.CASCADE, related_name="url")

    def __str__(self) -> str:
        return self.redirect_url
    
    class Meta:
        db_table = 'Redirect_Urls'
        managed = True
        verbose_name = 'Redirect URL'
        verbose_name_plural = 'Redirect URLs'
    
    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
         return super().save(force_insert, force_update, using, update_fields)