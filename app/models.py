from django.db import models

class CodePen(models.Model):
    unique_id = models.CharField(max_length=50, unique=True)
    html_code = models.TextField()
    css_code = models.TextField()
    js_code = models.TextField()

    def __str__(self):
        return self.unique_id
