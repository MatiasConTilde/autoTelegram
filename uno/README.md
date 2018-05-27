# autoUNO
Plays UNO automatically with [mau_mau_bot](https://github.com/jh0ker/mau_mau_bot) (hosted on [@unobot](https://t.me/unobot))

### Install
Get your API information from https://my.telegram.org/apps (Learn how to get one at https://core.telegram.org/api/obtaining_api_id)

Create a `config.json` file with
```json
{
	"API_ID": 12345,
	"API_HASH": "0123456789abcdef0123456789abcdef",
	"MIN_PLAYERS": 3,
	"GROUP_ID": 1234567890,
	"BOT_ID": 118169453,
	"BOT_NAME": "unobot"
}
```
and replace the according fields to yours:

`API_ID`: The Telegram API id

`API_HASH`: The Telegram API hash

`MIN_PLAYERS`: The minimal amout of players that have joined before starting the game automatiacally

`GROUP_ID`: The id of the group in which you want to play

`BOT_ID`: The id of the UNO bot ([@unobot](https://t.me/unobot) is 118169453)

`BOT_NAME`: The username of the UNO bot

### Run
`python3 main.py`

To stop, send `Enter` or `^C`

On the first connection, you will have provide login information as phone number and password
