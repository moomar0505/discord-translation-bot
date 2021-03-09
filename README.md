# Discord Translation Bot
A discord bot that translates a message to the desired language based on the type of the reaction emoji. For example, reacting to a message with the 'France' flag emoji would translate the message to French.

## Installation
1. Install the **google_trans_new** package:
```python
pip install google_trans_new
```

2. Replace the **BOT_TOKEN_HERE** string with the actual discord bot token in the [translator.py](https://github.com/moomar0505/usr-discord-translation-bot/blob/main/translator.py) file.
```python
token = "BOT_TOKEN_HERE"
```
3. Run the bot:
```python
python translator.py
```

## Usage
React to a message with the desired flag emoji to translate the message to the appropriate language. *Only French, Spanish and English supported as of 03/08/2021.*
(https://github.com/moomar0505/usr-discord-translation-bot/blob/main/usage_image.JPG)

## Contributing
Pull requests are welcome. 

Please help enhance the code to add more languages since only French, English, and Spanish are supported as of yet. 

## License
[MIT](https://choosealicense.com/licenses/mit/)
