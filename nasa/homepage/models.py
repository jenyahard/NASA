from django.db import models


class Images(models.Model):
    name = models.CharField(max_length=255,
                             verbose_name='Название изображения',
                             )
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name