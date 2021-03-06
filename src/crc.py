import numpy as np

# The divisor to be used in encoding and decoding in Cyclic Repetition Code.
divisor = [1, 0, 0, 1, 0, 1]
len_divisor = len(divisor)


def encode_crc(bits: list) -> list:
    """Encodes a given list of bits with CRC."""
    new_bits = list.copy(bits)
    bits_temp = list.copy(bits)
    for i in range(len_divisor - 1):
        bits_temp.append(0)
    bits_amount = len(new_bits)
    for i in range(bits_amount):
        if bits_temp[i] == 1:
            for j in range(len(divisor)):
                bits_temp[i + j] = int(np.logical_xor(bits_temp[i + j], divisor[j]))
    for i in range(len(divisor) - 1):
        new_bits.append(bits_temp[bits_amount + i])
    return new_bits


def decode_crc(bits: list) -> list:
    """Decodes a given list of bits with CRC."""
    bits_temp = list.copy(bits)
    bits_amount = len(bits)
    for i in range(bits_amount - len_divisor + 1):
        if bits_temp[i] == 1:
            for j in range(len_divisor):
                bits_temp[i + j] = int(np.logical_xor(bits_temp[i + j], divisor[j]))
    summ = 0
    for i in range(len_divisor):
        summ += bits_temp[bits_amount - 1 - i]

    if summ == 0:
        return bits[:-(len_divisor - 1)]
    elif summ == 1:
        new_bits = bits[:-(len_divisor - 1)]
        new_bits.append("F")
        return new_bits
    else:
        return ["R"]
