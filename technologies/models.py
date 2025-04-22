from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=100)
    aim = models.TextField()
    image = models.CharField(max_length=200)  # ścieżka do pliku
    progress_value = models.IntegerField()
    direction = models.CharField(max_length=10, blank=True, null=True)  # np. 'left' lub 'right'

    def progress(self):
        if self.direction:
            return [self.progress_value, self.direction]
        return self.progress_value

    def __str__(self):
        return self.name
