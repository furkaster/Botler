from discord.ext import commands
import discord
import os
from config import *
from discord import ui
from discord.ui import Button, View

from request import Request_Button, Validation_Button



class Botler_Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        intents.message_content = True
        super().__init__(
            command_prefix=commands.when_mentioned_or("!"), intents=intents
        )
        #self.persistent_views_added = False

    def setup_hook(self):
        print('async def setup_hook(self):')
        #self.add_view(Request_Button())
        #self.persistent_views_added = True
        #self.add_view(Validation_Button())
        #self.persistent_views_added = True


    async def on_ready(self):
        #if not self.persistent_views_added:
        self.add_view(Request_Button())
        self.persistent_views_added = True
        self.add_view(Validation_Button())
        self.persistent_views_added = True
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

bot = Botler_Bot()

@bot.event
async def on_member_join(member):
       #print(member.id)

       file_id = open("./id.txt", 'r', encoding='utf-8')

    # читаем все строки и удаляем переводы строк
       lines = file_id.readlines()
       lines = [line.rstrip('\n') for line in lines]
       file_id.close()
       #print(member.id)
    #print('+' + str(len(lines)))
       if str(member.id) in lines:
           #print("+")
           role = discord.utils.get(member.guild.roles, name = MAIN_GROUP)
           await member.add_roles(role)
       else:
           #print("-")
           role = discord.utils.get(member.guild.roles, name = TEMP_GROUP)
           await member.add_roles(role)
           
       embed = discord.Embed(
       title = '**Приватный сервер velonaland**',
       #description = '*Оповещение о статусе заявки*'
       )
       embed.add_field(name="",value="Привет! Что бы играть на приватном сервере, тебе надо отправить заявку в [канал](https://discord.com/channels/917392869201961010/1061917311818289172) и ждать ответа.",inline=False)
       await member.send(embed=embed)
           
#@bot.event 
#async def on_message(message): 
#    if 'discord.gg' in message.content: 
#        await message.delete() 