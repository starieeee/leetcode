def decrypt(decrypt_dict, encryptMsg):
    message = ""
    for char in encryptMsg:
        message += decrypt_dict[char]
    return message