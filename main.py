import discord
from discord.ext import commands
from config import token
from logic import Pokemon

# Настройка интентов для бота
intents = discord.Intents.default()  # Получаем настройки по умолчанию
intents.messages = True              # Разрешаем боту обрабатывать сообщения
intents.message_content = True       # Разрешаем боту читать содержимое сообщений
intents.guilds = True                # Разрешаем боту работать с серверами (guilds)

# Создание бота с заданным префиксом команд и активированными интентами
bot = commands.Bot(command_prefix='!', intents=intents)

# Событие, которое срабатывает, когда бот готов к работе
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')  # Выводит в консоль имя бота

# Команда '!go'
@bot.command()
async def go(ctx):
    author = ctx.author.name  # Получаем имя автора сообщения
    # Проверяем, есть ли уже покемон для этого пользователя
    if author not in Pokemon.pokemons.keys():
        pokemon = Pokemon(author)  # Создаем нового покемона
        await ctx.send(await pokemon.info())  # Отправляем информацию о покемоне
        image_url = await pokemon.show_img()  # Получаем URL изображения покемона
        if image_url:
            embed = discord.Embed()  # Создаем встраиваемое сообщение (embed)
            embed.set_image(url=image_url)  # Устанавливаем изображение покемона
            await ctx.send(embed=embed)  # Отправляем встраиваемое сообщение с изображением
        else:
            await ctx.send("Не удалось загрузить изображение покемона.")
    else:
        await ctx.send("Ты уже создал себе покемона.")  # Сообщение, если покемон уже создан

# Запуск бота
bot.run(token)
