from django.db.models import Q
from myapp.models import Address


def search_address(area=None, zipcode=None, sector=None):
    # Create an empty query set
    addresses = Address.objects.none()

    # Check which input parameter is provided and add corresponding filter to the query set
    if area:
        addresses = Address.objects.filter(area__icontains=area)
    if zipcode:
        addresses = Address.objects.filter(zip_code__icontains=zipcode)
    if sector:
        addresses = Address.objects.filter(
            Q(sector__icontains=sector) | Q(subsector__icontains=sector))

    return addresses
