import os

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)
    longpoll = VkBotLongPoll(vk_session, '193402549')
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            vk = vk_session.get_api()
            response = vk.users.get(user_id=event.obj.message['from_id'],
                                    fields="bdate, city")
            # print(response)
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"Привет, {response[0]['first_name']}",
                             random_id=random.randint(0, 2 ** 64))
            if 'city' in response[0]:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Как поживает {response[0]['city']['title']}?",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    TOKEN = str(os.environ.get("TOKEN"))
    main()
