import json
import random
from bot.core import run_bot_session

# Load proxy list
with open("proxies.json") as f:
    proxies = json.load(f)

# Target URL (edit to your destination)
url = "https://example.com"

# Launch 5 sessions for demo; adjust as needed
for _ in range(5):
    proxy = random.choice(proxies)
    print(f"Launching bot from: {proxy['country']} ({proxy['ip']})")
    run_bot_session(proxy, url)
