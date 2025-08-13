from django.db import models  # noqa

# Create your models here.
from django_tenants.models import TenantMixin, DomainMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField(null=True, blank=True)
    on_trial = models.BooleanField(default=True)
    # schema_name is required by TenantMixin
    # auto-create schema on save()


class Domain(DomainMixin):
    pass
