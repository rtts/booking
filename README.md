Booking.superformosa.com
========================

This repository contains the source code of
[booking.superformosa.com](https://booking.superformosa.com/), a
booking system created by [Return to the Source](https://rtts.eu/),
provided here for everyone to use under the [GPLv3](LICENSE) license
as part of our free and open source philosophy.


Installation
------------

Install Python and run the following commands:

    pip install -r requirements.txt
    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py runserver


Usage
-----

- Visit http://localhost:8000/admin/booking/photoshoot/add/ to add a photoshoot
- Visit http://localhost:8000/<slug>/add/ to generate timeslots
- Visit http://localhost:8000/<slug>/ to reserve a timeslot
