import discord
import random
class MyClient(discord.Client):


    #einloggen
    async def on_ready(self):
        print('ich bin online :)')



    #Nachricht schreiben
    prefix = '+'
    async def on_message(self, message ):


        #Nachrichten loggen
        if message.author != client.user: #eine log.txt erstellen um alle nachrichten zu loggen :)
            datum = str(message.created_at).split('.')
            datum.pop()
            DatumZeit = str(datum).removeprefix("['").removesuffix("']")
            datumzeit = DatumZeit.split(' ')
            Zeit = datumzeit.pop()
            Datum = str(datumzeit).removeprefix("['").removesuffix("']")

            f = open('logs.txt', 'a')
            f.writelines(f'{message.author} in {message.channel} auf {message.guild} am {Datum} um {Zeit}: {message.content} \n')
            f.close


        #commands
        prefix = '+'
        user = message.author
        command = message.content.lower()
        send = message.channel.send

        if command.startswith(prefix):

            if user == 828582354968248351:
                return

            else:
                if command == f'{prefix}help':
                    await send(f'``Dieser bot kann{prefix}help, {prefix}hi, {prefix}münze, {prefix}dice, {prefix}test, {prefix}tüv, {prefix}twitch, {prefix}HALLO, {prefix}github``')

                elif command == f'{prefix}hi':
                    await send(f'Hallo {user}')

                elif command == f'{prefix}münze':
                    Kopf_oder_Zahl = random.randint(1,2)
                    if Kopf_oder_Zahl == 1:
                        await send(f'{user} hat Kopf geworfen')
                    if Kopf_oder_Zahl == 2:
                        await send(f' {user} hat Zahl geworfen')

                elif command == f'{prefix}dice':
                    dice = random.randint(1,6)
                    await send(f'{user} hat eine {dice} gewürfelt')


                elif command == f'{prefix}test':
                    await send('das ist ein Testcommand :^)')

                if command == f'{prefix}twitch':
                    await send(f'Das ist der ofizielle Twitch account: https://www.twitch.tv/crispr_cas_9')

                if command == f'{prefix}info':
                    await send(f'Das ist der erste Bot von Crispr Cas9. Er ist in Python geschrieben und das habe ich getan weil Floschy gesagt hat python ist besser')

                if command == f'{prefix}HALLO':
                    await  send(f'@everyone kommt her')

                if command == f'{prefix}github':
                    await send(f'Der Bot ist öffentlich auf gitHub: https://github.com/CrispiCas/CrispiBot1')

    async def on_message_edit(self, before, after):

        if before.author != client.user:
            datum = str(after.edited_at).split('.')
            datum.pop()
            DatumZeit = str(datum).removeprefix("['").removesuffix("']")
            datumzeit = DatumZeit.split(' ')
            Zeit = datumzeit.pop()
            Datum = str(datumzeit).removeprefix("['").removesuffix("']")

            f = open('logs.txt', 'a')
            f.writelines(f'{before.author} hat in {after.channel} auf {after.guild} am {Datum} um {Zeit} von "{before.content}" zu "{after.content}" bearbeitet \n')
            f.close




client = MyClient()
client.run((open('token', 'r').read()))#den token in eine eigene token datei schreiben oder in die Klammer einfügen