import time
import logging
import asyncio
import mysql
import test


from aiogram import Bot, Dispatcher, executor, types

TOKEN = "6044222034:AAGJTlac_jQa-QjfSMId7IUOapuaMoaW0NE"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    global user_full_name 
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply(f"Привет, {user_full_name}! Меня зовут RemoteContrl, для того, чтобы узнать зачем я создан, напиши \" /help \"")
def usernames():
        return user_full_name   

@dp.message_handler(commands=['help'])
async def start_handler(message: types.Message):
    user_full_name = message.from_user.full_name
    await message.reply(f"Дорогой, {user_full_name}, этот бот создан для хранения в БД имен написавших! Если вы согласны оставть свое имя напишите \"Да\" ")

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    if msg.text.lower() == 'да':
        usernames()
        test.tests()
        await msg.answer('Привет, спасибо за содействие!')
        
         
    elif msg.text.lower() == 'нет':
           await msg.answer('Очень жаль(')
    else:
       await msg.answer('Не понимаю, что это значит')
           

if __name__ == "__main__":
    executor.start_polling(dp)