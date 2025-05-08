from django.db import models
class Feedback(models.Model):
    choices=[('general', 'General'), ('bug', 'Bug Report'), ('feature', 'Feature Request')]
    name = models.CharField(max_lenght=100)
    email = models.EmailField()
    feedback_type = forms.ChoiseField(choices=)
    message = models.CharField()