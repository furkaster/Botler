from discord.ext import commands
import discord
from discord import ui
from config import *
from discord.ui import Button, View
#from bot import *
import bot

refuses = ''
int_user = ''

class Validation_Button(discord.ui.View):
    def __init__(self):
#        self.author = author
        super().__init__(timeout=None)

    @discord.ui.button(label="Принять", style=discord.ButtonStyle.success,
                       emoji='👍', custom_id="persistent_view:yes")
    async def upvote_button(self, button : discord.ui.Button,
    interaction : discord.Interaction):
      if interaction.user.id == OWNER_ID:
       #modal = MyModal(title="Проходка на сервер")
       #pprint(dir(modal.children[4].value))
       #print(str(modal.children[0].value))
    #print(str(discord.Message.embeds[0].fields[0].name.lower()))

#       for embed in embed_content_in_dict:
       #print(discord.Message.embeds.item[0])
       #embed.set_footer(text="---------------------------")
#       for field in embed.fields: # Dynamically get the user id field.
#           print(embeds[0].fields.field.name)
#           if field.name.lower() == "Немного о себе":
#               user_id_field = field
#               break
#       else: # In case the field isn't found
#           pass # Put some code here
#       user_id = int(user_id_field.value) # Get the value of the field
#       await interaction.response.send_message(user_id, ephemeral=True)
       #print(dir(self.message.embeds[0].footer))
       #print(str(self.message.embeds[0].footer.text))
       #for member in self.message.guild.fetch_members(limit=150):
       #print(member.name)
       #print(self.message.guild.fetch_user('308537160124989440'))
       #print(self.message.guild.get_member_named("furkaster#6972"))

       #print(interaction.message.embeds[0].fields[0].value)
       #print(str(interaction.message.embeds[0].title))
       #title = str(interaction.message.embeds[0].title)
       #title1 = title.split()
       #print(title1[5])
       #print(dir(self.message.embeds[0].fields[0]))
       #print(str(self.message.embeds[0].fields[0].value))
       channel = bot.bot.get_channel(CONSOLE_MINECRAFT_CHANNEL)
       await channel.send('wl add '+ interaction.message.embeds[0].fields[0].value)

       userid = int(interaction.message.embeds[0].footer.text)

       file_id = open("./id.txt", "a") 
       file_id.write(str(userid) + '\n'); 
       file_id.close()

       user = await bot.bot.fetch_user(userid)
       embed = discord.Embed(
       title = '**Приватный сервер velonaland**',
       description = '*Оповещение о статусе заявки*'
       )
       embed.add_field(name="Статус: ", value="Заявка одобрена", inline=False)
       embed.add_field(name="Дополнительная информация: ",
       value='Гениталии не строить, скины 18+ не ставить, матом/КАПСОМ в чате '\
       'не писать, не гриферить(ведуться логи). На сервере есть приваты через топорик. На заверщающем этапе тебе нужно зайти на '\
       'сервер манкрафта и написать в чат команду /discord link, после чего'\
       'тебе будет написан код. Этот код надо написать в личные сообщения боту '\
       'Chat-Bot#1502.[Тут айпи сервера и ссылка на мод голосового чата]'\
       '(https://discord.com/channels/917392869201961010/985560096958480394)')
       embed.set_footer(text="" + int_user, icon_url=interaction.guild.icon.url)
       await user.send(embed=embed)
       server = bot.bot.get_guild(SERVER_ID)
       member = await server.fetch_member(userid)
       #role = discord.utils.get_role(1073235421024239638)
       role = discord.utils.get(member.guild.roles, name = MAIN_GROUP)
       #await user.add_roles(1073235421024239638)
       #await bot.add_role(member, '1073235421024239638')
       await member.add_roles(role)
       remove_role = discord.utils.get(member.guild.roles, name = TEMP_GROUP)
       await member.remove_roles(remove_role)
       #userr = interaction.message.embeds[0].author
       #pprint(dir(userr))
       #role = interaction.guild.get_role(1073235421024239638)
       #pprint(dir(user.name))
       #await interaction.user.add_roles(role)
       #guild = bot.get_guild(1066685614633795675)
       #role = guild.get_role(1073235421024239638)
       #await user.add_roles(role)
       #await message.add_roles(1073235421024239638)
       #await userr.add_roles("Minecraft")
       #role = discord.utils.get_role('1073235421024239638')
       #await bot.add_role(role) # interaction.message.embeds[0].author.name,
       #await user.send("Дополнительная информация:")
       #print(userid)
       for child in self.children:
           child.disabled = True
