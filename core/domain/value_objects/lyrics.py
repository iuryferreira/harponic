from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from core.domain.value_objects.verse import Verse


@dataclass
class Lyrics:
    verses: list[Verse] = field(default_factory=list)

    @staticmethod
    def parse_from_text(text: str) -> Lyrics:

        verses: List[Verse] = []
        verse_counter = 1

        lines = text.strip().split("\n")

        current_block = None
        current_lines = []

        for line in lines:
            line = line.strip()

            if bool(line) is False:
                continue

            if line.startswith("[Verse]"):
                if current_block is not None:
                    raise ValueError("Cannot start a new verse without closing the previous one.")
                current_block = "verse"
                current_lines = []
            elif line.startswith("[Chorus]"):
                if current_block is not None:
                    raise ValueError("Cannot start a new chorus without closing the previous one.")
                current_block = "chorus"
                current_lines = []
            elif line.startswith("[/Verse]"):
                if current_block != "verse":
                    raise ValueError("Cannot close a verse without starting one.")
                verses.append(Verse.create(verse_counter, current_lines))
                verse_counter += 1
                current_block = None
            elif line.startswith("[/Chorus]"):
                if current_block != "chorus":
                    raise ValueError("Cannot close a chorus without starting one.")
                verses.append(Verse.create(verse_counter, current_lines, is_chorus=True))
                current_block = None
            else:
                if current_block is None:
                    raise ValueError("Cannot add a line outside a verse or chorus block.")
                current_lines.append(line)

        return Lyrics(verses)
