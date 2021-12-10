import discord 
import asyncio 
import random
from discord import Member, Guild
from discord import User
from discord.ext.commands import Bot
from discord.ext import commands

client = commands.Bot(command_prefix='/', intents=discord.Intents.all())

beer = [
        'https://tenor.com/view/drinking-drink-cheers-toast-drunk-gif-17446146',        
        'https://tenor.com/view/anime-smile-drinking-beer-gif-12546881',
        'https://tenor.com/view/gintoki-anime-animation-beer-drip-gif-5081999',
        'https://tenor.com/view/anime-drinking-beer-happy-hour-gif-11166531',
        'https://tenor.com/view/jojo-anime-drink-beer-guys-gif-16740533',
        'https://tenor.com/view/yesterday-wo-utatte-drink-beer-smile-anime-gif-17361629'
        ]

waifu = ['ist Emilia https://tenor.com/view/emilia-tan-smile-re-zero-anime-windy-gif-17500641', 'ist Sakura https://tenor.com/view/sakura-haruno-naruto-waifu-gif-8390038', 'ist Toga https://tenor.com/view/himiko-toga-bnha-mha-smile-gif-13086340', 
         'ist Rem https://tenor.com/view/re-zero-rem-smile-happy-gif-9725590', 'ist Nao https://tenor.com/view/happy-charlotte-nao-tomori-anime-gif-7525684', 'ist Usagi https://tenor.com/view/sailormoon-smile-hi-yay-usagi-gif-10910670', 'ist Mikasa https://tenor.com/view/mikasa-ackerman-mikasa-attack-on-titan-gif-18236617',
         'ist Kanade https://tenor.com/view/kanade-angel-beats-stare-anime-gif-17758302', 'ist ZeroTwo https://tenor.com/view/zero-two-002-cute-anime-wink-gif-11994868', 'ist Lilith https://tenor.com/view/anime-trinity-seven-arata-lilith-punch-gif-12214647',
         'ist Nanime https://tenor.com/view/nami-one-piece-wink-gif-5799486', 'ist Ram https://tenor.com/view/ram-rem-anime-kawaii-smile-gif-8618517', 'ist Taiga https://tenor.com/view/taiga-toradora-shy-gif-5118649',
         'ist Asuna https://tenor.com/view/asuna-yuuki-sao-anime-gif-9666088', 'ist Erina https://tenor.com/view/erina-nakiri-shokugeki-no-soma-talking-pretty-anime-gif-15756269',
         'ist Nezuko https://tenor.com/view/nezuko-pretty-nezuko-kamado-demonslayer-kimetsu-no-yaiba-gif-15163215', 'ist Mai https://tenor.com/view/mai-sakurajima-gif-18357139',
         'ist Stephanie https://tenor.com/view/no-game-life-steph-stephanie-gif-7161673', 'ist Schwi https://tenor.com/view/no-game-no-life-zero-schwi-dola-shuvi-cute-anime-gif-14220305'
         'ist Mami https://tenor.com/view/mami-nanami-dance-rent-agirlfriend-kanokari-rental-girlfriend-gif-17763325', 'ist Tohka']


husbando = ['Zoro https://tenor.com/view/sanji-one-piece-gif-16224246', 'Subaru https://tenor.com/view/subaru-re-zero-fingers-scheming-anime-gif-16731654', 'Yu https://tenor.com/view/charlotte-y%c5%abotosaka-glowing-eyes-anime-gif-16096389',
            'Sasuke https://tenor.com/view/sasuke-katana-anime-gif-15929772', 'Ban https://tenor.com/view/ban-seven-deadly-sins-anime-gif-5840854', 'Suoh https://tenor.com/view/mikoto-suoh-kproject-anime-cigarette-cool-gif-17344819']

rum = ['https://tenor.com/view/cheers-jack-sparrow-gif-10882046', 'https://tenor.com/view/liquor-oldman-gif-18480181']

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    client.loop.create_task(status_task())


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('Join now PiratenBucht'), status=discord.Status.online)
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game('PiratenBuchtMC.de 19132'), status=discord.Status.online)
        await asyncio.sleep(5)


@client.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.add_roles(role)
    await ctx.send(f"Der Spieler {member} wurde gemutet")


# Moderation

@client.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.remove_roles(role)
    await ctx.send(f"Der Spieler {member} wurde entmutet")


@client.command() 
@commands.has_permissions(kick_members=True)  
async def kick(ctx, member: discord.Member, * , reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Der Spieler {member} wurde gekickt')

@client.command() 
@commands.has_permissions(ban_members=True)  
async def ban(ctx, member: discord.Member, * , reason=None):
    if member: 
        await member.ban(reason=reason)
        await ctx.send(f'Der Spieler {member} wurde gebannt')

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    bannedUsers = await ctx.guild.bans()
    name, discriminator = member.split("#")

    for ban in bannedUsers:
        user = ban.user

        if(user.name, user.discriminator) == (name, discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention} wurde entbannt.")
            return

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author.bot:
        return
    if 'ip' in message.content:
        await message.channel.send('Die IP ist: PiratenBuchtMC.de 19132') 

    curse_words = ['arsch', 'fick dich', 'hurensohn', 'wichser', 'wixxer', 'penis', 'vagina', 'mistgeburt', 'succubus', 'vollkoffer'
                   'idiot', 'trottel', 'depperter hund', 'hure', 'son of bitch', 'arschgesicht', 'arschloch', 'nigger', 'schlampe', 'bitch']
    if any(x in message.content.lower() for x in curse_words):
        print(f'Beleidigung gefunden')
        await message.delete()
        await message.channel.send(f"{message.author.mention}, Unterlass solche Wörter! ")


# Fun Commands

    if message.content.startswith('/beer'):
        await message.channel.send(content='Du hast dir dein Bier gegönnt {0}! {1}'.format(message.author.mention, random.choice(beer)))

    if message.content.startswith('/waifu'):
        await message.channel.send(content='Die Waifu von {0} {1} '.format(message.author.mention, random.choice(waifu)))

    if message.content.startswith('/husbando'):
        await message.channel.send(content='Der Husbando von {0} ist {1} '.format(message.author.mention, random.choice(husbando)))

    if message.content.startswith('/rum'):
        await message.channel.send(content='{0} hat sich rum gegönnt! {1} '.format(message.author.mention, random.choice(rum)))                   

# Welcomer / Goodbye

@client.event
async def on_member_join(member):
   await client.get_channel(770355595668357130).send(f"Willkommen an Board, {member.name}!")

@client.event
async def on_member_remove(member):
   await client.get_channel(770355595668357130).send(f"{member.name} hat unser Schiff verlassen. Wir wünschen dir weiterhin ruhiges Segeln außerhalb der Bucht!")


# Reaction Role

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id 
    if message_id == 771001395410370600:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'jalol':
            role = discord.utils.get(guild.roles, id=770634780814868480)
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
            print("Spieler bekommt Rang")

@client.event 
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id 
    if message_id == 771001395410370600:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'jalol':
            role = discord.utils.get(guild.roles, id=770634780814868480)
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
            print("Spieler hat abreagiert")








client.run("Hör auf zu stalken")
