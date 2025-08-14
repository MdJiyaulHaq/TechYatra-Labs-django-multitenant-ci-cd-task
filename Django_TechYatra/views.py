from django.shortcuts import render
from django.db import connection
from django_tenants.utils import get_public_schema_name
from customers.models import Client, Domain


def home(request):
    """
    Public schema: show tenant table with quick links.
    Tenant schema: show tenant-specific quick links.
    """
    is_public = connection.schema_name == get_public_schema_name()

    scheme = request.scheme
    port = request.get_port()
    port_suffix = "" if port in ("80", "443") else f":{port}"

    ctx = {"is_public": is_public}

    if is_public:
        tenants = []
        # list tenants with a primary domain
        for c in Client.objects.all().order_by("schema_name"):
            d = Domain.objects.filter(tenant=c, is_primary=True).first()
            if not d:
                continue
            base = f"{scheme}://{d.domain}{port_suffix}"
            tenants.append(
                {
                    "name": c.name,
                    "schema_name": c.schema_name,
                    "domain": d.domain,
                    "home_url": f"{base}/",
                    "admin_url": f"{base}/admin/",
                    "products_url": f"{base}/api/products/",
                }
            )
        ctx["tenants"] = tenants
    else:
        host = request.get_host().split(":")[0]  # current tenant domain
        base = f"{scheme}://{host}{port_suffix}"
        ctx.update(
            {
                "current_domain": host,
                "tenant_admin_url": f"{base}/admin/",
                "tenant_products_url": f"{base}/api/products/",
            }
        )

    return render(request, "home.html", ctx)
