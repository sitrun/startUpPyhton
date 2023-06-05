from loader import *
from handlers import start
from handlers import test


async def set_commands(bot: Bot):

    commands = [
        types.BotCommandScopeAllPrivateChats(command="/start", description="Перезапуск"),
        types.BotCommandScopeAllPrivateChats(command="/test_func", description="Тестируем бота"),
        types.BotCommandScopeAllPrivateChats(command="/options", description="Настройки"),
        types.BotCommandScopeAllPrivateChats(command="/help", description="Справка")
    ]

    await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats(), language_code='ru')
    await bot.delete_my_commands(scope=types.BotCommandScopeDefault(), language_code='ru')
    await bot.set_my_commands(commands, scope=types.BotCommandScopeAllPrivateChats(), language_code='ru')


async def go():

    await set_commands(bot)
    r = await aioredis.Redis(host='localhost', port=6379, password=str(REDIS_AUTH), db=0)
    # r = await aioredis.Redis(host='localhost', port=6379, db=0)
    storage = RedisStorage(r)
    dp: Dispatcher = Dispatcher(storage=storage)
    dp.include_router(start.router)
    dp.include_router(test.router)
    print("Бот удачно запущен!")
    await dp.start_polling(bot)

    # sync def set_default_commands(dp):


if __name__ == "__main__":
    asyncio.run(go())
