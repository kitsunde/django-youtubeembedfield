Django YouTube Embed Field
==========================

A field that accepts regular YouTube links and saves the embed ones. It just
wraps the regular URLField and converts the input to YouTube embedded ones.

Installation
------------

To get the latest stable release from PyPi::

    $ pip install django-youtubeembedfield

To get the latest commit from GitHub::

    $ pip install -e git+git://github.com/Celc/django-youtubeembedfield.git#egg=youtubeembedfield

Usage
-----

Add the field to your model::

    import youtubeembedfield

    class MyAwesomeModel(models.Model):
        youtube = youtubeembedfield.YoutubeEmbedField()

Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch
