from bot import *
from discord.ext import commands
import discord
import os
from config import *
from discord import ui
from discord.ui import Button, View

from request import Request_Button, Validation_Button

bot.load_extension('request')

bot.run(TOKEN)