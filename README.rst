============
Igor Project
============

[![Analytics](https://ga-beacon.appspot.com/UA-71640963-2/welcome-page)](https://github.com/Rootex/IGOR)

[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badge/)


The project is aimed to develop an AI learning platform
by gamification. It will be web based and consist of several
interesting analysis modules to better understand the
learning habit of developers and in turn tune their instance
to meet the requirements they need to learn better.

Documentation can be found in the "docs" directory.

Quick start
-----------

1. Add "puzzles" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'puzzles',
    ]

2. Include the puzzles URLconf in your project urls.py like this::

    url(r'^puzzles/', include('puzzles.urls')),

3. Run `python manage.py migrate` to create the puzzles models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a puzzles (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/puzzles/ to see the created puzzles and attempt them.
