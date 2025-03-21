from django.db import models
from django.contrib.auth.models import User


class TODOO(models.Model):

    title=models.CharField(max_length=25)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task_number = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f"{self.task_number}.{self.title}"
    
    class Meta:
        ordering = ['-date']