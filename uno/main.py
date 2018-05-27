from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetInlineBotResultsRequest, SendInlineBotResultRequest
from telethon.tl.types import UpdateShortChatMessage
import json, time

with open('config.json') as file:
	config = json.load(file)

# Define constants
sticker_names = ['b_0', 'b_1', 'b_2', 'b_3', 'b_4', 'b_5', 'b_6', 'b_7', 'b_8', 'b_9', 'b_draw', 'b_skip', 'b_reverse', 'g_0', 'g_1', 'g_2', 'g_3', 'g_4', 'g_5', 'g_6', 'g_7', 'g_8', 'g_9', 'g_draw', 'g_skip', 'g_reverse', 'r_0', 'r_1', 'r_2', 'r_3', 'r_4', 'r_5', 'r_6', 'r_7', 'r_8', 'r_9', 'r_draw', 'r_skip', 'r_reverse', 'y_0', 'y_1', 'y_2', 'y_3', 'y_4', 'y_5', 'y_6', 'y_7', 'y_8', 'y_9', 'y_draw', 'y_skip', 'y_reverse']
special_stickers = ['draw', 'pass', 'draw_four', 'colorchooser']
color_hearts = [('💙', 'b'), ('💚', 'g'), ('❤️', 'r'), ('💛', 'y')]

# All IDs have ':' followed by the round number at the end so remove that
def name_from_id(id):
	return id[:id.find(':')]

def do_next_move():
	# Get cards from inline query
	inline_result = client(GetInlineBotResultsRequest(uno_bot, group_chat, '', ''))
	buttons = inline_result.results

	# If I have to choose the color (from a colorchooser card before)
	if name_from_id(buttons[-1].id) == 'hand':
		most_color = (0, '')
		# Search for the most appearing color
		for color, name in color_hearts:
			color_count = buttons[-1].description.count(color)

			if color_count > most_color[0]:
				most_color = (color_count, name)

		client(SendInlineBotResultRequest(group_chat, inline_result.query_id, most_color[1]+buttons[0].id[buttons[0].id.find(':'):]))
		return True

	# If there's a normal card
	for card in buttons:
		if name_from_id(card.id) in sticker_names:
			client(SendInlineBotResultRequest(group_chat, inline_result.query_id, card.id))
			return True

	# If no normal card is available, choose the best special one
	for card in reversed(buttons):
		if name_from_id(card.id) in special_stickers:
			client(SendInlineBotResultRequest(group_chat, inline_result.query_id, buttons[0].id))
			return True

	return False

client = TelegramClient('uno', config['API_ID'], config['API_HASH'], update_workers=4)
client.start()

group_chat = client.get_input_entity(config['GROUP_ID'])
uno_bot = client.get_input_entity(config['BOT_ID'])

joined_count = 0

@client.on(events.NewMessage(chats=group_chat, incoming=True))
def update_handler(event):
	global joined_count

	if event.message.from_id == uno_bot.user_id:
		if event.message.mentioned:
			do_next_move()
		if event.message.message == 'Game ended!':
			client.send_message(group_chat, '/new@'+config['BOT_NAME'])
		if event.message.message == 'Created a new game! Join the game with /join and start the game with /start':
			client.send_message(group_chat, '/join@'+config['BOT_NAME'])
			joined_count = 0
		if event.message.message == 'Joined the game':
			joined_count += 1
		if joined_count >= config['MIN_PLAYERS']:
			client.send_message(group_chat, '/start@'+config['BOT_NAME'])

do_next_move()

try:
	input()
	client.disconnect()
except KeyboardInterrupt:
	client.disconnect()
