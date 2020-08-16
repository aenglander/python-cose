from enum import Enum
from enum import unique


@unique
class ContextAlgorithmParameters(Enum):
    PARTY_U = -21
    PARTY_U_NONCE = -22
    PARTY_U_OTHER = -23
    PARTY_V = -24
    PARTY_V_NONCE = -25
    PARTY_V_OTHER = -26


@unique
class Core(Enum):
    ENCRYPT_0 = 16
    MAC_0 = 17
    SIGN_1 = 18
    ENCRYPT = 96
    MAC = 97
    SIGN = 98
    KEY = 101
    KEY_SET = 102


@unique
class CommonHeaders(Enum):
    ALG = 1
    CRIT = 2
    CONTENT_TYPE = 3
    KID = 4
    IV = 5
    PARTIAL_IV = 6
    COUNTER_SIGNATURE = 7


@unique
class KeyCommonParameters(Enum):
    KTY = 1
    KID = 2
    KEY_PARM_ALG = 3
    KEY_PARM_KEY_OPS = 4
    KEY_PARM_BASE_4 = 5


@unique
class KeyOperationValues(Enum):
    SIGN: 1
    VERIFY: 2
    ENCRYPT: 3
    DECRYPT: 4
    WRAP_KEY: 5
    UNWRAP_KEY: 6
    DERIVE_KEY: 7
    DERIVE_BITS: 8
    MAC_CREATE: 9
    MAC_VERIFY: 10


@unique
class KeyTypeValues(Enum):
    DIRECT = -6
    DIRECT_HKDF_SHA_256 = -10
    DIRECT_HKDF_SHA_512 = -11
    DIRECT_HKDF_AES_128 = -12
    DIRECT_HKDF_AES_256 = -13


@unique
class KeyObjectParameters(Enum):
    OKP: 1
    EC2: 2
    SYMMETRIC: 5
    RESERVED: 0


@unique
class EllipticCurveKeys(Enum):
    P_256: 1
    P_384: 2
    P_512: 3
    X25519: 4
    X448: 5
    ED25519: 6
    ED448: 7


class KeyParameters(Enum):
    CRV: -1
    K: -1
    X: -2
    Y: -3
    D: -4


@unique
class DigitalSignatureAlgorithms(Enum):
    ES_256 = -7
    ES_384 = -35
    ES_512 = -36
    ED_DSA = -8


@unique
class MacAlgorithms(Enum):
    HMAC_SHA_256_64 = 4
    HMAC_SHA_256_256 = 5
    HMAC_SHA_384_384 = 6
    HMAC_SHA_512_512 = 7

    AES_MAC_128_64 = 14
    AES_MAC_256_64 = 15
    AES_MAC_128_128 = 25
    AES_MAC_256_128 = 26


@unique
class ContentEncryptionAlgorithms(Enum):
    AES_128_CGM = 1
    AES_192_CGM = 2
    AES_256_CGM = 3

    AES_CCM_16_64_128 = 10
    AES_CCM_16_64_256 = 11
    AES_CCM_64_64_128 = 12
    AES_CCM_64_64_256 = 13
    AES_CCM_16_128_128 = 30
    AES_CCM_16_128_256 = 31
    AES_CCM_64_128_128 = 32
    AES_CCM_64_128_256 = 33

    CHA_CHA_20_POLY_1305 = 24


@unique
class AESKeyWrapAlgorithms(Enum):
    AES_128_KW = -3
    AES_192_KW = -4
    AES_256_KW = -5


@unique
class ECDHAlgorithms(Enum):
    ECDH_ES_HKDF_256 = -25
    ECDH_ES_HKDF_512 = -26
    ECDH_SS_HKDF_256 = -27
    ECDH_SS_HKDF_512 = -28

    ECDH_ES_A128KW = -29
    ECDH_ES_A192KW = -30
    ECDH_ES_A256KW = -31
    ECDH_SS_A128KW = -32
    ECDH_SS_A192KW = -33
    ECDH_SS_A256KW = -34


@unique
class ECDHAlgorithmParameters(Enum):
    ephemeral_key = -1
    static_key = -2
    static_key_id = -3


@unique
class HKDFAlgorithms(Enum):
    SALT = -20
