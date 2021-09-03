from django.db import models

# Create your models here.
class photo(models.Model):
    tittle=models.TextField()
    des=models.TextField()
    img=models.ImageField(upload_to='pictures')

    def __str__(self):
        return format(self.tittle)


