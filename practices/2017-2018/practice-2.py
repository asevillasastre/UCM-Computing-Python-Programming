"""PRACTICE 2"""
def coder_atbash(message):
    """
    That function returns a message encrypted by reversing each letter
    Parameters
    -----------
    message
        clear string of characters

    Returns
    -----------
    cryptogram
        encrypted string of characters

    Example
    -----------
    >>> "A"
    "Z"
    """
    auxiliar_number_list, cryptogram = [], ""
    for letter in message:
        auxiliar_number_list.append(ord(letter))
    for auxiliar_number in auxiliar_number_list:
        capital_letter = auxiliar_number <= 90 and auxiliar_number >= 65
        small_letter = auxiliar_number >= 97 and auxiliar_number <= 122
        other_character = (not capital_letter) and (not small_letter)
        if capital_letter:
            cryptogram += chr(155-auxiliar_number)
        if small_letter:
            cryptogram += chr(219-auxiliar_number)
        if other_character:
            cryptogram += chr(auxiliar_number)
    return cryptogram
def decoder_atbash(cryptogram):
    """
    That function returns a decrypted which was encrypted by reversing each letter

    Parameters
    -----------
    cryptogram
        encrypted string of characters

    Returns
    -----------
    message
        clear string of character

    Example
    -----------
    >>>"Z"
    'A'
    """
    auxiliar_number_list, message = [], ""
    for letter in cryptogram:
        auxiliar_number_list.append(ord(letter))
    for auxiliar_number in auxiliar_number_list:
        capital_letter = auxiliar_number <= 90 and auxiliar_number >= 65
        small_letter = auxiliar_number >= 97 and auxiliar_number <= 122
        other_character = (not capital_letter) and (not small_letter)
        if capital_letter:
            message += chr(155-auxiliar_number)
        if small_letter:
            message += chr(219-auxiliar_number)
        if other_character:
            message += chr(auxiliar_number)
    return message
def coder_transposition(message):
    """
    That function returns an encrypted message by transposition method

    Parameters
    -----------
    message
        clear string of characters

    Returns
    -----------
    cryptogram
        encrypted string of characters

    Example
    -----------
    >>>"123456"
    '135246'
    """
    message_list, even_list, odd_list, j = [], [], [], 0
    for letter in message:
        message_list.append(letter)
    while j < len(message_list):
        if j % 2 == 0:
            even_list.append(message_list[j])
        else:
            odd_list.append(message_list[j])
        j += 1
    cryptogram = ""
    i = 0
    while i < len(even_list):
        cryptogram += even_list[i]
        i += 1
    i = 0
    while i < len(odd_list):
        cryptogram += odd_list[i]
        i += 1
    return cryptogram
def decoder_transposition(cryptogram):
    """
    That function returns a decrypted message which was encrypted by transposition method

    Parameters
    -----------
    cryptogram
        encrypted string of characters

    Returns
    -----------
    message
        clear string of characters

    Example
    -----------
    >>>"135246"
    '123456'
    """
    disordered_list, message_list, j, message = [], [], 0, ""
    for disordered_element in cryptogram:
        disordered_list.append(disordered_element)
    if len(disordered_list)%2 == 0:
        while j < len(disordered_list)//2:
            message_list.append(disordered_list[j])
            message_list.append(disordered_list[len(disordered_list)//2 + j])
            j += 1
    else:
        while j < len(disordered_list)//2:
            message_list.append(disordered_list[j])
            message_list.append(disordered_list[len(disordered_list)//2 + j + 1])
            j += 1
        message_list.append(disordered_list[len(disordered_list)//2])
    for letter in message_list:
        message += letter
    return message
