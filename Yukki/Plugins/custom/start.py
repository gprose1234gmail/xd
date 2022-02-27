from config import THUMBNAIL
from Yukki import SUDOERS, app
from pyrogram import filters
from Yukki.Plugins.custom.strings import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



@app.on_callback_query(filters.regex("admin_cmd"))
async def admin_menu(_, query):    
    await query.message.edit(text=ADMIN_TEXT,reply_markup=BACK_BUTTON,parse_mode="markdown")

@app.on_callback_query(filters.regex("play_cmd"))
async def play_menu(_, query):    
    await query.message.edit(text=PLAY_TEXT,reply_markup=BACK_BUTTON,parse_mode="markdown")

@app.on_callback_query(filters.regex("bot_cmd"))
async def bot_menu(_, query):    
    await query.message.edit(text=BOT_TEXT,reply_markup=BACK_BUTTON,parse_mode="markdown")

@app.on_callback_query(filters.regex("sudo_cmd"))
async def sudo_menu(_, query):    
    await query.message.edit(text=SUDO_TEXT,reply_markup=SUDO_BACK_BUTTON)

@app.on_callback_query(filters.regex("extra_cmd"))
async def extra_menu(_, query):    
    await query.message.edit(text=EXTRA_TEXT,reply_markup=BACK_BUTTON,parse_mode="markdown")

@app.on_callback_query(filters.regex("close_btn"))
async def closer_menu(_, query):    
    await query.message.delete()
