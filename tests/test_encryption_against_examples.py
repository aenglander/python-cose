import json
from binascii import hexlify
from os import path
from typing import Dict

import pytest
from cose import encrypt, Key

from .example_helpers import EXAMPLE_ROOT

data_files = {
    "aes-ccm-examples": (
        "aes-ccm-01.json",
        "aes-ccm-02.json",
        "aes-ccm-03.json",
        "aes-ccm-04.json",
        "aes-ccm-05.json",
        "aes-ccm-06.json",
        "aes-ccm-07.json",
        "aes-ccm-08.json",
        "aes-ccm-enc-01.json",
        "aes-ccm-enc-02.json",
        "aes-ccm-enc-03.json",
        "aes-ccm-enc-04.json",
        "aes-ccm-enc-05.json",
        "aes-ccm-enc-06.json",
        "aes-ccm-enc-07.json",
        "aes-ccm-enc-08.json",
    ),
    "aes-gcm-examples": (
        "aes-gcm-01.json",
        "aes-gcm-02.json",
        "aes-gcm-03.json",
        "aes-gcm-04.json",
        "aes-gcm-enc-01.json",
        "aes-gcm-enc-02.json",
        "aes-gcm-enc-03.json",
    ),
    "chacha-poly-examples": ("chacha-poly-01.json", "chacha-poly-enc-01.json"),
    "hkdf-aes-examples": (
        "hmac-aes-128-01.json",
        "hmac-aes-128-02.json",
        "hmac-aes-128-03.json",
        "hmac-aes-128-04.json",
        "hmac-aes-128-05.json",
        "hmac-aes-128-06.json",
        "hmac-aes-128-07.json",
        "hmac-aes-128-08.json",
        "hmac-aes-128-09.json",
        "hmac-aes-128-10.json",
        "hmac-aes-128-11.json",
        "hmac-aes-128-12.json",
        "hmac-aes-128-13.json",
        "hmac-aes-128-14.json",
    ),
    "rsa-oaep-examples": (
        "ps256-128gcm-01.json",
        "ps512-256gcm-01.json",
        "ps-128gcm-01.json",
    ),
    "X25519-tests": (
        "x25519-hkdf-256-direct.json",
        "x25519-ss-hkdf-256-direct.json",
    ),
}

test_data = []
for directory, filenames in data_files.items():
    for filename in filenames:
        with open(path.join(EXAMPLE_ROOT, directory, filename)) as file:
            example = json.load(file)
            id = example["title"]
            plain_text = example["input"]["plaintext"]
            if "enveloped" in example["input"]:
                enc_env = "enveloped"
            elif "encrypted" in example["input"]:
                enc_env = "encrypted"
            elif "mac" in example["input"]:
                enc_env = "mac"
            else:
                raise ValueError(
                    'Neither enveloped, encrypted, or mac in example["input"]'
                )
            enc_alg = example["input"][enc_env]["protected"]["alg"]
            key = example["input"][enc_env]["recipients"][0]["key"]
            try:
                key_alg = example["input"][enc_env]["recipients"][0][
                    "protected"
                ]["alg"]
            except KeyError:
                key_alg = example["input"][enc_env]["recipients"][0][
                    "unprotected"
                ]["alg"]
            rng_stream = example["input"].get("rng_stream", [])
            output = example["output"]["cbor"].lower().encode("utf-8")
            test_data.append(
                pytest.param(
                    plain_text,
                    enc_alg,
                    key,
                    key_alg,
                    rng_stream,
                    output,
                    id=id,
                )
            )


@pytest.mark.skip
@pytest.mark.parametrize(
    "plain_text,enc_alg,key_data,key_alg,rng_stream,expected", test_data
)
def test_encrypt(
    plain_text: str,
    enc_alg: str,
    key_data: Dict[str, str],
    key_alg: str,
    rng_stream: str,
    expected: str,
):
    key = Key.from_data(key_data)
    actual = encrypt(plain_text.encode("utf-8"), key, enc_alg, key_alg)
    assert expected == hexlify(actual)
