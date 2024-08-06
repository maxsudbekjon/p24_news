from django.db.models import Manager
from django.db.models.query import QuerySet

from apps.article.choices import Status
from django.utils import timezone

class PublishManager(Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(status=Status.PUBLISHED)
        return queryset
class ActiveAdvertiseManager(Manager):
    def get_queryset(self) -> QuerySet:
        quertset= super().get_queryset()
        quertset.filter(is_active=True and  expire_date != timezone.now() )
        return quertset
  
