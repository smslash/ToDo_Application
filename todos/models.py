from django.db import models

# Need to create models

class Todo(models.Model):
    content = models.TextField()