from django.db import models

# Create your models here.
class todo(models.Model):
    task = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    status = models.CharField(
        max_length=10,
        choices=(("TODO","Todo"),("DONE","Done")),
        default="TODO",
    )
    def __str__(self):
        return f"Task {self.id}"