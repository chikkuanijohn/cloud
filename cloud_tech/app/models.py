from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    id = models.IntegerField(primary_key=True)  # Set id as the primary key
    img = models.FileField(upload_to='course_images/')  # Define where to store the images

    def __str__(self):
        return f"Course ID: {self.id}"  # Optional: String representation of the course

    
