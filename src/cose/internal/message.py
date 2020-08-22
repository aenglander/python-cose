from collections import namedtuple
from typing import Any
from typing import Dict
from typing import List
from typing import Set
from typing import Union


HeaderParameter = namedtuple("HeaderParameter", ["label", "must_protect"])
ReservedHeaderParameter = HeaderParameter(0, False)
AlgHeaderParameter = HeaderParameter(1, False)
CritHeaderParameter = HeaderParameter(2, True)
ContentTypeHeaderParameter = HeaderParameter(3, False)
KeyIDHeaderParameter = HeaderParameter(4, False)
IVHeaderParameter = HeaderParameter(5, False)
PartialIVHeaderParameter = HeaderParameter(6, False)
CounterSignatureHeaderParameter = HeaderParameter(7, False)
CounterSignature0HeaderParameter = HeaderParameter(9, False)
KeyIDContextHeaderParameter = HeaderParameter(10, False)
X5BagHeaderParameter = HeaderParameter(32, False)
X5ChainHeaderParameter = HeaderParameter(33, False)
X5THeaderParameter = HeaderParameter(34, False)
X5UHeaderParameter = HeaderParameter(35, True)

HeaderLabel = Union[str, int]
ProtectedHeaders = Set[HeaderParameter]
UnprotectedHeaders = Dict[HeaderParameter, Any]


class Signature:
    pass


class Taggable:
    def __init__(self, tag: int):
        self.__tag = tag

    @property
    def tag(self):
        return self.__tag


class Message:
    def __init__(
        self,
        protected_header_parameters: ProtectedHeaders,
        unprotected_header_parameters: UnprotectedHeaders,
        content: bytes,
    ) -> None:
        self.__protected_header_parameters = protected_header_parameters
        self.__unprotected_header_parameters = unprotected_header_parameters
        self.__content = content

    @property
    def protected_header_parameters(self):
        return None

    @property
    def unprotected_header_parameters(self):
        return None

    @property
    def content(self):
        return None


class SignMessage(Message, Taggable):
    def __init__(
        self,
        protected_headers: ProtectedHeaders,
        unprotected_headers: UnprotectedHeaders,
        payload: bytes,
        signatures: List[Signature],
    ) -> None:
        Taggable.__init__(self, 98)
        self.__protected_headers = protected_headers
        self.__unprotected_headers = unprotected_headers
        self.__payload = payload
        self.__signatures = signatures


class Sign1Message(Message, Taggable):
    def __init__(self) -> None:
        Taggable.__init__(self, 18)


class EncryptMessage(Message, Taggable):
    def __init__(self) -> None:
        Taggable.__init__(self, 96)


class Encrypt0Message(Message, Taggable):
    def __init__(self) -> None:
        Taggable.__init__(self, 16)


class MacMessage(Message, Taggable):
    def __init__(self) -> None:
        Taggable.__init__(self, 97)


class Mac0Message(Message, Taggable):
    def __init__(self) -> None:
        Taggable.__init__(self, 17)


class TaggedMessage(Message):
    pass


class SignTaggedMessage(TaggedMessage, SignMessage):
    pass


class Sing1TaggedMessage(TaggedMessage, Sign1Message):
    pass


class EncryptTaggedMessage(TaggedMessage, EncryptMessage):
    pass


class Encrypt0TaggedMessage(TaggedMessage, Encrypt0Message):
    pass


class MacTaggedMessage(TaggedMessage, MacMessage):
    pass


class Mac0TaggedMessage(TaggedMessage, Mac0Message):
    pass
