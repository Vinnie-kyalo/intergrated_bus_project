from django.contrib import admin
from .models import Route, Bus, Passenger, Booking, Payment

admin.site.register(Route)
admin.site.register(Bus)
admin.site.register(Passenger)
admin.site.register(Booking)
admin.site.register(Payment)
