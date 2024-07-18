from django.db import models

# Create your models here.
class Entries(models.Model):
  title = models.CharField(max_length=60)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  content = models.TextField()

  def __str__(self):
    return self.title
