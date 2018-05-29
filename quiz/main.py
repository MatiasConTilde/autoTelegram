from telethon import TelegramClient, events
from telethon.tl.types import PeerChannel, PeerChat
import json, re

with open('config.json') as file:
	config = json.load(file)

solutions = [r'Yes, (.*)!', r'Nobody guessed. The correct answer was (.*)', r'Правильно, (.*)!', r'Никто не угадал. Правильный ответ был (.*)']

client = TelegramClient('quiz', config['API_ID'], config['API_HASH'], update_workers=4)
client.start()

questions = {}

quizarium_bot = client.get_input_entity(155670507)

with open('db.json', 'r') as db:
	data = json.load(db)

@client.on(events.NewMessage(chats=config['GROUPS'], incoming=True))
def update_handler(event):
	if isinstance(event.message.to_id, PeerChannel):
		group_id = event.message.to_id.channel_id
	elif isinstance(event.message.to_id, PeerChat):
		group_id = event.message.to_id.chat_id

	if event.message.from_id == quizarium_bot.user_id:
		text = event.message.message

		if 'QUESTION' in text or 'ВОПРОС' in text:
			index = 1
			if 'Round' in text or 'Раунд' in text:
				index = 2
			questions[group_id] = text.split('\n')[index]
			print(questions[group_id])

			if questions[group_id] in data:
				client.send_message(event.message.to_id, data[questions[group_id]])
				print('A:', data[questions[group_id]])

		elif not questions[group_id] in data:
			for regex in solutions:
				result = re.search(regex, text.split('\n')[0])
				if result and questions[group_id]:
					data[questions[group_id]] = result.group(1)
					with open('db.json', 'w') as db:
						json.dump(data, db)
					print(len(data))
					break

try:
	input()
	client.disconnect()
except KeyboardInterrupt:
	client.disconnect()
