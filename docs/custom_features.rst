.. currentmodule:: discord

.. _custom_features:

Intro
=====
enhanced-dpy was made to add some extra features that make it just a bit easier. This custom version of discord.py will always remain up-to-date with the beta version, so not everything might work or be stable. 

Custom Features
---------------
Here are the custom features listed that have been added to enhanced-dpy. You can refer to the changelog to see in what version they were added!

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
- Added ``Permissions.admin`` as alias to ``Permissions.administrator``