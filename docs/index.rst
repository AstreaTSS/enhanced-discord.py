.. discord.py documentation master file, created by
   sphinx-quickstart on Fri Aug 21 05:43:30 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to discord.py
===========================

.. image:: /images/snake.svg
.. image:: /images/snake_dark.svg

discord.py is a modern, easy to use, feature-rich, and async ready API wrapper
for Discord.
Credits to original lib by `Rappts <https://github.com/iDutchy/discord.py>`_

**WARNING: This is not the official discord.py lib! This is a custom version to which I add some features that might be useful or just makes things easier for the lazy people. See below which features have been added. This lib will also be kept updated with the BETA version of the original lib! So things may be unstable, please keep that in mind.**

Custom Features
---------------

- **Documentation URL:** https://enhanced-dpy.readthedocs.io/en/latest/index.html
- Added ``Guild.bots`` / ``Guild.humans``
- Added ``Bot.owner`` / ``Bot.owners``
- Merged in ext-colors (https://github.com/MGardne8/DiscordPyColours)
- Using Rapptz/discord.py/tree/neo-docs for documentation
- Adding support for ``hex()`` to ``discord.Color``

Features
--------

- Modern Pythonic API using ``async``\/``await`` syntax
- Sane rate limit handling that prevents 429s
- Implements the entire Discord API
- Command extension to aid with bot creation
- Easy to use with an object oriented design
- Optimised for both speed and memory

Documentation Contents
-----------------------

.. toctree::
   :maxdepth: 2

   intro
   quickstart
   migrating
   logging
   api

Extensions
-----------

.. toctree::
  :maxdepth: 3

  ext/commands/index.rst
  ext/tasks/index.rst


Additional Information
-----------------------

.. toctree::
    :maxdepth: 2

    discord
    intents
    faq
    whats_new
    version_guarantees

If you still can't find what you're looking for, try in one of the following pages:

* :ref:`genindex`
* :ref:`search`
