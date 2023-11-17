# Importa a biblioteca pycord
import discord 
# Cria uma instancia de discord.Bot 
bot = discord.Bot()

# Decorador que é responsavel por lidar com eventos 
@bot.event 
# Função que modifica o "on_ready" presente no decorador 
async def on_ready():
    print(f"{bot.user} online")

# Decorador responsavel por lidar com comandos slash 
# o mesmo recebe como parametro o nome (name) e a descrição do comando (description)  
@bot.slash_command(name = 'oi', description = 'Faz o bot dizer oi')
# Função responsavel por lidar com a resposta do comando
async def oi(ctx):
    await ctx.respond("Oi")


# OBS: É recomendado carregar o token de um .env
bot.run('TOKEN')

