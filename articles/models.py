from django.db import models
from django.shortcuts import reverse


class Articles(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.TextField()
    long_content = models.TextField()
    category = models.CharField(max_length=50)
    auther_name = models.CharField(max_length=50)
    created_at= models.DateField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'Articles'


    def get_detail_url(self):
        return reverse('articles:detail', args=[self.pk])