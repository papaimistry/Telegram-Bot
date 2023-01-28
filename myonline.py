import telegram

bot = telegram.Bot(token='5837129083:AAHuwFCnUcX1R9KZyItA7ZDnRgacjm81rEY')

# Use webhook to always keep the bot online
updater = Updater(token='5837129083:AAHuwFCnUcX1R9KZyItA7ZDnRgacjm81rEY', use_context=True)
updater.start_webhook(listen="0.0.0.0",
                      port= 3001,
                      url_path='5837129083:AAHuwFCnUcX1R9KZyItA7ZDnRgacjm81rEY')
updater.bot.setWebhook(url='https://telegram-bot-1ddq.onrender.com' + '5837129083:AAHuwFCnUcX1R9KZyItA7ZDnRgacjm81rEY')
updater.idle()
