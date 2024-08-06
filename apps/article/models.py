from django.db import models

# Create your models here.
from datetime import timedelta

from django.db.models import CharField, SlugField, TextField, DateTimeField, TextChoices, Manager, ForeignKey, CASCADE, \
    IntegerField, ImageField, SET_NULL, URLField, BooleanField
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from apps.article.choices import Status
from apps.article.managers import PublishManager
from apps.shared.models import BaseModel

from faker import Faker
class Article(BaseModel):
    # managers
    objects = Manager()
    published = PublishManager()

    # fields
    title = CharField(max_length=256)
    slug = SlugField(unique=True)
    body = TextField()
    published_at = DateTimeField(default=timezone.now)
    status = CharField(max_length=15, choices=Status.choices, default=Status.DRAFT)
    category = ForeignKey("article.Category", CASCADE, 'artcicles')
    likes = IntegerField(default=0)
    image = ImageField(upload_to="article/images/")
    owner = ForeignKey("account.Account", SET_NULL, 'article', null=True)
    is_active=BooleanField(default=False)
Article=Faker()

class Category(BaseModel):
    name = CharField(max_length=64)
Category=Faker()

class Comment(BaseModel):
    body = TextField()
    owner = ForeignKey("account.Account", CASCADE, "comments")
    article = ForeignKey("article.Article", CASCADE, "comments")
Comment=Faker()
def advertise_expire(*args, **kwargs):
    return timezone.now()+timedelta(days=3)


class Advertise(BaseModel):
    image = ImageField(upload_to="advertise/images/")
    url = URLField()
    expire_date = DateTimeField(default=advertise_expire)
    phone = PhoneNumberField(region="UZ")
    is_active = BooleanField()
Advertise=Faker()
