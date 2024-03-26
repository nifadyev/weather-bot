import re
from typing import Final


def escape_reserved_symbols(unsafe_value: str) -> str:
    """Escape reserved Telegram symbols.

    Based on `escape_markdown` from `python-telegram-bot`, source is available at
    https://github.com/python-telegram-bot/python-telegram-bot/blob/v20.6/telegram/helpers.py#L45-L78
    """
    escape_chars: Final[str] = r"\_*[]()~`>#+-=|{}.!"

    return re.sub(f"([{re.escape(escape_chars)}])", r"\\\1", unsafe_value)
