from hashlib import sha1, sha256, sha512
from Cryptodome.Cipher import AES
import hashlib
import hmac


def SHA1(data):
    sha = sha1()
    sha.update(data)
    return sha.hexdigest()


def SHA256(data):
    sha = sha256()
    sha.update(data)
    return sha.hexdigest()


def SHA512(data):
    sha = sha512()
    sha.update(data)
    return sha.hexdigest()


def HMAC_SHA1(key: bytes, msg: bytes):
    hmac_maker = hmac.new(key, msg, hashlib.sha1).hexdigest()
    return hmac_maker


def HMAC_SHA512(key: bytes, msg: bytes):
    hmac_maker = hmac.new(key, msg, hashlib.sha512).hexdigest()
    return hmac_maker


"""
    # performance bottleneck!
    # pls use hashlib.pbkdf2_hmac() or other API!
"""


def HMAC_pkcs5_pbkdf2(password: bytes, salt: bytes, iteration: int, dklen: int, sizeHmac=64):
    count = 1
    out_key_len = dklen
    obuf = b''
    key = b''
    while dklen > 0:
        a_salt = salt + count.to_bytes(4, byteorder='big', signed=False)
        # dl = bytes.fromhex(hmac.new(password, a_salt, hashlib.sha512).hexdigest())
        dl = hmac.new(password, a_salt, hashlib.sha512).digest()
        obuf = dl
        # ======================================================
        for index in range(1, iteration):
            # dl = bytes.fromhex(hmac.new(password, dl, hashlib.sha512).hexdigest())
            dl = hmac.new(password, dl, hashlib.sha512).digest()
            obuf = [obuf[i] ^ dl[i] for i in range(sizeHmac)]
            # obuf = accurate(dl, obuf, sizeHmac)
            obuf = b''.join([_.to_bytes(1, byteorder='big', signed=False) for _ in obuf])

            # obuf_tmp = b''
            # for i in range(sizeHmac):
            #     obuf_tmp += (obuf[i] ^ dl[i]).to_bytes(1, byteorder='big', signed=False)
            # obuf = obuf_tmp
            dl = obuf
        # =====================================================
        r = min(sizeHmac, out_key_len)
        dklen -= r
        count += 1
        key += obuf

    assert len(key) >= out_key_len
    return key[:out_key_len].hex()


def DecryptAES_CBC(key: bytes, msg: bytes, iv: bytes):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = cipher.decrypt(msg)
    return data.hex()
