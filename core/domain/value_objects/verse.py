from __future__ import annotations

from dataclasses import dataclass
from typing import AnyStr, Pattern, List


@dataclass
class Verse:
    number: int
    lines: List[str]
    is_chorus: bool = False

    VERSE_PATTERN: Pattern[AnyStr] = r"\[Verse](.*?)\[/Verse]"
    CHORUS_PATTERN: Pattern[AnyStr] = r"\[Chorus](.*?)\[/Chorus]"

    @staticmethod
    def create(number: int, lines: List[str], is_chorus: bool = False) -> Verse:

        if number <= 0:
            raise ValueError("Verse number must be positive.")

        if not lines:
            raise ValueError("Verse lines cannot be empty.")

        if not all(bool(line.strip()) for line in lines):
            raise ValueError("Verse lines cannot be empty.")

        return Verse(number, lines, is_chorus)
