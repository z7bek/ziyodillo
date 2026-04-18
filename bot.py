import telebot

TOKEN = 8621880920:AAGlcySue8hiddpBmzPMdqLJ8FwOR017OF8
bot = @gold_z7_bot(8621880920:AAGlcySue8hiddpBmzPMdqLJ8FwOR017OF8)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
    "Salom!\n\nBalans, risk%, SL pip yubor.\nMasalan:\n300 2 70")

@bot.message_handler(func=lambda message: True)
def calculate(message):
    try:
        data = message.text.split()
        balance = float(data[0])
        risk_percent = float(data[1])
        sl_pips = float(data[2])

        risk_money = balance * risk_percent / 100
        lot = risk_money / (sl_pips * 1)

        lot = round(lot, 2)

        bot.send_message(message.chat.id,
        f"💰 Risk: {risk_money}$\n📊 Lot: {lot}\n\nSL ursin → -{risk_money}$")

    except:
        bot.send_message(message.chat.id,
        "❌ Format noto‘g‘ri!\nMisol: 300 2 70")

bot.polling()
