from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import loader, TemplateDoesNotExist
from django.urls import reverse
from .models import Bus, Route, Booking, Passenger, Payment
import datetime

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    try:
        load_template = request.path.split('/')[-1]
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template
        html_template = loader.get_template(f'home/{load_template}')
        return HttpResponse(html_template.render(context, request))
    except TemplateDoesNotExist:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except Exception:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

# 🏠 Home View: Displays Available Routes
def home(request):
    routes = Route.objects.all()
    return render(request, "home/index.html", {"routes": routes})

# 🚍 Available Buses View
def available_buses(request):
    if request.method == "POST":
        from_location = request.POST.get("from")
        to_location = request.POST.get("to")
        travel_date = request.POST.get("date")

        # Validate input
        if not from_location or not to_location or not travel_date:
            return render(request, "home/search_bus.html", {"error": "All fields are required."})

        # ❌ Prevent Past Date Bookings
        today = datetime.date.today()
        try:
            travel_date = datetime.datetime.strptime(travel_date, "%Y-%m-%d").date()
        except ValueError:
            return render(request, "home/search_bus.html", {"error": "Invalid date format."})

        if travel_date < today:
            return render(request, "home/search_bus.html", {"error": "You cannot book for past dates."})

        # Check if route exists
        route = Route.objects.filter(from_location=from_location, to_location=to_location).first()
        
        if not route:
            return render(request, "home/search_bus.html", {"error": "No available buses for this route."})

        # Fetch Buses assigned to this route
        buses = Bus.objects.filter(route=route)

        return render(request, "home/buses.html", {"buses": buses, "travel_date": travel_date})

    return render(request, "home/search_bus.html")

# 🎟 Book Bus View
def book_bus(request, bus_id):
    bus = get_object_or_404(Bus, id=bus_id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        seats = request.POST.get("seats")

        print(f"DEBUG: Received - Name: {name}, Email: {email}, Phone: {phone}, Seats: {seats}")

        # ✅ Validate Input Fields
        if not name or not email or not phone or not seats:
            return render(request, "home/add_passenger.html", {"bus": bus, "error": "All fields are required."})

        try:
            passenger = Passenger.objects.create(name=name, email=email, phone=phone)
            booking = Booking.objects.create(passenger=passenger, bus=bus, seats_booked=int(seats), status="Pending")

            return redirect("payment", booking_id=booking.id)

        except Exception as e:
            print(f"ERROR: {e}")
            return render(request, "home/add_passenger.html", {"bus": bus, "error": "Something went wrong! Please try again."})

    return render(request, "home/add_passenger.html", {"bus": bus})

# 💳 Payment Processing View
def process_payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    amount = booking.seats_booked * booking.bus.price_per_seat

    if request.method == "POST":
        Payment.objects.create(
            booking=booking,
            amount=amount,
            payment_method="Mpesa",
            payment_status="Completed"
        )
        booking.status = "Confirmed"
        booking.save()
        return render(request, "home/ticket.html", {"booking": booking})

    return render(request, "home/payment.html", {"booking": booking, "amount": amount})
