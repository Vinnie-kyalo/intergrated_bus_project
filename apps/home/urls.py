# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),



    path("", views.home, name="home"),
    path("buses/", views.available_buses, name="available_buses"),
    path("book/<int:bus_id>/", views.book_bus, name="book_bus"),
    path("payment/<int:booking_id>/", views.process_payment, name="payment"),
]

