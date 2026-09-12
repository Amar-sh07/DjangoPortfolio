from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    about = models.TextField()

    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )

    about_image = models.ImageField(
     upload_to="profile/",
     blank=True,
     null=True
     )

    resume = models.FileField(
        upload_to="resume/",
        blank=True,
        null=True
    )

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)

    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_logo(self):
        logos = {
            "HTML": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg",
            "HTML5": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg",

            "CSS": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg",
            "CSS3": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg",

            "JavaScript": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg",

            "Python": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg",

            "Django": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg",
        }

        return logos.get(self.name, "")

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=150)

    description = models.TextField()

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    technologies = models.CharField(
        max_length=300,
        blank=True
    )

    github_link = models.URLField(
        blank=True
    )

    live_link = models.URLField(
        blank=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name

class Achievement(models.Model):
    title = models.CharField(max_length=200)

    description = models.TextField(
        blank=True
    )

    date = models.DateField(
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to="achievements/",
        blank=True,
        null=True
    )

    certificate = models.FileField(
        upload_to="certificates/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)

    email = models.EmailField()

    message = models.TextField()

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} - {self.email}"