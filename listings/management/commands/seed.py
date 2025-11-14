"""Management command to seed the database with sample data."""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review
from decimal import Decimal
from datetime import date, timedelta


class Command(BaseCommand):
    """Seed database with sample listings, bookings, and reviews."""
    help = 'Seeds the database with sample listing data'

    def handle(self, *args, **kwargs):
        """Execute the seed command."""
        self.stdout.write('Seeding database...')

        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Review.objects.all().delete()
        Booking.objects.all().delete()
        Listing.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()

        # Create sample users
        self.stdout.write('Creating users...')
        users = []
        for i in range(1, 6):
            user = User.objects.create_user(
                username=f'user{i}',
                email=f'user{i}@example.com',
                password='password123',
                first_name=f'First{i}',
                last_name=f'Last{i}'
            )
            users.append(user)
        self.stdout.write(self.style.SUCCESS(f'Created {len(users)} users'))

        # Create sample listings
        self.stdout.write('Creating listings...')
        listings_data = [
            {
                'title': 'Cozy Apartment in Downtown',
                'description': 'A beautiful apartment in the heart of the city with amazing views.',
                'location': 'New York, NY',
                'price_per_night': Decimal('150.00'),
            },
            {
                'title': 'Beach House Paradise',
                'description': 'Luxurious beach house with private access to the beach.',
                'location': 'Miami, FL',
                'price_per_night': Decimal('300.00'),
            },
            {
                'title': 'Mountain Cabin Retreat',
                'description': 'Peaceful cabin in the mountains, perfect for a getaway.',
                'location': 'Aspen, CO',
                'price_per_night': Decimal('200.00'),
            },
            {
                'title': 'Modern Loft in Tech Hub',
                'description': 'Stylish loft in the tech district with all amenities.',
                'location': 'San Francisco, CA',
                'price_per_night': Decimal('250.00'),
            },
            {
                'title': 'Historic Townhouse',
                'description': 'Charming townhouse with historical significance.',
                'location': 'Boston, MA',
                'price_per_night': Decimal('180.00'),
            },
        ]

        listings = []
        for i, listing_data in enumerate(listings_data):
            listing = Listing.objects.create(
                host=users[i % len(users)],
                **listing_data
            )
            listings.append(listing)
        self.stdout.write(self.style.SUCCESS(f'Created {len(listings)} listings'))

        # Create sample bookings
        self.stdout.write('Creating bookings...')
        bookings = []
        today = date.today()
        for i, listing in enumerate(listings[:3]):
            booking = Booking.objects.create(
                listing=listing,
                user=users[(i + 1) % len(users)],
                start_date=today + timedelta(days=i * 7),
                end_date=today + timedelta(days=i * 7 + 3),
                total_price=listing.price_per_night * 3,
                status='confirmed' if i % 2 == 0 else 'pending'
            )
            bookings.append(booking)
        self.stdout.write(self.style.SUCCESS(f'Created {len(bookings)} bookings'))

        # Create sample reviews
        self.stdout.write('Creating reviews...')
        reviews_data = [
            {'rating': 5, 'comment': 'Amazing place! Highly recommended.'},
            {'rating': 4, 'comment': 'Great location, very comfortable.'},
            {'rating': 5, 'comment': 'Perfect for a weekend getaway.'},
            {'rating': 3, 'comment': 'Good but could be cleaner.'},
            {'rating': 4, 'comment': 'Nice amenities and friendly host.'},
        ]

        reviews = []
        for i, review_data in enumerate(reviews_data):
            review = Review.objects.create(
                listing=listings[i % len(listings)],
                user=users[(i + 2) % len(users)],
                **review_data
            )
            reviews.append(review)
        self.stdout.write(self.style.SUCCESS(f'Created {len(reviews)} reviews'))

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
        self.stdout.write(f'Summary:')
        self.stdout.write(f'  - Users: {len(users)}')
        self.stdout.write(f'  - Listings: {len(listings)}')
        self.stdout.write(f'  - Bookings: {len(bookings)}')
        self.stdout.write(f'  - Reviews: {len(reviews)}')
