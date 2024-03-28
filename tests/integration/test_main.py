import pytest
from src.constants.messages import START_MESSAGE
from telethon.events import StopPropagation
from src.main import start

from tests.conftest import EventFactory, MessageFactory


# ! WIP - not working because EventFactory has no chat attr
@pytest.mark.asyncio
async def test_start(event_loop):
    message = MessageFactory.build()
    event = EventFactory.build(message=message)

    # .respond() returns None because there is no event.client
    with pytest.raises(StopPropagation):
        assert await start(event) == START_MESSAGE
