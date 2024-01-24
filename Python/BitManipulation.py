# Get Bit to see what ith bit is
# @param: num int - the input num
# @param: i int - ith bit to get, right least significant bit is 0th bit
# @return bool - True for 1 or False for 0 for the ith bit
def get_bit(num: int, i: int) -> bool:
    # left shift 1 by i to look like 0001000
    # use bitwise AND & to clear all other bits
    # if ith bit is 1, then result is not 0, return True indicate bit is 1
    # if ith bit is 0, then result is 0, return False indicate bit is 0
    print(f"\nInput num is: {bin(num)} i is: {i}")
    print(f"Left shit 1 by i: {bin(1 << i)}")
    print(f"num & (1<<i) : {num & (1 << i)}")
    print("Is result not zero 0?")
    return num & (1 << i) != 0


num = 0b1101
# num: the 0th bit is 1 or True
print(get_bit(num, 0))

# num: the 1st bit is 0 or False
print(get_bit(num, 1))

# num: the 2nd bit is 1 or True
print(get_bit(num, 2))

# num: the 3rd bit is 1 or True
print(get_bit(num, 3))


# Set Bit to set ith bit to 1
# @param: num int
# @param: i int
# @return: int

def set_bit(num: int, i: int) -> int:
    print(f"\nInput num: {bin(num)} i: {i}")
    print(f"left shift 1 by i: {bin(1 << i)}")
    return num | (1 << i)


num = 0b1000
print(bin(set_bit(num, 0)))


def clear_bit(num: int, i: int) -> int:
    print(f"\nInput num: {bin(num)} i: {i}")
    mask = ~(1 << i)  # 1110111, use 0 to mask ith bit
    return num & mask


num = 0b1111
print(bin(clear_bit(num, 2)))


def clear_bit_msb_to_i(num: int, i: int) -> int:
    print(f"\nclear_bit_msb_to_i")
    print(f"Input num: {bin(num)} i: {i}")
    mask = (1 << i) - 1  # 0001000 -> 0000111
    return num & mask


num = 0b1111
print(bin(clear_bit_msb_to_i(num, 2)))


def clear_bit_i_to_lsb(num: int, i: int) -> int:
    print(f"\nclear_bit_i_to_lsb")
    print(f"Input num: {bin(num)} i: {i}")
    mask = -1 << (i + 1)
    return num & mask


num = 0b1111
print(bin(clear_bit_i_to_lsb(num, 2)))


def update_bit(num: int, i: int, bitIs1: bool) -> int:
    print(f"\nupdate bit")
    print(f"Input num: {bin(num)} i: {i} bitIs1: {bitIs1}")
    value = 1 if bitIs1 else 0
    mask = ~(1 << i)
    return (num & mask) | (value << i)


num = 0b1111
print(bin(update_bit(num, 2, 0)))
