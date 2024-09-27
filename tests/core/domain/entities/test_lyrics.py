import pytest

from core.domain.value_objects.lyrics import Lyrics


class TestLyrics:

    def test_parse_with_single_verse(self):
        text = """
        [Verse]
        This is the first verse.
        [/Verse]
        """

        lyrics = Lyrics.parse_from_text(text)

        assert len(lyrics.verses) == 1
        assert lyrics.verses[0].number == 1
        assert lyrics.verses[0].lines == ["This is the first verse."]

    def test_parse_with_multiple_verses(self):
        text = """
        [Verse]
        This is the first verse.
        [/Verse]

        [Verse]
        This is the second verse.
        [/Verse]
        """

        lyrics = Lyrics.parse_from_text(text)

        assert len(lyrics.verses) == 2
        assert lyrics.verses[0].number == 1
        assert lyrics.verses[0].lines == ["This is the first verse."]
        assert lyrics.verses[1].number == 2
        assert lyrics.verses[1].lines == ["This is the second verse."]

    def test_parse_with_verse_and_chorus(self):
        text = """
        [Verse]
        This is the first verse.
        [/Verse]

        [Chorus]
        This is the chorus.
        [/Chorus]
        """

        lyrics = Lyrics.parse_from_text(text)

        assert len(lyrics.verses) == 2
        assert lyrics.verses[0].number == 1
        assert lyrics.verses[0].lines == ["This is the first verse."]
        assert lyrics.verses[1].number == 2
        assert lyrics.verses[1].lines == ["This is the chorus."]
        assert lyrics.verses[1].is_chorus == True

    def test_parse_starting_verse_without_closing_previous(self):
        text = """
        [Verse]
        This is the first verse.
        [Verse]
        This is the second verse.
        [/Verse]
        """
        with pytest.raises(ValueError, match="Cannot start a new verse without closing the previous one."):
            Lyrics.parse_from_text(text)

    def test_parse_starting_chorus_without_closing_previous(self):
        text = """
        [Chorus]
        This is the chorus.
        [Chorus]
        This is another chorus.
        [/Chorus]
        """
        with pytest.raises(ValueError, match="Cannot start a new chorus without closing the previous one."):
            Lyrics.parse_from_text(text)

    def test_parse_closing_verse_without_opening(self):
        text = """
        [/Verse]
        """
        with pytest.raises(ValueError, match="Cannot close a verse without starting one."):
            Lyrics.parse_from_text(text)

    def test_parse_closing_chorus_without_opening(self):
        text = """
        [/Chorus]
        """
        with pytest.raises(ValueError, match="Cannot close a chorus without starting one."):
            Lyrics.parse_from_text(text)

    def test_parse_adding_line_outside_of_block(self):
        text = """
        This is a line outside any block.
        """
        with pytest.raises(ValueError, match="Cannot add a line outside a verse or chorus block."):
            Lyrics.parse_from_text(text)
