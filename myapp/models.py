from django.db import models
from django.utils.safestring import mark_safe

class ContactMessage(models.Model):
    cname = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    file = models.FileField(upload_to="uploads/", blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def file_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.file.url))

    file_photo.allow_tags = True
    def __str__(self):
        return f"{self.cname} - {self.email}"
