import pytest
from datetime import date
from customers.models import Client


@pytest.mark.django_db
def test_create_client():
    client = Client.objects.create(
        name="Test Client",
        paid_until=date(2024, 12, 31),
        on_trial=True,
        schema_name="test_schema",
    )
    assert client.name == "Test Client"
    assert client.paid_until == date(2024, 12, 31)
    assert client.on_trial is True
    assert client.schema_name == "test_schema"
