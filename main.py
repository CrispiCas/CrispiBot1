import discord
import random
import sys
import time
class MyClient(discord.Client):


    #einloggen
    async def on_ready(self):
        print('Lustig') 
        print('ich bin online xDD')
        embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")

        embed.add_field(name="Ich bin online",
                        value="benutze xd help um die Commands zu sehen ")
        await client.get_channel(830513327192801300).send(embed=embed)

        await client.change_presence(activity=discord.Game(name=f'mit dem Fichbot '))
        print('Bot is finally started')

    #Nachricht schreiben
    async def on_message(self, message):

        #Nachrichten loggen
        if message.author != client.user: #eine log.txt erstellen um alle nachrichten zu loggen :)
            datum = str(message.created_at).split('.')
            datum.pop()
            DatumZeit = str(datum).removeprefix("['").removesuffix("']")
            datumzeit = DatumZeit.split(' ')
            Zeit = datumzeit.pop()
            Datum = str(datumzeit).removeprefix("['").removesuffix("']")

            f = open('logs/logs.txt', 'a')
            f.writelines(f'{message.author} in {message.channel} auf {message.guild} am {Datum} um {Zeit}: {message.content} \n')
            f.close()



        #commands
        prefix = 'xd '
        user = message.author
        command = message.content.lower()
        send = message.channel.send
        userIdgesplitet = str(user).split("#", 1)[0]



        if user == 828582354968248351:
            return

        else:
            #helpcommand mit einem Embed
            if command == f'{prefix}help':
                embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")

                embed.add_field(name="Dieser Bot kann:",
                                    value="xd help, xd hi, xd münze, xd dice, xd test, xd twitch, xd github, xd info, xd idee: [Idee]."
                                          "Wenn du eine Idee hast, mit welcher der Bot noch besser werden kann, dann sag mir uns mit xd idee:")

                await send(embed=embed)

                #hi command
            elif command == f'{prefix}hi':
                    await send(f'Hallo {userIdgesplitet}')
                    await message.author.send('Hallo du')

            if command == f'{prefix}dm':
                    dm = random.randint(1,5)
                    if dm == 1:
                        await message.author.send('Du wolltest ne dm hier hast du ne Dm')
                    elif dm == 2:
                        await message.author.send(f'Huhu {userIdgesplitet}')
                    elif dm == 3:
                        await message.author.send(f'mir fällt nichts ein bitte schick mir Vorschläge mit xd idee:')
                    elif dm == 4:
                        await message.author.send('............................')
                    elif dm == 5:
                        await send(f'*Hier könnte ihre Nachricht stehen*')



            #Münzen command
            elif command == f'{prefix}münze':
                Kopf_oder_Zahl = random.randint(1,2)
                if Kopf_oder_Zahl == 1:
                        await send(f'{userIdgesplitet} hat Kopf geworfen')
                if Kopf_oder_Zahl == 2:
                        await send(f' {userIdgesplitet} hat Zahl geworfen')

                #Würfel command
            elif command == f'{prefix}dice':
                    dice = random.randint(1,6)
                    await send(f'{userIdgesplitet} hat eine {dice} gewürfelt')

            #test command
            elif command == f'{prefix}test':
                    await send('das ist ein Testcommand :^)')

            #twitch command
            elif command == f'{prefix}twitch':
                    await send(f'Das ist der ofizielle Twitch account: https://www.twitch.tv/crispr_cas_9')

            #info command
            elif command == f'{prefix}info':
                    embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")

                    embed.add_field(name="CrispiBot:",
                                    value='Dieser Bot ist der erste Discord bot von CrisprCas 9. Weitere Informationen [hier](https://github.com/CrispiCas/CrispiBot1/blob/master/README.md) Und öffentlich auf [GitHub](https://github.com/CrispiCas/CrispiBot1).'
                                          ' Mit xd help erfahrt ihr alle commands')

                    await send(embed=embed)

            #GitHub command
            elif command == f'{prefix}github':
                    await send(f'der Bot ist öffentlich auf GitHub: https://github.com/CrispiCas/CrispiBot1')

            elif command == f'{prefix}wichtig':
                await send('Schlüselszene, Schlüsselszene, SCHLÜSSELSZENE')
                time.sleep(10)
                await send('Merk dir das das wird gaaaaaaaaanz wichtig')



            #stop command
            elif command == 'xd stop':
                id = str(message).split(' ')[12]
                userID = id.split('=')[1]
                if int(userID) == 802641583190573107:
                    if message.channel == client.get_channel(830513327192801300):
                                embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")

                                embed.add_field(name="Ich bin nun offline",
                                                value="Wenn ich offline bin kannst du meine Commands nicht mehr verwenden")
                                await client.get_channel(830344946753077269).send(embed=embed)
                                await client.get_channel(830513327192801300).send(embed=embed)
                                sys.exit()
                    else:
                        await send('das ist der Falsche Channel...Huch jetzt wisst ihr ja das ich nur über einen bestimmten channel gestoppt werden kann.')

                else:
                    await send('hast wohl nicht die nötigen rechte dafür...tja doof gelaufen')



            #the idea command
            if message.content.startswith('xd idee: '):
                messagesplit = message.content.replace("xd idee:", "")
                l = open('logs/Ideen.txt', 'a')
                l.writelines(f'{message.author} hatte die Idee: {messagesplit}\n')
                l.close()
                await message.channel.purge(limit=1)
                #await message.delete()
                embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")

                embed.add_field(name="Deine Idee:",
                                value=f"{messagesplit}")
                await message.author.send(embed = embed)

            #blacklist 
            blacklist = ['test', 'Doofman']
            for x in blacklist:
                if x in message.content.lower():
                    await message.delete()
                    await message.author.send('Bitte benutze nicht solche begriffe!')


            #the Virus fun command
            if command == 'würfel':
                rand3 = random.randint(0,3)
                await send('__Preparing Virus Data.__')
                await send('`0%`')
                time.sleep(rand3)
                await send('`78%`')
                time.sleep(rand3)
                await send('`100%`')
                time.sleep(rand3)
                
                time.sleep(3)
                await send('**Virus Download has started.**')
                await send('__Downloading data.__')
                await send('`0%`')
                time.sleep(rand3)
                await send('`3%`')
                time.sleep(rand3)
                await send('`11%`')
                time.sleep(rand3)
                await send('`17%`')
                time.sleep(rand3)
                await send('`24%`')
                time.sleep(rand3)
                await send('`25%`')
                time.sleep(rand3)
                await send('`27%`')
                time.sleep(rand3)
                await send('`36%`')
                time.sleep(rand3)
                await send('`40%`')
                time.sleep(rand3)
                await send('`52%`')
                time.sleep(rand3) 
                await send('`66%`')
                time.sleep(rand3)
                await send('`82%`')
                time.sleep(rand3)
                await send('`90%`')
                time.sleep(rand3)
                await send('`91%`')
                time.sleep(rand3)
                await send('`92%`')
                time.sleep(rand3)
                await send('`95%`')
                time.sleep(rand3)
                await send('`100%`') 
                time.sleep(rand3)

                await send('__Freezing Data.__')
                await send('`0%`')
                time.sleep(rand3)
                await send('`32%`')
                time.sleep(rand3)
                await send('`54%`')
                time.sleep(rand3)
                await send('`89%`')
                time.sleep(rand3)
                await send('`100%`')
                time.sleep(rand3)

                await send('__Starting Virus.__')
                await send('`0%`')
                time.sleep(rand3)
                await send('`74%`')
                time.sleep(rand3)
                await send('`100%`')
                time.sleep(rand3)

                await send('**__Virus Installed and Started.__**')
                await send('*You Have now remote acsess to every system that connectet to this page*')



    #Bearbeitete Nachrichten werden geloggt
    async def on_message_edit(self, before, after):

        if before.author != client.user:
            datum = str(after.edited_at).split('.')
            datum.pop()
            DatumZeit = str(datum).removeprefix("['").removesuffix("']")
            datumzeit = DatumZeit.split(' ')
            Zeit = datumzeit.pop()
            Datum = str(datumzeit).removeprefix("['").removesuffix("']")

            f = open('logs/logs.txt', 'a')
            f.writelines(f'{before.author} hat in {after.channel} auf {after.guild} am {Datum} um {Zeit} von "{before.content}" zu "{after.content}" bearbeitet \n')
            f.close()



client = MyClient()
client.run((open('token', 'r').read()))#den token in eine eigene token datei schreiben oder in die Klammer einfügen
