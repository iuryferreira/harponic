from core.domain.entities.hymn import Hymn


class TestHymn:

    def test_hymn_creation(self):
        title = "Amazing Grace"
        author = "John Newton"
        content = (
            "[Verse]\n"
            "Amazing grace! How sweet the sound\n"
            "That saved a wretch like me\n"
            "I once was lost, but now am found;\n"
            "Was blind, but now I see.\n"
            "[/Verse]\n"
        )
        hymn = Hymn.create(title, author, content)
        assert hymn.title == title
        assert hymn.author == author
        assert hymn.lyrics.verses[0].lines[0] == "Amazing grace! How sweet the sound"
        assert hymn.lyrics.verses[0].lines[1] == "That saved a wretch like me"
        assert hymn.lyrics.verses[0].lines[2] == "I once was lost, but now am found;"
        assert hymn.lyrics.verses[0].lines[3] == "Was blind, but now I see."
