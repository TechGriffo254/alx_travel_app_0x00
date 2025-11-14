# ALX Travel App - Database Modeling and Seeding

A Django-based travel booking application featuring property listings, bookings, and reviews with comprehensive database modeling and seeding capabilities.

## Project Overview

This project demonstrates backend development skills by implementing:
- Relational database models with proper constraints
- RESTful API serializers using Django REST Framework
- Automated database seeding through custom management commands
- Complete CRUD operations for travel booking entities

## Project Structure

```
alx_travel_app_0x00/
├── alx_travel_app/          # Main project directory
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── listings/               # Listings application
│   ├── models.py           # Database models (Listing, Booking, Review)
│   ├── serializers.py      # DRF serializers
│   ├── admin.py            # Django admin configuration
│   ├── management/         # Custom management commands
│   │   └── commands/
│   │       └── seed.py     # Database seeding command
│   └── migrations/         # Database migrations
├── manage.py               # Django management script
└── README.md               # This file
```

## Models

### Listing
Represents a property available for booking.

**Fields:**
- `listing_id` (UUID): Primary key
- `host` (ForeignKey): Reference to User who owns the listing
- `title` (CharField): Listing title
- `description` (TextField): Detailed description
- `location` (CharField): Property location
- `price_per_night` (DecimalField): Nightly rate
- `created_at` (DateTimeField): Creation timestamp
- `updated_at` (DateTimeField): Last update timestamp

**Relationships:**
- One-to-Many with Booking (one listing can have many bookings)
- One-to-Many with Review (one listing can have many reviews)

### Booking
Represents a reservation made by a user.

**Fields:**
- `booking_id` (UUID): Primary key
- `listing` (ForeignKey): Reference to the booked listing
- `user` (ForeignKey): Reference to user making the booking
- `start_date` (DateField): Check-in date
- `end_date` (DateField): Check-out date
- `total_price` (DecimalField): Total booking cost
- `status` (CharField): Booking status (pending, confirmed, canceled)
- `created_at` (DateTimeField): Creation timestamp

**Constraints:**
- Status must be one of: pending, confirmed, canceled
- End date must be after start date (validated in serializer)

### Review
Represents a user's review of a listing.

**Fields:**
- `review_id` (UUID): Primary key
- `listing` (ForeignKey): Reference to reviewed listing
- `user` (ForeignKey): Reference to user who wrote the review
- `rating` (IntegerField): Rating from 1 to 5
- `comment` (TextField): Review text
- `created_at` (DateTimeField): Creation timestamp

**Constraints:**
- Rating must be between 1 and 5

## Serializers

### ListingSerializer
- Converts Listing model instances to JSON
- Includes nested host information (read-only)
- Accepts `host_id` for write operations

### BookingSerializer
- Converts Booking model instances to JSON
- Includes nested listing and user information (read-only)
- Validates that end_date is after start_date
- Accepts `listing_id` and `user_id` for write operations

### ReviewSerializer
- Converts Review model instances to JSON
- Includes nested listing and user information (read-only)
- Validates rating is between 1 and 5
- Accepts `listing_id` and `user_id` for write operations

## Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/TechGriffo254/alx_travel_app_0x00.git
cd alx_travel_app_0x00
```

2. **Install dependencies:**
```bash
pip install django djangorestframework
```

3. **Run migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Create a superuser (optional):**
```bash
python manage.py createsuperuser
```

5. **Seed the database:**
```bash
python manage.py seed
```

6. **Run the development server:**
```bash
python manage.py runserver
```

## Database Seeding

The custom `seed` management command populates the database with sample data:

### What gets seeded:
- **5 Users**: Sample users with credentials
- **5 Listings**: Various properties in different locations
- **3 Bookings**: Sample reservations with different statuses
- **5 Reviews**: Reviews with ratings and comments

### Running the seed command:
```bash
python manage.py seed
```

### Sample Output:
```
Seeding database...
Clearing existing data...
Creating users...
Created 5 users
Creating listings...
Created 5 listings
Creating bookings...
Created 3 bookings
Creating reviews...
Created 5 reviews
Database seeded successfully!
Summary:
  - Users: 5
  - Listings: 5
  - Bookings: 3
  - Reviews: 5
