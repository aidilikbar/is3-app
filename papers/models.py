from django.db import models

class Paper(models.Model):
    paper_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=500)
    year = models.IntegerField(null=True, blank=True)
    authors = models.TextField(null=True, blank=True)  # Store as a comma-separated string
    abstract = models.TextField(null=True, blank=True)
    url = models.URLField()
    open_access_pdf = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title