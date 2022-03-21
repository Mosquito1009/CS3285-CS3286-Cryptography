import base64
import json
import os

import rsa

FILE_PRIV = 'siyao.txt'
FILE_PUB = 'gongyao.txt'

if os.path.exists(FILE_PRIV) and os.path.exists(FILE_PUB):
    with open(FILE_PRIV, 'r') as io:
        g_priv = rsa.PrivateKey(**json.load(io))
    with open(FILE_PUB, 'r') as io:
        g_pub = rsa.PublicKey(**json.load(io))
else:
    g_pub, g_priv = rsa.newkeys(512)

    with open(FILE_PRIV, 'w') as io:
        json.dump(dict(
            n=g_priv.n, e=g_priv.e, d=g_priv.d, p=g_priv.p, q=g_priv.q,
        ), io)

    with open(FILE_PUB, 'w') as io:
        json.dump(dict(
            n=g_pub.n, e=g_pub.e
        ), io)


def encrypt(data, pub):
    return base64.b64encode(rsa.encrypt(data.encode(), pub)).decode()


def decrypt(data, priv):
    return rsa.decrypt(base64.b64decode(data), priv).decode()


text = input('请输入加解密内容：')
is_decrypt = input('是否解密(Y/n)：') != 'n'

if is_decrypt:
    print(decrypt(text, g_priv))
else:
    print(encrypt(text, g_pub))
