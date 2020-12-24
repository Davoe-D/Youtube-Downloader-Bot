from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('❤ Bots Updates Channel ❤', url='https://t.me/naijabestz'),
                    InlineKeyboardButton('Feedback 🤷‍♂️', url='https://t.me/bestzbrothers')
                ],
               [
                    InlineKeyboardButton('⭐ Support Group ⭐', url='https://t.me/naija_bestz'),
                    InlineKeyboardButton('Source 😜', url='https://github.com/Davoe-D/Youtube-Downloader-Bot')
                ]
            ]
        )
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
