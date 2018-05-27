from telethon import TelegramClient, events
from telethon.tl.types import InputMediaDocument, InputDocument
import json

stickers = {
	'aber':    (642456970665656355,  8738296472267118536),
	'alta':    (642456970665656356,  1241390899587307533),
	'boa':     (642456970665656357,  3508415662098963477),
	'boi':     (642456970665656358,  1685284828572902628),
	'du':      (642456970665656359, -7314435806691410614),
	'fik':     (642456970665656360,  1949728862297623771),
	'fikka':   (642456970665656361, -3809861800361143345),
	'funtzt':  (642456970665656362, -8434805796000684763),
	'fünf':    (642456970665656363,  6466214945029397670),
	'geil':    (642456970665656364, -3847265925162213998),
	'gut':     (642456970665656365,  6673288332469284757),
	'hmm':     (642456970665656366,  4685372553348949718),
	'hummel':  (642456970665656367, -7838419127565731143),
	'ja':      (642456970665656368,  7139140935903523838),
	'junge':   (642456970665656369, -4129511533755674316),
	'kind':    (642456970665656370, -2339623014728440097),
	'korrekt': (642456970665656371, -6642668567133715383),
	'mann':    (642456970665656372,  1995962138856399551),
	'mhm':     (642456970665656373,  57243201838567964  ),
	'na':      (642456970665656374, -687880242121344724 ),
	'ne':      (642456970665656375, -6127922788427950671),
	'net':     (642456970665656376,  4702115899428041477),
	'punkt':   (642456970665656377, -6538630790483696727),
	'richtig': (642456970665656378,  458017928210743450 ),
	'scheiße': (642456970665656379,  3268119976343293083),
	'sehr':    (642456970665656380, -1521026836820926828),
	'so':      (642456970665656381, -3794781430722098337),
	'supa':    (642456970665656382, -6026898138866261270),
	'tja':     (642456970665656383, -5971598910560468746),
	'voll':    (642456970665656384,  8933118209398398212),
	'was':     (642456970665656385,  1128642555321771106),
	'wow':     (642456970665656386,  2709195205445998072),
	'wzf':     (642456970665656387, -1776019908441277016),
	'zf':      (642456970665656388, -6920141374605229484),
	'zwei':    (642456970665656389, -8959184212521341238),
	'2.5':     (642456970665656390,  6681913079297189642)
}

with open('config.json') as file:
	config = json.load(file)

client = TelegramClient('stikas', config['API_ID'], config['API_HASH'], update_workers=4)
client.connect()

if not client.is_user_authorized():
	client.send_code_request(config['PHONE_NUMBER'])
	client.sign_in(config['PHONE_NUMBER'], input('Enter code: '))

@client.on(events.NewMessage(outgoing=True))
def update_handler(event):
	words = event.message.message.split()
	if len(words >= config['MIN_AMOUT']):
		all_correct = True
		for word in words:
			if not word in stickers:
				all_correct = False
				break

		if all_correct:
			client.delete_messages(event.message.to_id, event.message.id);
			for word in words:
				client.send_file(event.message.to_id, InputMediaDocument(id=InputDocument(id=stickers[word][0], access_hash=stickers[word][1])), reply_to=event.message.reply_to_msg_id)

try:
	input()
	client.disconnect()
except KeyboardInterrupt:
	client.disconnect()
