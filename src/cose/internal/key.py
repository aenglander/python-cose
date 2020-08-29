from enum import Enum
from enum import unique
from typing import Dict
from typing import List
from typing import Optional


@unique
class Use(Enum):
    SIGNATURE = "sig"
    ENCRYPTION = "enc"


@unique
class KeyType(Enum):
    OKP = 1
    EC2 = 2
    RSA = 3
    SYMMETRIC = 4
    HSS_LMS = 5


@unique
class KeyOp(Enum):
    SIGN = 1
    VERIFY = 2
    ENCRYPT = 3
    DECRYPT = 4
    WRAP_KEY = 5
    UNWRAP_KEY = 6
    DERIVE_KEY = 7
    DERIVE_BITS = 8
    MAC_CREATE = 9
    MAC_VERIFY = 10


@unique
class EC2Curve(Enum):
    P_256 = 1
    P_384 = 2
    P_521 = 3
    SECP256K1 = 8


@unique
class OKPCurve(Enum):
    X25519 = 4
    X448 = 5
    ED25519 = 6
    ED448 = 7


class Key:
    def __init__(
        self, kty: KeyType, kid: Optional[str], key_ops: Optional[List[KeyOp]]
    ) -> None:
        self.__kty = kty
        self.__kid = kid
        self.__key_ops = key_ops

    @staticmethod
    def from_data(key_data: Dict[str, str]) -> "Key":
        return Key(KeyType.SYMMETRIC, None, None)


class EllipticalCurve2PrivateKey(Key):
    def __init__(
        self,
        curve: EC2Curve,
        private_key: bytes,
        x: bytes = None,
        kid: str = None,
        key_ops: List[KeyOp] = None,
    ) -> None:
        super().__init__(KeyType.EC2, kid, key_ops)
        self.__curve = curve
        self.__x = x
        self.__private_key = private_key


class EllipticalCurve2PublicKey(Key):
    def __init__(
        self,
        curve: EC2Curve,
        x: bytes,
        y: bytes,
        kid: str = None,
        key_ops: List[KeyOp] = None,
    ) -> None:
        super().__init__(KeyType.EC2, kid, key_ops)
        self.__curve = curve
        self.__x = x
        self.__y = y


class OctetKeyPairPrivateKey(Key):
    def __init__(
        self,
        curve: OKPCurve,
        private_key: str,
        x: str = None,
        kid: str = None,
        key_ops: List[KeyOp] = None,
    ) -> None:
        super().__init__(KeyType.OKP, kid, key_ops)
        self.__curve = curve
        self.__x = x
        self.__private_key = private_key


class OctetKeyPairPublicKey(Key):
    def __init__(
        self,
        curve: OKPCurve,
        x: str,
        kid: str = None,
        key_ops: List[KeyOp] = None,
    ) -> None:
        super().__init__(KeyType.OKP, kid, key_ops)
        self.__curve = curve
        self.__x = x


class SymmetricKey(Key):
    def __init__(
        self,
        key: bytes,
        kid: Optional[str] = None,
        key_ops: Optional[List[KeyOp]] = None,
    ):
        super().__init__(KeyType.SYMMETRIC, kid, key_ops)
        self.__key = key
