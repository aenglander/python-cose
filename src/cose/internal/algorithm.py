from enum import Enum
from enum import unique


@unique
class SignatureAlgorithm(Enum):
    # Elliptical Curve Digital Signature Algorithm
    ES256 = -7  # ECDSA w/SHA-256
    ES384 = -35  # ECDSA w/SHA-384
    ES512 = -36  # ECDSA w/SHA-512

    # Edwards Curve Digital Signature Algorithm
    EDDSA = -8  # Pure EdDSA with no hash


@unique
class MACAlgorithm(Enum):
    # Hash-Based Message Authentication Codes
    HMAC_256_64 = 4  # HMAC w/SHA-256 truncated to 64 bits
    HMAC_256_256 = 5  # HMAC w/SHA-256
    HMAC_384_384 = 6  # HMAC w/SHA-384
    HMAC_512_512 = 7  # HMAC w/SHA-512

    # AES Message Authentication Code
    AES_MAC_128_64 = 14  # AES-CBC-MAC: 128 bit key, 64-bit tag
    AES_MAC_256_64 = 15  # AES-CBC-MAC: 256 bit key, 64-bit tag
    AES_MAC_128_128 = 35  # AES-CBC-MAC: 128 bit key, 128-bit tag
    AES_MAC_256_128 = 36  # AES-CBC-MAC: 256 bit key, 128-bit tag


@unique
class ContentEncryptionAlgorithm(Enum):
    # AES Encryption in Galois Counter Mode
    A128GCM = 1  # AES-GCM mode w/128-bit key, 128-bit tag
    A192GCM = 2  # AES-GCM mode w/192-bit key, 128-bit tag
    A256GCM = 3  # AES-GCM mode w/256-bit key, 128-bit tag

    # AES encryption in Counter with CBC MAC mode
    AES_CCM_16_64_128 = 10  # AES-CCM: 128-bit key, 64-bit tag, 13-byte nonce
    AES_CCM_16_64_256 = 11  # AES-CCM: 256-bit key, 64-bit tag, 13-byte nonce
    AES_CCM_64_64_128 = 12  # AES-CCM: 128-bit key, 64-bit tag, 7-byte nonce
    AES_CCM_64_64_256 = 13  # AES-CCM: 256-bit key, 64-bit tag, 7-byte nonce
    AES_CCM_16_128_128 = 30  # AES-CCM: 128-bit key, 128-bit tag, 13-byte nonce
    AES_CCM_16_128_256 = 31  # AES-CCM: 256-bit key, 128-bit tag, 13-byte nonce
    AES_CCM_64_128_128 = 32  # AES-CCM: 128-bit key, 128-bit tag, 7-byte nonce
    AES_CCM_64_128_256 = 33  # AES-CCM: 256-bit key, 128-bit tag, 7-byte nonce

    CHACHA20_POLY1305 = 24  # ChaCha20/Poly1305 w/ 256-bit key, 128-bit tag


@unique
class KeyDerivationFunction(Enum):
    DIRECT = -6  # Shared secret

    # HMAC-Based Extract-and-Expand Key Derivation Function
    DIRECT_HKDF_SHA_256 = -10  # Shared secret w/HKDF and SHA-256
    DIRECT_HKDF_SHA_512 = -11  # Shared secret w/HKDF and SHA-512
    DIRECT_HKDF_AES_128 = -12  # Shared secret w/AES-MAC 128-bit key
    DIRECT_HKDF_AES_256 = -13  # Shared secret w/AES-MAC 256-bit key

    # AES Key Wrap
    A128KW = -3  # AES Key Wrap w/128-bit key
    A192KW = -4  # AES Key Wrap w/192-bit key
    A256KW = -5  # AES Key Wrap w/256-bit key


class KeyTransport:
    pass


@unique
class DirectKeyAgreement(Enum):
    # Elliptical Curve Diffie-Hellman
    ECDH_ES_HKDF_256 = -25  # ECDH ES w/HKDF and SHA-256
    ECDH_ES_HKDF_512 = -26  # ECDH ES w/HKDF and SHA-512
    ECDH_SS_HKDF_256 = -27  # ECDH SS w/HKDF and SHA-256
    ECDH_SS_HKDF_512 = -28  # ECDH SS w/HKDF and SHA-512


class KeyAgreementWithKeyWrap(Enum):
    # Elliptical Curve Diffie-Hellman
    ECDH_ES_A128KW = -29  # ECDH ES w/Concat KDF and AES Key Wrap w/128-bit key
    ECDH_ES_A192KW = -30  # ECDH ES w/Concat KDF and AES Key Wrap w/192-bit key
    ECDH_ES_2568KW = -31  # ECDH ES w/Concat KDF and AES Key Wrap w/256-bit key
    ECDH_SS_A128KW = -32  # ECDH SS w/Concat KDF and AES Key Wrap w/128-bit key
    ECDH_SS_A192KW = -33  # ECDH SS w/Concat KDF and AES Key Wrap w/192-bit key
    ECDH_SS_2568KW = -34  # ECDH SS w/Concat KDF and AES Key Wrap w/256-bit key
