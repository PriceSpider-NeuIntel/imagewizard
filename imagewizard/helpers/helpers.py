def bin_str_to_binary(value: str) -> bin:
    return bin(int(value, 2))

def hex_str_to_int(value: str) -> int:
    return int(value, 16)

def hex_str_to_hex(value: str) -> hex:
    return hex(int(value, 16))

def hex_to_bin(value: hex) -> bin:
    return bin(value)