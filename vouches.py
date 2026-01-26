import asyncio
import random
from datetime import datetime
import pytz
from service import get_next_element

from aiogram import Bot, Dispatcher
from keepalive import keep_alive
import pyotp

keep_alive()

# ===== CONFIG =====
BOT_TOKEN = "8276206384:AAGH6-LHRyqhZixP28Kum-VYRthyZqQgKJ4"
CHANNEL_ID = "-1002609367196"  # or channel ID (-100xxxx)

US_TZ = pytz.timezone("US/Eastern")

SYSTEM_MESSAGES = [r"""╔══🌀 *DRAGON OTP BOT* 🌀══╗  
     🔐 Real\-Time OTP Hunter  
╚════════════════╝  

📞 *CALL STATUS*: ✅ `Call Successful`
━━━━━━━━━━━━━━━━━  
🛠️ *CALL DETAILS*:  
├─ 🎯 *Service*: `{service}`  
├─ 🎭 *Spoofing*: ✅ *Enabled* 
├─ 🌍 *International*: ❌ *No*  
└─ 🛡️ *Verification*: `NORMAL`  

━━━━━━━━━━━━━━━━━  
📩 *CAPTURED DATA*:  
├─ 🔐 *OTP*: `[{otp_code}]`  
└─ 🕵️ *Captured By*: `********`  

━━━━━━━━━━━━━━━━━  
🤖 [BOT](https://t.me/dragonotp1bot) *\|* [CHANNEL](https://t.me/DRAGON_OTP_channel) *\|* [VOUCHES](https://t.me/DragonOtp_Vouches) 
🔻 *Powered by Dragon Systems*™""",

r"""╔══🌀 *DRAGON OTP BOT V2* 🌀══╗  
🔐 Real\-Time OTP Hunter  
╚════════════════╝  
📞 *CALL STATUS*: ✅ `Call Successful`
━━━━━━━━━━━━━━━━━  
🛠️ *CALL DETAILS*:  
├─ 🎯 *Service*: `{service}`
├─ 🎭 *Spoofing*: ✅ *Enabled* 
├─ 🔐 *Call Type*: {call_type} 
└─ 🛡️ *Verification*: `NORMAL`  
━━━━━━━━━━━━━━━━━  
📩 *CAPTURED DATA*:  
├─ 🔐 *OTP*: `[{otp_code}]`  
└─ 🕵️ *Captured By*: `********`  
━━━━━━━━━━━━━━━━━  
🤖 [BOT](https://t.me/dragonotp1bot) *\|* [CHANNEL](https://t.me/DRAGON_OTP_channel) *\|* [VOUCHES](https://t.me/DragonOtp_Vouches) 
🔻 *Powered by Dragon Systems*™"""]

# Activity simulation (15–20% of 393)
MIN_ACTIVE = 55
MAX_ACTIVE = 80

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# ===== TIME HELPERS =====
def us_hour():
    return datetime.now(US_TZ).hour

def is_us_night():
    return 1 <= us_hour() < 8

def next_delay():
    if is_us_night():
        # Very low activity at night
        return random.randint(30*60 , 120*60)  # 30–120 min

    r = random.random()

    # Small burst (people clicking fast)
    if r < 0.10:
        return random.randint(5, 20) #5 20

    # Long pause (people away)
    elif r < 0.25:
        return random.randint(10*60 , 45*60 )

    # Normal activity
    else:
        return random.randint(30, 360)  # 30s – 6min

def choose_message():
    if random.random() < 0.95:
        return SYSTEM_MESSAGES[0]
    else:
        return SYSTEM_MESSAGES[1]

def generate_otp():
    secret = pyotp.random_base32()

    totp = pyotp.TOTP(secret)
    otp_code = totp.now()
    return otp_code


def generate_message():
    template = choose_message()

    if "{call_type}" in template:
        call_types = ['Custom call','Custom voice']
        value = call_types[random.randint(0,1)]
        return template.format(call_type=value, otp_code=generate_otp(),service=get_next_element())

    return template.format(otp_code=generate_otp(),service=get_next_element())

# ===== MAIN LOOP =====
async def activity_loop():

    while True:
        msg = generate_message()

        try:
            await bot.send_message(CHANNEL_ID, msg,parse_mode='MarkdownV2')
        except Exception as e:
            print("Send error:", e)
        delay = next_delay()
        await asyncio.sleep(delay)

# ===== START =====
async def main():
    asyncio.create_task(activity_loop())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())




