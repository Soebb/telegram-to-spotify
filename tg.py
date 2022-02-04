from telethon.sync import TelegramClient
import os
import re
from datetime import datetime, timedelta
import pathlib


api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
chat = os.getenv('chat')
current_path = pathlib.Path().resolve()

dt = datetime.today()
mnd = dt - timedelta(days=dt.weekday())
monday = (dt - timedelta(days=dt.weekday())).strftime("%Y-%m-%d")
m1 = (dt - timedelta(days=dt.weekday()))
tuesday = (mnd + timedelta(days=1)).strftime("%Y-%m-%d")
t1 = (mnd + timedelta(days=1))
wednesday = (mnd + timedelta(days=2)).strftime("%Y-%m-%d")
w1 = (mnd + timedelta(days=2))
thursday = (mnd + timedelta(days=3)).strftime("%Y-%m-%d")
th1 = (mnd + timedelta(days=3))
friday = (mnd + timedelta(days=4)).strftime("%Y-%m-%d")
f1 = (mnd + timedelta(days=4))
saturday = (mnd + timedelta(days=5)).strftime("%Y-%m-%d")
s1 = (mnd + timedelta(days=5))
sunday = (mnd + timedelta(days=6)).strftime("%Y-%m-%d")
sa1 = (mnd + timedelta(days=6))
month = (mnd + timedelta(days=2)).strftime("%Y-%m")


# def check(s):
#     print('check')
#     with open(f'{current_path}/test.txt', "r") as file:
#         print('open')
#         searchlines = file.readlines()
#         file.close()
#         for i, line in enumerate(searchlines):
#             # print(i,line)
#             print(f'40 {s}end')
#             print(f'41 {line.rstrip()}end')
#             print(s.__contains__(line))
#             if line.rstrip() == s:
#                 print(f'41 {line}')
#                 return True
#         return False
#
# def check2():
#     a_file = open("test.txt", "r")
#     list_of_lists = []
#     for line in a_file:
#         stripped_line = line.strip()
#         list_of_lists.append(stripped_line)
#     a_file.close()
#     return list_of_lists

with TelegramClient('session_name', int(api_id), api_hash) as client:
    # monday
    count = 0
    lists = []

    for message in client.iter_messages(chat, search=f"Release Date: {month}"):
            # print(message.text)
        # lists = check2()
        test = re.findall('\[(.*?)\]', message.text)
        if test:
                # print(test)
            if '—' in test[0]:
                strs = test[0].lstrip().rstrip()
                lists.append(strs)
                    # if test[0] in f.read():
                    #     print(f'\n{test[0]}')
                    #     pass
                    # else:
                    #     f.write(f'\n{test[0]}')
                count += 1

    print(count)
    with open(f'{current_path}/test.txt', "r+") as f:
        nl = list(dict.fromkeys(lists))
        for n in nl:
            f.write('\n')
            f.write(n)

    print(lists)

client.start()
client.run_until_disconnected()
