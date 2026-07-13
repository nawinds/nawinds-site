from pathlib import Path

from babel.messages.pofile import read_po
from flask_babel import pgettext


POT_PATH = Path(__file__).parent / "translations/messages.pot"


def load_messages(path: Path) -> dict[str, str]:
    with path.open("r", encoding="utf-8") as file:
        catalog = read_po(file)

    messages: dict[str, str] = {}

    for message in catalog:
        if not message.id or not message.context:
            continue

        if isinstance(message.id, tuple):
            raise ValueError(
                f"Plural message is not supported for context: {message.context}"
            )

        if message.context in messages:
            raise ValueError(
                f"Duplicate msgctxt in {path}: {message.context}"
            )

        messages[message.context] = message.id

    return messages


SOURCE_MESSAGES = load_messages(POT_PATH)


def tr(message_id: str, **variables) -> str:
    source_text = SOURCE_MESSAGES.get(message_id)

    if source_text is None:
        raise KeyError(f"Unknown translation ID: {message_id}")

    return pgettext(message_id, source_text, **variables)


_ = tr
