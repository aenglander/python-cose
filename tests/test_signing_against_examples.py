from binascii import hexlify
from typing import Dict

import cose
import pytest
from cose.internal.key import ECKey, Key

keys: Dict[str, Key] = {
    "11": ECKey(
        **{
            "kty": "EC",
            "kid": "11",
            "crv": "P-256",
            "x": "usWxHK2PmfnHKwXPS54m0kTcGJ90UiglWiGahtagnv8",
            "y": "IBOL-C3BttVivg-lSreASjpkttcsz-1rb7btKLv8EX4",
            "d": "V8kgd2ZBRuh2dgyVINBUqpPDr7BOMGcF22CQMIUHtNM",
        }
    ),
}


@pytest.mark.skip
def test_single_signature():
    r""""
    C.1.1.  Single Signature

    This example uses the following:

    o  Signature Algorithm: ECDSA w/ SHA-256, Curve P-256

    Size of binary file is 103 bytes

    98(
      [
        / protected / h'',
        / unprotected / {},
        / payload / 'This is the content.',
        / signatures / [
          [
            / protected / h'a10126' / {
                \ alg \ 1:-7 \ ECDSA 256 \
              } / ,
            / unprotected / {
              / kid / 4:'11'
            },
            / signature / h'e2aeafd40d69d19dfe6e52077c5d7ff4e408282cbefb
    5d06cbf414af2e19d982ac45ac98b8544c908b4507de1e90b717c3d34816fe926a2b
    98f53afd2fa0f30a'
          ]
        ]
      ]
    )
    """
    expected = (
        b"e2aeafd40d69d19dfe6e52077c5d7ff4e408282cbe"
        b"fb5d06cbf414af2e19d982ac45ac98b8544c908b45"
        b"07de1e90b717c3d34816fe926a2b98f53afd2fa0f30a"
    )
    actual = hexlify(cose.sign(b"This is the content.", [keys["11"]]))
    assert expected == actual
