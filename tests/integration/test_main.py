import pytest

from src.main import echo
from tests.fixtures import EventFactory, MessageFactory

# ! WIP
@pytest.mark.asyncio
async def test_echo(event_loop):
    message = MessageFactory.build()
    event = EventFactory.build(message=message)

    # .respond() returns None because there is no event.client
    assert await echo(event) == event.text
