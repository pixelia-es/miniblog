# miniblog engine #

miniblog is a (really) small blog engine to demonstrate the use of [Django][].
It allows to create articles using the Django-based admin site, view a list of
them and a detailed view of each one.

There are two branches in the repository. `master` contains the pure Django
implementation and `app_engine` a version ready to run on [Google App Engine][].
To start developing, clone the repository and edit your `local_settings.py` file
to customize your DB settings.

This code was discussed in the Spanish podcast [We.Developers][] as part of an
episode centered in Python and Django development.


[Django]: http://www.djangoproject.com/ "Django Project"
[Google App Engine]: http://developers.google.com/appengine/ "Google App Engine"
[We.Developers]: http://wedevelopers.com/2012/07/22/we-developers-007-python-django/ "We.Developers 007 - Python & Django"