```

## Sample Data

### Sample Listings Created:
1. **Cozy Apartment in Downtown** - New York, NY ($150/night)
2. **Beach House Paradise** - Miami, FL ($300/night)
3. **Mountain Cabin Retreat** - Aspen, CO ($200/night)
4. **Modern Loft in Tech Hub** - San Francisco, CA ($250/night)
5. **Historic Townhouse** - Boston, MA ($180/night)

### Sample Users:
- Username: `user1` - `user5`
- Password: `password123`
- Email: `user1@example.com` - `user5@example.com`

## Admin Interface

Access the Django admin at `http://127.0.0.1:8000/admin/` to manage:
- Listings
- Bookings
- Reviews
- Users

## Key Features

✅ **UUID Primary Keys**: Enhanced security and scalability
✅ **Proper Relationships**: ForeignKey relationships with related_name
✅ **Data Validation**: Serializer-level validation for dates and ratings
✅ **Automated Seeding**: Quick database population for development
✅ **Admin Interface**: Full CRUD operations through Django admin
✅ **Timestamps**: Automatic tracking of creation and update times
✅ **Status Management**: Booking status tracking (pending, confirmed, canceled)

## Database Schema

```
User (Django built-in)
  └─ has many ─> Listing (as host)
  └─ has many ─> Booking (as user)
  └─ has many ─> Review (as user)

Listing
  ├─ belongs to ─> User (as host)
  ├─ has many ─> Booking
  └─ has many ─> Review

Booking
  ├─ belongs to ─> Listing
  └─ belongs to ─> User

Review
  ├─ belongs to ─> Listing
  └─ belongs to ─> User
```

## Development Workflow

1. **Define Models**: Create database schema using Django ORM
2. **Create Serializers**: Set up DRF serializers for API representation
3. **Seed Database**: Use management command to populate with sample data
4. **Test**: Verify data through admin interface or Django shell
5. **Build APIs**: Create views and endpoints (future enhancement)

## Testing

### Verify seeded data in Django shell:
```python
python manage.py shell

from listings.models import Listing, Booking, Review
print(f"Listings: {Listing.objects.count()}")
print(f"Bookings: {Booking.objects.count()}")
print(f"Reviews: {Review.objects.count()}")
```

### Check specific data:
```python
# Get all listings
listings = Listing.objects.all()
for listing in listings:
    print(f"{listing.title} - ${listing.price_per_night}/night")

# Get bookings with confirmed status
confirmed_bookings = Booking.objects.filter(status='confirmed')
print(f"Confirmed bookings: {confirmed_bookings.count()}")

# Get 5-star reviews
top_reviews = Review.objects.filter(rating=5)
print(f"5-star reviews: {top_reviews.count()}")
```

## Technologies Used

- **Django 5.2.7**: Web framework
- **Django REST Framework 3.16.1**: API toolkit
- **Python 3.13**: Programming language
- **SQLite**: Database (development)

## Best Practices Implemented

1. **Model Design**: Proper field types, constraints, and relationships
2. **UUID Keys**: Better security than sequential integers
3. **Serializer Validation**: Data integrity at the API level
4. **Related Names**: Clear reverse relationship access
5. **Timestamps**: Automatic audit trail
6. **Management Commands**: Reusable database operations
7. **Documentation**: Comprehensive README and inline comments

## Repository Information

- **GitHub Repository**: [alx_travel_app_0x00](https://github.com/TechGriffo254/alx_travel_app_0x00)
- **Directory**: alx_travel_app
- **Key Files**:
  - `listings/models.py`
  - `listings/serializers.py`
  - `listings/management/commands/seed.py`

## Future Enhancements

- [ ] Add API views and endpoints
- [ ] Implement authentication and permissions
- [ ] Add search and filtering capabilities
- [ ] Create booking availability checking
- [ ] Add payment integration
- [ ] Implement rating aggregation
- [ ] Add image upload for listings
- [ ] Create booking conflict prevention

## License

This project is part of the ALX Backend Python curriculum.

---

**Author**: TechGriffo254  
**Project**: Milestone 2 - Creating Models, Serializers, and Seeders  
**Date**: November 2025
