from enum import Enum
from enum import unique
from typing import Collection
from typing import Tuple

from cose.key import Key


@unique
class Algorithm(Enum):
    pass


def sign(payload: bytes, keys: Key, algorithm: Algorithm) -> bytes:
    raise NotImplementedError


def counter_sign(payload: bytes, key: Key, algorithm: Algorithm) -> bytes:
    raise NotImplementedError


def verify_signatures(cose_payload: bytes, keys: Collection[Key]) -> bytes:
    raise NotImplementedError


def encrypt(payload: bytes, key: Key, algorithm: Algorithm) -> bytes:
    raise NotImplementedError


def encrypt_multiple(
    payload: bytes, keys: Collection[Tuple[Key, Algorithm]] = None
) -> bytes:
    raise NotImplementedError


def decrypt(payload: bytes, key: Key) -> bytes:
    raise NotImplementedError
