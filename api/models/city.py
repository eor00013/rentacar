from django.db import models


class City(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False, verbose_name='Name')
    
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False, verbose_name='Creation date')
    
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name='Update date')

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name