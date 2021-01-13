.. currentmodule:: discord

.. _custom_features:

Intro
=====
enhanced-dpy was made to add some extra features that make it just a bit easier. This custom version of discord.py will always remain up-to-date with the beta version, so not everything might work or be stable. 

Custom Features
---------------
Here are the custom features listed that have been added to enhanced-dpy. You can refer to the changelog to see in what version they were added!

- **Documentation URL:** https://enhanced-dpy.readthedocs.io/en/latest/index.html
- Added :attr:`Guild.bots` and :attr:`Guild.humans`
- Added :attr:`Client.owner` and :attr:`Client.owners`
- Added :meth:`Client.try_user`
- :attr:`Guild.icon_url` and :attr:`User.avatar_url` return the string in stead of Asset. use icon/avatar url_as to get the :class:`Asset`
- Merged in ext-colors (https://github.com/MGardne8/DiscordPyColours)
- Using Rapptz/discord.py/tree/neo-docs for documentation
- Added support for ``hex()`` to :class:`Color`
- Added :attr:`Client.embed_color`
- Added :meth:`Client.set_embed_color`
- Added :attr:`TextChannel.can_send`
- Added :meth:`Intents.from_list`
- Added support for ``int()`` to :class:`User`, :class:`Member`, :class:`Emoji`, :class:`Role`, :class:`Guild`, :class:`Message`, :class:`TextChannel`, :class:`VoiceChannel`, :class:`CategoryChannel`, :class:`Attachment` and :class:`Message`. This will return their id
- Added support for ``str()`` to :class:`Message`. This will return the message content
- Added :meth:`Guild.try_member`
- Added :attr:`Context.clean_prefix <.ext.commands.Context.clean_prefix>`
- Added :meth:`Colour.nitro_booster`
- Added :attr:`Permissions.admin` as alias to :attr:`Permissions.administrator`
- Added :attr:`CogMeta.aliases <.ext.commands.CogMeta.aliases>`
- Added :attr:`Bot.case_insensitive_prefix <.ext.commands.Bot.case_insensitive_prefix>`
- Added ``silent`` kwarg to :meth:`Message.delete`