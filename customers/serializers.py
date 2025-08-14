from rest_framework import serializers
from .models import Client, Domain


class TenantSerializer(serializers.ModelSerializer):
    primary_domain = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ["schema_name", "name", "paid_until", "on_trial", "primary_domain"]

    def get_primary_domain(self, obj):
        domain = Domain.objects.filter(tenant=obj, is_primary=True).first()
        return domain.domain if domain else None
