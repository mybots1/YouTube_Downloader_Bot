from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("rami al ali", url="https://t.me/nnnnh")],
        [InlineKeyboardButton(
            "- لشراء نسخة", url="https://t.me/nnnnh")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\nsend /help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
