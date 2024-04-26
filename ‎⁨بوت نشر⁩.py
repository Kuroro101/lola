from telethon.sync import TelegramClient, events
from os import system
from random import sample
from json import dumps,loads
from asyncio import sleep
from re import match
import speedtest
import sqlite3

api_id = "Api id"
api_hash = "Api hash"
alEx = TelegramClient('Name_Session_File', api_id, api_hash).start()

@alEx.on(events.NewMessage)
async def handle_new_message(event):
    try:
    	Id_G= int(event.original_update.message.peer_id.channel_id)
    except:
    	Id_G= int(event.original_update.message.peer_id.user_id)
    if ".كرر" in event.message.message:
    	Ag = match(".كرر (.*?)$",event.message.message).group(1)
    	
    	TeleThon = {"id_group":str(Id_G),"What":str(Ag)}
    	with open(f'{event.original_update.message.peer_id.channel_id}-Id.json','w') as alx:
    		alx.write(dumps(TeleThon))
    	with open(f'{event.original_update.message.peer_id.channel_id}-Id.json','r') as c:
    		writ = loads(c.read())
    	Slep = (writ['What'].split(' ')[1])
    	Number = (writ['What'].split(' ')[0])
    	Words = (writ['What'].split(Number)[1].split(Slep)[1])
    	
    	await alEx.edit_message(Id_G,event.original_update.message.id,"تم حفظ الامر  ❕•");await sleep(2);await alEx.delete_messages(Id_G,event.original_update.message.id)
    	for i in range(int(Number)):
    		await alEx.send_message(Id_G,Words)
    		await sleep(int(Slep))













alEx.run_until_disconnected()