from backend.app.internal.data.accounts import Accounts
from backend.app.internal.data.proxy import Proxy
import sys

from telethon import TelegramClient

accounts = Accounts()
proxy = Proxy()

try:
    api_id = Accounts.accounts[0][1]
    api_hash = Accounts.accounts[0][2]
    phone = Accounts.accounts[0][0]
    proxy_ip = Proxy.proxy[0][0]
    proxy_port = Proxy.proxy[0][1]
    client = TelegramClient(phone, api_id, api_hash, proxy=(proxy_ip, proxy_port))
except KeyError:
    print("KeyError: Check your accountsDB.json and proxyDB.json files.")
    sys.exit(1)

