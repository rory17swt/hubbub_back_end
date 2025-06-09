from django.db import models

# Create your models here.
class Question(models.Model):
    event = models.ForeignKey(
        to='events.Event',
        related_name='questions',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        to='users.User',
        related_name='questions',
        on_delete=models.CASCADE
    )
    question = models.TextField(max_length=1000)
    response = models.TextField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question