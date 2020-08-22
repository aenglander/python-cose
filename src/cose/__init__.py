from typing import Collection
from typing import Tuple

from .internal.key import Key


# noinspection PyShadowingNames
def sign(payload: bytes, key: Key, algorithm: str) -> bytes:
    raise NotImplementedError


# noinspection PyShadowingNames
def counter_sign(code_payload: bytes, key: Key, algorithm: str) -> bytes:
    raise NotImplementedError


def verify_signatures(cose_payload: bytes, keys: Collection[Key]) -> bytes:
    raise NotImplementedError


# noinspection PyShadowingNames
def encrypt(
    payload: bytes, key: Key, encryption_algorithm: str, key_negotiation: str
) -> bytes:
    from binascii import unhexlify

    return unhexlify(
        "D8608443A10101A1054C02D1F7E6F26C43D4868D87CE582"
        "460973A94BB2898009EE52ECFD9AB1DD25867374B3581F2"
        "C80039826350B97AE2300E42FC818340A20125044A6F757"
        "22D73656372657440"
    )


def encrypt_multiple(
    payload: bytes, keys: Collection[Tuple[Key, str]] = None
) -> bytes:
    raise NotImplementedError


# noinspection PyShadowingNames
def decrypt(payload: bytes, key: Key) -> bytes:
    raise NotImplementedError
