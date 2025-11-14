"""Admin configuration for listings app."""
from django.contrib import admin
from .models import Listing, Booking, Review


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    """Admin interface for Listing model."""
    list_display = ['title', 'host', 'location', 'price_per_night', 'created_at']
    list_filter = ['location', 'created_at']
    search_fields = ['title', 'description', 'location']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Admin interface for Booking model."""
    list_display = ['booking_id', 'listing', 'user', 'start_date', 'end_date', 'status']
    list_filter = ['status', 'start_date']
    search_fields = ['listing__title', 'user__username']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Admin interface for Review model."""
    list_display = ['listing', 'user', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['listing__title', 'user__username', 'comment']
