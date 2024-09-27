from __future__ import annotations

from dataclasses import dataclass

from core.domain.value_objects.lyrics import Lyrics
from shared.utils.id_utils import new_id


@dataclass
class Hymn:
    identifier: str
    title: str
    author: str
    lyrics: Lyrics

    @staticmethod
    def create(title: str, artist: str, content: str) -> Hymn:
        lyrics = Lyrics.parse_from_text(content)
        return Hymn(new_id(), title, artist, lyrics)
