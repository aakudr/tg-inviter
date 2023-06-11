import traceback
from backend.app.internal.data.accounts import Accounts
from backend.app.internal.data.proxy import Proxy
import sys
import csv
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest



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


client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('[+] Enter the code: '))


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
 
i=0
""" for group in groups:
    print(gr+'['+cy+str(i)+gr+']'+cy+' - '+group.title)
    i+=1

print(gr+'[+] Choose a group to add members')
g_index = input(gr+"[+] Enter a Number : "+re)
target_group=groups[int(g_index)]
 
target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)

print(gr+"[1] add member by user ID\n[2] add member by username ")
mode = int(input(gr+"Input : "+re)) 
n = 0
print(users)
print('before for') """


""" for user in users:
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
	        sys.exit(re+"[!] Invalid Mode Selected. Please Try Again.")
        client(InviteToChannelRequest(target_group_entity,[user_to_add]))
        print(gr+"[+] Waiting for 10-30 Seconds...")
        time.sleep(random.randrange(10, 30))
    except PeerFloodError:
        print(re+"[!] Getting Flood Error from telegram. \n[!] Script is stopping now. \n[!] Please try again after some time.")
    except UserPrivacyRestrictedError:
        print(re+"[!] The user's privacy settings do not allow you to do this. Skipping.")
    except:
        traceback.print_exc()
        print(re+"[!] Unexpected Error")
        continue """