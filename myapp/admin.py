"""
This module registers the BandMember model with the Django admin interface,
allowing the BandMember model to be managed via the Django admin site.
"""
from django.contrib import admin
from .models import BandMember

# Register the BandMember model to make it visible in the Django admin site
admin.site.register(BandMember)
