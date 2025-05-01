from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    content = models.TextField(verbose_name="Matn")
    views = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='news_images/', verbose_name="Rasm")
    date_posted = models.DateTimeField(default=timezone.now, verbose_name="Sana")
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        ordering = ['-date_posted']

class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    subject = models.CharField(max_length=100, verbose_name="Fan")
    photo = models.ImageField(upload_to='teachers_photos/', verbose_name="Rasm")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ustoz"
        verbose_name_plural = "Ustozlar"