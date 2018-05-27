# autoStikas
Replaces messages that contain words from [my sticker pack](https://t.me/addstickers/supageil) with the actual stickers

### Install
Get your API information from https://my.telegram.org/apps (Learn how to get one at https://core.telegram.org/api/obtaining_api_id)

Create a `config.json` file with
```json
{
	"API_ID": 12345,
	"API_HASH": "0123456789abcdef0123456789abcdef",
	"PHONE_NUMBER": "+1987654321",
	"MIN_WORD_AMOUNT": 2
}
```
and replace the according fields to yours:

`API_ID`: The Telegram API id

`API_HASH`: The Telegram API hash

`PHONE_NUMBER`: Your phone number in international format (for the first connection)

`MIN_WORD_AMOUNT`: The minimum amount of words in a message for it to be converted into stickers

### Run
`python3 main.py`

To stop, send `Enter` or `^C`
