# Discord Translation Bot
A discord bot that translates a message to the desired language based on the type of the reaction emoji. For example, reacting to a message with the 'France' flag emoji would translate the message to French.

## Installation
1. Install the **google_trans_new** package:
```
pip install google_trans_new
```

2. Replace the **BOT_TOKEN_HERE** string with the actual discord bot token in the *translator.py* file.
```
token = "BOT_TOKEN_HERE"
```
3. Run the bot:
```python3
python translator.py
```


## Contributing
Pull requests are welcome. Only French, English, and Spanish are supported as of yet. Please help enhance the code to add more languages.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
