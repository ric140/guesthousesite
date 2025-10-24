# --- START OF CORRECTED FILE app.py ---

from flask import Flask, render_template, request, redirect, url_for
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

# --- MOCK DATABASE (Room Information Updated) ---
MOCK_DATA = {
    "rooms": [
        {
            "id": "balcony-king",
            "name": "Balcony King",
            "description": "A beautifully appointed room with a plush king-sized bed and a private balcony offering charming city views. Perfect for couples or solo travelers seeking a touch of luxury.",
            "price_per_night": 15.00,
            "image_url": "static/images/room_balcony_king.png",
            "amenities": ["Free WiFi", "Air Conditioning", "Private Balcony", "Plush Linens"]
        },
        {
            "id": "deluxe-triple",
            "name": "Deluxe Triple",
            "description": "This spacious room features a comfortable king bed plus an additional full bed, making it ideal for small groups or families. Modern amenities ensure a comfortable stay.",
            "price_per_night": 13.00,
            "image_url": "static/images/room_deluxe_triple.jpg",
            "amenities": ["Free WiFi", "Air Conditioning", "Extra Bed", "Work Desk"]
        },
        {
            "id": "family-quad",
            "name": "Family Quad",
            "description": "Designed for families, this large room features two queen-sized beds and ample space to relax. It's the perfect home base for your Kampot adventures.",
            "price_per_night": 15.00,
            "image_url": "static/images/room_family_quad.jpg",
            "amenities": ["Free WiFi", "Air Conditioning", "Two Queen Beds"]
        }
    ],
    "experiences": [
        # Data is here for future use
    ],
    "services": [
        # ... services data ...
    ],
    "testimonials": [
        # ... testimonials data ...
    ],
    "guesthouse_info": {
        "name": "Good Day Kampot Guesthouse",
        "phone": "+855 15 424 147",
        "email": "gooddaykampot@gmail.com",
        "address": "J53M+PH, Krong Kampot, Cambodia",
        "booking_url": "https://www.booking.com/hotel/kh/good-day-kampot-guesthouse.html?aid=304142&label=gen173nr-10CAEoggI46AdIM1gEaHiIAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGoAgG4AqTFlMYGwAIB0gIkZWE5YzU2ZGYtNzkyNC00ZDZlLTlmNjktNTkyZGQwMDFlYmJk2AIB4AIB&sid=42fbf4a10a1612285da95e998a881ac5&dest_id=14744613&dest_type=hotel&dist=0&group_adults=2&group_children=0&hapos=1&hpos=1&no_rooms=1&req_adults=2&req_children=0&room1=A%2CA&sb_price_type=total&sr_order=popularity&srepoch=1757749960&srpvid=4cfa376167ea04ad&type=total&ucfs=1&"
    }
}

# --- FLASK ROUTES ---
@app.route('/')
def home():
    return render_template('index.html', guesthouse=MOCK_DATA['guesthouse_info'], rooms=MOCK_DATA['rooms'], services=MOCK_DATA['services'], testimonials=MOCK_DATA['testimonials'])

@app.route('/about')
def about():
    return render_template('about.html', guesthouse=MOCK_DATA['guesthouse_info'])

@app.route('/rooms')
def rooms():
    return render_template('rooms.html', rooms=MOCK_DATA['rooms'], guesthouse=MOCK_DATA['guesthouse_info'])

@app.route('/experiences')
def experiences():
    # Per our MVP plan, this link is removed from the nav, but if a user types it in, we redirect them home.
    return redirect(url_for('home'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # ... contact form logic ...
        return render_template('contact.html', guesthouse=MOCK_DATA['guesthouse_info'], success=True)
    return render_template('contact.html', guesthouse=MOCK_DATA['guesthouse_info'], success=False)

@app.route('/booking')
def booking_step1():
    # Per our MVP plan, all "Book Now" buttons now go directly to the external booking URL.
    # This route now redirects there, instead of to a local template.
    return redirect(MOCK_DATA['guesthouse_info']['booking_url'])

# This is the single, correct block for building the site.
if __name__ == '__main__':
    freezer.freeze()

# --- END OF CORRECTED FILE app.py ---