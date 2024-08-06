from django.db.models import TextChoices, BooleanField


class Status(TextChoices):
    DRAFT = ("df", "Draft"),
    PUBLISHED = ("pb", "Published")

