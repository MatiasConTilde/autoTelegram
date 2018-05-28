# autoQuiz
Plays @Quizarium automatically

### Install
Get your API information from https://my.telegram.org/apps (Learn how to get one at https://core.telegram.org/api/obtaining_api_id)

Create a `config.json` file with
```json
{
	"API_ID": 12345,
	"API_HASH": "0123456789abcdef0123456789abcdef",
	"GROUPS": ["quizarium_en", "Quizarium", "quizarium_es", "quizarium_de", "QuizariumTraining"]
}
```
and replace the according fields to yours:

`API_ID`: The Telegram API id

`API_HASH`: The Telegram API hash

`GROUPS`: The groups to play in

And a `db.json` file with just `{}` in it

### Run
`python3 main.py`

To stop, send `Enter` or `^C`

On the first connection, you will have provide login information as phone number and password
