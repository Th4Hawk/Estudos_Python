# Importa a biblioteca
import telebot 
# Variavel com o token de autenticação
TOKEN = ''
# Instancia que recebe o token do bot como parametro
bot = telebot.TeleBot(TOKEN)
# Decorador responsavel por lidar com o comando
@bot.message_handler(commands=['start'])
# Função responsavel por lidar com a lógica do comando 
def start(message):
    bot.send_message(message, "Olá")
# Inicializa o bot 
bot.polling()
