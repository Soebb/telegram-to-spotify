from telethon.sync import TelegramClient
import os
import re
from datetime import datetime, timedelta


api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
chat = os.getenv('chat')

dt = datetime.today()
if dt.isoweekday() == 7:
    mnd = dt + timedelta(days=1)
    monday = (dt + timedelta(days=1)).strftime("%Y-%m-%d")
    m1 = datetime.today().date() + timedelta(days=1)
    tuesday = (dt + timedelta(days=2)).strftime("%Y-%m-%d")
    t1 = datetime.today().date() + timedelta(days=2)
    wednesday = (dt + timedelta(days=3)).strftime("%Y-%m-%d")
    w1 = datetime.today().date() + timedelta(days=3)
    thursday = (dt + timedelta(days=4)).strftime("%Y-%m-%d")
    th1 = datetime.today().date() + timedelta(days=4)
    friday = (dt + timedelta(days=5)).strftime("%Y-%m-%d")
    f1 = datetime.today().date() + timedelta(days=5)
    saturday = (dt + timedelta(days=6)).strftime("%Y-%m-%d")
    s1 = datetime.today().date() + timedelta(days=6)
    sunday = (dt + timedelta(days=7)).strftime("%Y-%m-%d")
    sa1 = datetime.today().date() + timedelta(days=7)
else:
    mnd = dt - timedelta(days=dt.weekday())
    monday = (dt - timedelta(days=dt.weekday())).strftime("%Y-%m-%d")
    m1 = datetime.today().date()
    tuesday = (mnd + timedelta(days=1)).strftime("%Y-%m-%d")
    t1 = datetime.today().date() + timedelta(days=1)
    wednesday = (mnd + timedelta(days=2)).strftime("%Y-%m-%d")
    w1 = datetime.today().date() + timedelta(days=2)
    thursday = (mnd + timedelta(days=3)).strftime("%Y-%m-%d")
    th1 = datetime.today().date() + timedelta(days=3)
    friday = (mnd + timedelta(days=4)).strftime("%Y-%m-%d")
    f1 = datetime.today().date() + timedelta(days=4)
    saturday = (mnd + timedelta(days=5)).strftime("%Y-%m-%d")
    s1 = datetime.today().date() + timedelta(days=5)
    sunday = (mnd + timedelta(days=6)).strftime("%Y-%m-%d")
    sa1 = datetime.today().date() + timedelta(days=6)

with TelegramClient('session_name', int(api_id), api_hash) as client:
    # monday
    print('monday')
    for message in client.iter_messages(chat, offset_date=m1, search=f"Release Date: {monday}"):
        print(message.text)
        re.findall('\[(.*?)\]',message.test)

    print('tuesday')
    for message in client.iter_messages(chat, offset_date=t1, search=f"Release Date: {tuesday}"):
        print(message.text)
        re.findall('\[(.*?)\]', message.test)

    print('wednesday')
    for message in client.iter_messages(chat, offset_date=w1, search=f"Release Date: {wednesday}"):
        print(message.text)
        re.findall('\[(.*?)\]', message.test)

    print('thursday')
    for message in client.iter_messages(chat, offset_date=th1, search=f"Release Date: {thursday}"):
        print(message.text)
        re.findall('\[(.*?)\]', message.test)

    print('friday')
    for message in client.iter_messages(chat, offset_date=f1, search=f"Release Date: {friday}"):
        print(message.text)
        re.findall('\[(.*?)\]', message.test)

    print('saturday')
    for message in client.iter_messages(chat, offset_date=s1, search=f"Release Date: {saturday}"):
        print(message.text)
        re.findall('\[(.*?)\]', message.test)

    print('sunday')
    for message in client.iter_messages(chat, offset_date=sa1, search=f"Release Date: {sunday}"):
        print(message.text)
        re.findall('\[(.*?)\]', message.test)

client.start()
client.run_until_disconnected()
