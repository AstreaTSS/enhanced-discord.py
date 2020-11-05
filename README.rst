Enhanced-dpy (custom discord.py)
=================================

.. image:: https://img.shields.io/pypi/pyversions/discord.py.svg
   :target: https://pypi.python.org/pypi/discord.py
   :alt: PyPI supported Python versions

A modern, easy to use, feature-rich, and async ready API wrapper for Discord written in Python.
Credits to the `original lib by Rapptz <https://github.com/iDutchy/discord.py>`_

**WARNING: This is not the official discord.py lib! This is a custom version to which I add some features that might be useful or just makes things easier for the lazy people. See below which features have been added. This lib will also be kept updated with the BETA version of the original lib! So things may be unstable, please keep that in mind.**

Custom Features
----------------

- **Documentation URL:** https://enhanced-dpy.readthedocs.io/en/latest/index.html
- Added ``Guild.bots`` / ``Guild.humans``
- Added ``Bot.owner`` / ``Bot.owners``
- Added ``Client.try_user`` / ``Bot.try_user``
- ``Guild.icon_url`` and ``User.avatar_url`` return the string in stead of Asset. use icon/avatar url_as to get the Asset
- Merged in ext-colors (https://github.com/MGardne8/DiscordPyColours)
- Using Rapptz/discord.py/tree/neo-docs for documentation
- Added support for ``hex()`` to ``discord.Color``
- Added ``Client.embed_color`` / ``Bot.embed_color``
- Added ``Client.set_embed_color`` / ``Bot.set_embed_color``
- Added ``TextChannel.can_send``
- Added ``Intents.from_list``
- Added support for ``int()`` to ``discord.User``, ``discord.Member``, ``discord.Emoji``, ``discord.Role``, ``discord.Guild``, ``discord.Message``, ``discord.TextChannel``, ``discord.VoiceChannel``, ``discord.CategoryChannel``, ``discord.Attachment`` and ``discord.Message``. This will return their id
- Added support for ``str()`` to ``discord.Message``. This will return the message content
- Added ``Guild.try_member``
- Added ``Context.clean_prefix``
- Added ``Color.nitro_booster``

Key Features
-------------

- Modern Pythonic API using ``async`` and ``await``.
- Proper rate limit handling.
- 100% coverage of the supported Discord API.
- Optimised in both speed and memory.

Installing
----------

**Python 3.5.3 or higher is required**

To install the library without full voice support, you can just run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U enhanced-dpy

    # Windows
    py -3 -m pip install -U enhanced-dpy

To install the development version, do the following:

.. code:: sh

    $ git clone https://github.com/iDutchy/discord.py
    $ cd discord.py
    $ python3 -m pip install -U .[voice]


Optional Packages
~~~~~~~~~~~~~~~~~~

* PyNaCl (for voice support)

Please note that on Linux installing voice you must install the following packages via your favourite package manager (e.g. ``apt``, ``dnf``, etc) before running the above commands:

* libffi-dev (or ``libffi-devel`` on some systems)
* python-dev (e.g. ``python3.6-dev`` for Python 3.6)

Quick Example
--------------

.. code:: py

    import discord

    class MyClient(discord.Client):
        async def on_ready(self):
            print('Logged on as', self.user)

        async def on_message(self, message):
            # don't respond to ourselves
            if message.author == self.user:
                return

            if message.content == 'ping':
                await message.channel.send('pong')

    client = MyClient()
    client.run('token')

Bot Example
~~~~~~~~~~~~~

.. code:: py

    import discord
    from discord.ext import commands

    bot = commands.Bot(command_prefix='>')

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    bot.run('token')

You can find more examples in the examples directory.

Links
------

- `Documentation <https://enhanced-dpy.readthedocs.io/en/latest/index.html>`_
- `Official Discord Server <https://discord.gg/wZSH7pz>`_
- `Discord API <https://discord.gg/discord-api>`_
