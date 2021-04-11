import discord
import random
import sys
class MyClient(discord.Client):


    #einloggen
    async def on_ready(self):
        print('ich bin online xDD')
        embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")

        embed.add_field(name="Ich bin online",
                        value="benutze xd help um die Commands zu sehen ")
        await client.get_channel(830344946753077269).send(embed=embed)
        await client.get_channel(830513327192801300).send(embed=embed)

        await client.change_presence(activity=discord.Game(name=f'mit mir '))

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

        if command.startswith(prefix):

            if user == 828582354968248351:
                return

            else:
                #helpcommand mit einem Embed

                if command == f'{prefix}help':
                    embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")

                    embed.add_field(name="Dieser Bot kann:",
                                    value="xd help, xd hi, xd münze, xd dice, xd test, xd twitch, xd github, xd info, xd dm.")

                    await send(embed=embed)

                    #hi command
                elif command == f'{prefix}hi':
                    await send(f'Hallo {userIdgesplitet}')
                    await message.author.send('Huhu')

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
                    await send(f'Dieser Bot wurde von Crispr Cas 9 programmiert')

                #GitHub command
                elif command == f'{prefix}github':
                    await send(f'der Bot ist öffenrlich auf GitHub: https://github.com/CrispiCas/CrispiBot1')

                elif command == f'{prefix}dm':
                    await message.author.send('Du wolltest ne Dm hier hast du ne Dm')

                #stop command
                elif command == 'xd stop':
                    if message.channel == client.get_channel(830513327192801300):


                        id = str(message).split(' ')[12]
                        userID = id.split('=')[1]
                        if int(userID) == 802641583190573107:
                            embed = discord.Embed(colour=discord.Colour(0xffa8), url="https://discordapp.com")

                            embed.add_field(name="Ich bin nun offline",
                                            value="Wenn ich offline bin kannst du meine Commands nicht mehr verwenden")
                            await client.get_channel(830344946753077269).send(embed=embed)
                            await client.get_channel(830513327192801300).send(embed=embed)
                            sys.exit()

                    else:
                        await send('das ist die Falscher Channel xD')



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
