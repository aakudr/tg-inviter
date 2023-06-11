import random
import time
import traceback
from .data.accounts import Accounts
from .data.proxy import Proxy
import sys
import csv
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest


accounts = Accounts().populate("C:\\Users\\Лиза\\Code\\tg-inviter\\backend\\app\\internal\\data\\accountsDB.json")
proxy = Proxy().populate("C:\\Users\\Лиза\\Code\\tg-inviter\\backend\\app\\internal\\data\\proxyDB.json")
users = [
    ["username", "id (int)", "access_hash (int)", "name"],
    ["username", "id", "access_hash", "name"]
]
""" users = []
with open(input_file, encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user) """
mode = 2


def ClientConnection(accounts, proxy):
    try:
        api_id = accounts.accounts["accounts"][0][1]
        api_hash = accounts.accounts["accounts"][0][2]
        phone = accounts.accounts["accounts"][0][0]
        proxy_protocol = proxy.proxy["proxy"][0][0]
        proxy_ip = proxy.proxy["proxy"][0][1]
        proxy_port = int(proxy.proxy["proxy"][0][2])
        client = TelegramClient(phone, api_id, api_hash)
        """ , proxy=(proxy_protocol, proxy_ip, proxy_port) """
    except KeyError:
        print("KeyError: Check your accountsDB.json and proxyDB.json files.")
        sys.exit(1)

    """ client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('[+] Enter the code: ')) """
    client.start("+77711828948")

    client.send_message('me', 'Hello, myself!')
    return client

def GetTargetChat(client):
    chats = []
    last_date = None
    chunk_size = 200
    groups=[]
    
    result = client(GetDialogsRequest(
                 offset_date=last_date,
                 offset_id=0,
                 offset_peer=InputPeerEmpty(),
                 limit=chunk_size,
                 hash = 0
             ))
    chats.extend(result.chats)
    
    for chat in chats:
        try:
            if chat.megagroup== True:
                groups.append(chat)
        except:
            continue
        
    i = 0
    for group in groups:
        print('['+str(i)+']'+' - '+group.title)
        i += 1

    print('[+] Choose a group to add members')
    g_index = input("[+] Enter a Number : ")

    target_group=groups[int(g_index)]

    print(target_group.title)
    
    target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)

    return target_group_entity

def InviteUsers(client, target_group_entity, users, mode):
    n = 0
    for user in users:
        n += 1
        if 1 == 1:
            time.sleep(1)
        try:
            print ("Adding {}".format(user['id']))
            if mode == 1:
                if user['username'] == "":
                    continue
                user_to_add = client.get_input_entity(user['username'])
            elif mode == 2:
                user_to_add = InputPeerUser(user['id'], user['access_hash'])
            else:
                sys.exit("[!] Invalid Mode Selected. Please Try Again.")
            client(InviteToChannelRequest(target_group_entity,[user_to_add]))
            print("[+] Waiting for 10-30 Seconds...")
            time.sleep(random.randrange(10, 30))
        except PeerFloodError:
            print("[!] Getting Flood Error from telegram. \n[!] Script is stopping now. \n[!] Please try again after some time.")
        except UserPrivacyRestrictedError:
            print("[!] The user's privacy settings do not allow you to do this. Skipping.")
        except:
            traceback.print_exc()
            print("[!] Unexpected Error")
            continue 


client = ClientConnection(accounts=accounts, proxy=proxy)
target_group_entity = GetTargetChat(client)
"""InviteUsers(client, target_group_entity, users, mode) """