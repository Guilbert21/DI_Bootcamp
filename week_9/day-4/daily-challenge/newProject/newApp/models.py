from django.db import models

class Image(models.Model):
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='imag/%y')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.caption
    