import asyncio
from aiogram import Bot
import os
from keepalive import keep_alive
from random import randint

keep_alive()

services = [
    "afterpay", "amazon", "american express", "applepay", "bank",
    "bankofamerica", "carrier", "cashapp", "chase bank", "cibc",
    "citibank", "citizens", "coinbase", "email", "facebook", "gmail",
    "google", "hsbc bank usa", "instagram", "marcus", "mastercard",
    "microsoft", "paypal", "pnc bank", "quadpay", "td bank",
    "truist bank", "twitter support", "u.s. bank", "venmo",
    "visa", "wellsfargo", "whatsapp", "zelle"
]




bot = Bot('8276206384:AAGH6-LHRyqhZixP28Kum-VYRthyZqQgKJ4')
async def main_loop():
    while True:
        try:
            otp = ''.join([str(randint(0, 9)) for _ in range(6)])
            service = services[randint(0, len(services)-1)]
            msg1 = (
                f"<b>🐉 DRAGON OTP 🐉 ┃ VOUCHES </b>\n"
                f"➖➖➖➖➖➖\n"
                f"╭  Service Name ➣ <b>{service}</b>\n"
                f"⭐ OTP ➣ <code>{otp}</code> ✅\n"
                f"╰  Capture By: **********\n"
                f"🤖 <a href='https://t.me/dragonotp1bot'>BOT</a>"
            )
            await bot.send_message(chat_id=-1002609367196, text=msg1, parse_mode='HTML')
        except:
            pass
        try:
            otp = ''.join([str(randint(0, 9)) for _ in range(6)])
            service = services[randint(0, len(services)-1)]
            msg2 = (
                f"<b>📲 M9WD OTP 📲 ┃ VOUCHES </b>\n"
                f"➖➖➖➖➖➖\n"
                f"╭  Service Name ➣ <b>{service}</b>\n"
                f"⭐ OTP ➣ <code>{otp}</code> ✅\n"
                f"╰  Capture By: **********\n"
                f"🤖 <a href='https://t.me/bypassotpm9wdbot11_bot'>BOT</a>"
            )
            await bot.send_message(chat_id=-1003469369405, text=msg2, parse_mode='HTML')
        except:
            pass
        await asyncio.sleep(randint(600, 1500))



while True:
    try:
        asyncio.run(main_loop())
    except Exception as e:
        print(f"❌ Bot crashed: {e}")
        sleep(3)

