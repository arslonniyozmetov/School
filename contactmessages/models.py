from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.created_at}"