from django.db import models

# Create your models here.
class HomeBG(models.Model):
    name1 = models.CharField('BG name1', max_length=30)
    name2 = models.CharField('BG name2', max_length=30)
    about = models.TextField('BG about')
    img = models.ImageField('BG image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeBG'
        verbose_name_plural = 'HomeBGS'


class TourIdea(models.Model):
    name = models.CharField('Idea name', max_length=50)
    about = models.TextField('Idea about')
    img = models.ImageField('Idea image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TourIdea'
        verbose_name_plural = 'TourIdeas'