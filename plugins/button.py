# CodeXBotz 
# mrismanaziz
# devolart


from config import FORCE_SUB_, BUTTON_ROW, BUTTON_TITLE

from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_:
        buttons = [
            [
                InlineKeyboardButton(text="Bantuan", callback_data="help"),
                InlineKeyboardButton(text="Tutup", callback_data="close"),
            ],
        ]
        return buttons

    dynamic_buttons = []

    current_row = []
    for key in FORCE_SUB_.keys():
        current_row.append(InlineKeyboardButton(text=f"{BUTTON_TITLE} {key}", url=getattr(client, f'invitelink{key}')))
        if len(current_row) == BUTTON_ROW:
            dynamic_buttons.append(current_row)
            current_row = []

    if current_row:
        dynamic_buttons.append(current_row)

    buttons = [
        [
            InlineKeyboardButton(text="Bantuan", callback_data="help"),
        ],
    ] + dynamic_buttons + [
        [InlineKeyboardButton(text="Tutup", callback_data="close")],
    ]
    return buttons


def fsub_button(client, message):
    if FORCE_SUB_:
        dynamic_buttons = []
        current_row = []
        for key in FORCE_SUB_.keys():
            current_row.append(InlineKeyboardButton(text=f"{BUTTON_TITLE} {key}", url=getattr(client, f'invitelink{key}')))
            if len(current_row) == BUTTON_ROW:
                dynamic_buttons.append(current_row)
                current_row = []

        if current_row:
            dynamic_buttons.append(current_row)
            
        try:
            dynamic_buttons.append([
                InlineKeyboardButton(
                    text="Coba Lagi",
                    url=f"https://t.me/{client.username}?start={message.command[1]}",
                )
            ])
        except IndexError:
            pass

        return dynamic_buttons