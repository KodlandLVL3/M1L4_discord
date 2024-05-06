import aiohttp  # Библиотека для асинхронных HTTP запросов
import random

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]

    async def get_name(self):
        # Асинхронный метод для получения имени покемона через PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API для запроса
        async with aiohttp.ClientSession() as session:  # Открытие сессии HTTP
            async with session.get(url) as response:  # Отправка GET запроса
                if response.status == 200:
                    data = await response.json()  # Получение и декодирование JSON ответа
                    return data['forms'][0]['name']  # Возврат имени покемона
                else:
                    return "Pikachu"  # Возврат стандартного имени, если запрос не удался

    async def info(self):
        # Метод возвращает информацию о покемоне
        if not self.name:
            self.name = await self.get_name()  # Получение имени, если оно еще не загружено
        return f"Имя твоего покемона: {self.name}"  # Возвращение строки с именем покемона

    async def show_img(self):
        # Асинхронный метод для получения URL изображения покемона через PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:  # Открытие сессии HTTP
            async with session.get(url) as response:  # Отправка GET запроса на получение данных о покемоне
                if response.status == 200:
                    data = await response.json()  # Получение JSON ответа
                    img_url = data['sprites']['front_default']  # Получение URL покемона
                    return img_url  # Возвращаем URL изображения
                else:
                    return None  # Возврат None, если запрос не удался
