def crypt(text: str, key_str: str, is_decrypt=False, is_phantom=False):
    content = text.split(' ')
    key = {}
    key_items = key_str.split(',')
    if is_phantom:
        key_items = reversed(key_items)
    for i, v in enumerate(key_items):
        if is_decrypt:
            key[int(v) - 1] = i
        else:
            key[i] = int(v) - 1
    data = [''] * len(content)
    for k, v in key.items():
        data[k] = content[v]
    return ' '.join(data)


g_content = input('请输入加解密内容：')
g_key = input('请输入加密密钥：')
g_is_decrypt = input('是否解密内容（Y/n）：').lower() != 'n'
g_is_phantom = input('是否幻方加密（Y/n）：').lower() != 'n'
print('结果:', crypt(g_content, g_key, g_is_decrypt, g_is_phantom))
