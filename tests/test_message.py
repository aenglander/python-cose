from cose.internal.message import (
    Taggable,
    SignMessage,
    Sign1Message,
    EncryptMessage,
    Encrypt0Message,
    Mac0Message,
    MacMessage,
)


class TestTaggable:
    def test_tag(self):
        assert 999 == Taggable(999).tag


class TestSignMessage:
    def test_tag(self) -> None:
        assert 98 == SignMessage(set(), dict(), b"", list()).tag


class TestSign1Message:
    def test_tag(self):
        assert 18 == Sign1Message().tag


class TestEncryptMessage:
    def test_tag(self):
        assert 96 == EncryptMessage().tag


class TestEncrypt0Message:
    def test_tag(self):
        assert 16 == Encrypt0Message().tag


class TestMacMessage:
    def test_tag(self):
        assert 97 == MacMessage().tag


class TestMac0Message:
    def test_tag(self):
        assert 17 == Mac0Message().tag
