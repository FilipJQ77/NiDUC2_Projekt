def encode_hamming(bits: list) -> list:
    """Encodes a given list of bits with Hamming code.
    https://en.wikipedia.org/wiki/Hamming_code#General_algorithm"""
    new_bits = list.copy(bits)
    bits_amount = len(new_bits)
    index = 1
    # adding parity bits in correct places to the list
    while index <= bits_amount:
        new_bits.insert(index - 1, 0)
        bits_amount += 1
        index *= 2
    # algorithm step 5
    index = 1
    while index <= bits_amount:
        i = index
        summ = 0
        while i <= bits_amount:
            for j in range(index):
                # we need to check if we haven't exceeded data amount (in case the Hamming code is not full)
                if i <= bits_amount:
                    summ += new_bits[i - 1]
                    i += 1
            i += index
        new_bits[index - 1] = summ % 2
        index *= 2
    # after encoding the information with Hamming code we add an extra parity bit (SECDED)
    summ = 0
    for i in range(bits_amount):
        summ += new_bits[i]
    new_bits.append(summ % 2)
    return new_bits


def decode_hamming(bits: list) -> list:
    """Decodes a given list of bits with Hamming code."""
    bits_amount = len(bits)
    index = 1
    wrong_bit_index = 0
    is_fixed = ""
    while index < bits_amount:
        i = index
        summ = 0
        while i < bits_amount:
            for j in range(index):
                # we need to check if we haven't exceeded data amount (in case the Hamming code is not full)
                if i < bits_amount:
                    summ += bits[i - 1]
                    i += 1
            i += index
        if summ % 2 != 0:
            wrong_bit_index += index
        index *= 2

    if 0 < wrong_bit_index <= bits_amount:
        wrong_bit_index -= 1
        if bits[wrong_bit_index]:
            bits[wrong_bit_index] = 0
        else:
            bits[wrong_bit_index] = 1
        summ = 0
        # checking the additional parity bit
        for i in range(bits_amount - 1):
            summ += bits[i]
        if summ % 2 == bits[-1]:
            is_fixed = "F"
        else:
            return ["R"]

    index = 1
    new_bits = []
    for i in range(bits_amount - 1):
        if i + 1 == index:
            index *= 2
        else:
            new_bits.append(bits[i])
    if is_fixed:
        new_bits.append(is_fixed)
    return new_bits
