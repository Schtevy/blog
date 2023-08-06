from django.db import models

class School(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField("start date")
    end_date = models.DateField("end date")

    class Meta:
        ordering = ["start_date"]
        verbose_name_plural = "School"

    def __str__(self):
        return self.name