#       button.disabled = True
       #print(embeds[0].fields.field.name)
       button.style = discord.ButtonStyle.gray
       #await interaction.response.edit_message(view=self)
       await interaction.message.edit(view=self)
       return False
      else:
       await interaction.response.send_message('Нельзя сотворить здесь!',
       ephemeral=True)
       return False
      #await interaction.response.edit_message(view=self) # edit the message's view

    @discord.ui.button(label="Отказать", style=discord.ButtonStyle.danger,
                       emoji='👎', custom_id="persistent_view:no")
    async def downvote_button(self, button : discord.ui.Button,
                              interaction : discord.Interaction):
        if interaction.user.id == OWNER_ID:
         global userid
         userid = int(interaction.message.embeds[0].footer.text)
         #user = await bot.bot.fetch_user(userid)

         for child in self.children:
            child.disabled = True # set button.disabled to True to disable the button
         orig_msg = interaction.message
         button.style = discord.ButtonStyle.gray
         modal = refuse(title="Причина отказа", timeout=None)
         await interaction.response.send_modal(modal)
         await modal.wait()
         em1 = interaction.message.embeds[0].add_field(name="Причина отказа", value=refuses, inline=False)         
         await orig_msg.edit(view=self, embed=em1)
         #await interaction.response.edit_message(view=self, embed=em1)
         return False
        else:
         await interaction.response.send_message('Нельзя сотворить здесь!',
         ephemeral=True)
         return False

class refuse(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="Причина отказа"))

    async def callback(self, interaction: discord.Interaction):
        user = await bot.bot.fetch_user(userid)
        embed = discord.Embed(
        title = '**Приватный сервер velonalandi**',
        description = '*Оповещение о статусе заявки*'
        )
        embed.add_field(name="Статус: ", value="Заявка отклонена")
        embed.add_field(name="Причина отказа",
        value = self.children[0].value, inline=False)
        global int_user
        embed.set_footer(text="" + int_user, icon_url=interaction.guild.icon.url)
        #print(interaction.guild.icon.url)
        global refuses
        refuses = self.children[0].value
        await user.send(embed=embed)
        await interaction.response.send_message(".",ephemeral=True)

class Input_Request(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Твой игровой ник с учетом регистра"))
        self.add_item(discord.ui.InputText(label="Твой возраст"))
        self.add_item(discord.ui.InputText(label="Что ты считаешь нормой общения"))
        self.add_item(discord.ui.InputText(label="Что ты хочешь реализовать на"\
        "сервере", style=discord.InputTextStyle.long))
        self.add_item(discord.ui.InputText(label="Немного о себе",
        style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Проходка на сервер", description="")
        embed.add_field(name="Твой игровой ник", value=self.children[0].value,
        inline=False)
        embed.add_field(name="Твой возраст", value=self.children[1].value,
        inline=False) #
        embed.add_field(name="Что ты считаешь нормой общения",
        value=self.children[2].value, inline=False)
        embed.add_field(name="Что ты хочешь реализовать на сервере",
        value=self.children[3].value, inline=False)
        embed.add_field(name="Немного о себе", value=self.children[4].value,
        inline=False)
        global int_user
        int_user = str(interaction.user.id)
        embed.set_footer(text="" + str(interaction.user.id),icon_url=interaction.guild.icon.url)
        #embed.set_author(name=interaction.user) #, icon_url=interaction.user.avatar)
        #pprint(dir(interaction.user.avatar))
        if hasattr(interaction.user.avatar, "url"):
          #print('Yes')
          embed.set_author(name=interaction.user,icon_url=interaction.user.avatar)
        else:
          #print('No')
          embed.set_author(name=interaction.user,icon_url = discord.Embed.Empty)

        channel = bot.bot.get_channel(REQUEST_CHANNEL)
        await channel.send(embeds=[embed],view=Validation_Button())

        admin = bot.bot.get_user(OWNER_ID)
        await admin.send('Новая заявка!')

        #user = await bot.fetch_user(int(interaction.user.id))
        #embed1 = discord.Embed(
        #title = '**Приватный сервер Almari**',
        #description = '*Оповещение о статусе заявки*'
        #)
        #embed1.add_field(name="Статус: ", value="На рассмотрении. Если владелец в сети и не занят, то рассмотрение происходит быстро.", inline=False)
        #await user.send(embed=embed1)

        await interaction.response.send_message(content="Заявка ушла на рассмот"\
        "рение. Если владелец в сети и не занят, то рассмотрение происходит быс"\
        "тро. Ответ придет в ЛС.", ephemeral=True)


        #admin = await bot.fetch_user('308537160124989440')
        #await admin.send('Новая заявка!')

        #await interaction.response.send_message(embeds=[embed],view=Buttons())
        #user = await bot.fetch_user("308537160124989440")
        #await user.send(embeds=[embed],view=Buttons())





class Request_Button(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Заполнить 📩", style=discord.ButtonStyle.grey,
        custom_id="persistent_view:grey"
    )
    async def grey(self, button: discord.ui.Button,
    interaction: discord.Interaction):

        # await interaction.response.send_message("This is grey.", ephemeral=True)
        await interaction.response.send_modal(Input_Request(title="Проходка на сервер",timeout=None))




@commands.command()
@commands.is_owner()
async def test(ctx):

    await ctx.message.delete()
    await ctx.send("Чтобы попасть на сервер, необходимо подать заявку. Для "\
    "создания заявки нажми на кнопку и заполни анкету." +"\r\n"+
    "Администрация вправе отказать без объяснения причин." +"\r\n"+ "Помни: не в"\
    "ажно сколько тебе лет, главное адекватность.", view=Request_Button())


def setup(bot):
    bot.add_command(test)