import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session = vk_api.VkApi(token='2cd085bc56cb581fec1f84446f74e1fb93e93c30999660d7625ab3f189c4fac709826910ee0299647de55')

tools = vk_api.VkTools(vk_session)

longpoll = VkBotLongPoll(vk_session, 199664083)

vk = vk_session.get_api()

def get_name(uid: int) -> str:
    name = vk.users.get(user_id = uid)[0]
    return "{} {}".format(name['first_name'], name['last_name'])


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        print('New msg')
        print(str(event))
        print(event.message.from_id)
        print('Text: ', event.message.text)
        print(get_name(event.message.from_id))
        key, server, ts = vk.groups.getLongPollServer(group_id=199664083)
        print(key)
        print(server)
        print(ts)
        vk.messages.send(
            key = key,
            server = server,
            ts = ts,
            message="ответ",
            reply_to = event.message.message_id,
            random_id = vk_api.utils.get_random_id(),
        )