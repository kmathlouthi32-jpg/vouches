import random

# ================= CONFIG =================

ELEMENTS = [
    "afterpay", "amazon", "american express", "applepay", "bank",
    "bankofamerica", "carrier", "cashapp", "chase bank", "cibc",
    "citibank", "citizens", "coinbase", "email", "facebook", "gmail",
    "google", "hsbc bank usa", "instagram", "marcus", "mastercard",
    "microsoft", "paypal", "pnc bank", "quadpay", "td bank",
    "truist bank", "twitter support", "u.s. bank", "venmo",
    "visa", "wellsfargo", "whatsapp", "zelle"
]

VIRTUAL_USERS = 80

STICK_MIN = 0.92
STICK_MAX = 0.99

BURST_MIN = 2
BURST_MAX = 4

INTERRUPT_CHANCE = 0.12

# =========================================

# Virtual users state
_users = {uid: random.choice(ELEMENTS) for uid in range(VIRTUAL_USERS)}
_loyalty = {uid: random.uniform(STICK_MIN, STICK_MAX) for uid in range(VIRTUAL_USERS)}

# Burst state
_active_user = random.randrange(VIRTUAL_USERS)
_burst_left = random.randint(BURST_MIN, BURST_MAX)

def _choose_new_element(current):
    return random.choice([e for e in ELEMENTS if e != current])

def _user_action(uid):
    current = _users[uid]

    if random.random() < _loyalty[uid]:
        return current

    new_element = _choose_new_element(current)

    # 40% chance the switch becomes permanent
    if random.random() < 0.4:
        _users[uid] = new_element

    return new_element

# ================= PUBLIC FUNCTION =================

def get_next_element():
    """
    Returns a realistic next element.
    Simulates burst behavior and rare interruptions.
    """

    global _active_user, _burst_left

    # If burst ended, pick a new main user
    if _burst_left <= 0:
        _active_user = random.randrange(VIRTUAL_USERS)
        _burst_left = random.randint(BURST_MIN, BURST_MAX)

    # Small chance another user interrupts
    if random.random() < INTERRUPT_CHANCE:
        intruder = random.randrange(VIRTUAL_USERS)
        return _user_action(intruder)

    # Normal burst action
    _burst_left -= 1
    return _user_action(_active_user)
