import factory
from faker import Faker

from telethon.events import NewMessage
from telethon.tl.patched import Message

fake = Faker()

class MessageFactory(factory.Factory):
    class Meta:
        model = Message

    id = 1
    peer_id = 2
    message: str = fake.text()

class EventFactory(factory.Factory):
    class Meta:
        model = NewMessage.Event

    message = factory.SubFactory(MessageFactory)
