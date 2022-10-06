from typing import Optional


def isolate_frame(frame: bytes, start_byte: bytes) -> Optional[bytes]:
    """
    Function isolating frame from given bytes.
    Function searches for starting byte and returns frame starting with it.
    Params:
        -frame - given frame to isolate
        -start_byte - given start byte
    Return:
        isolated frame or None if not found
    """
    frame_str = frame.decode("utf-8")
    try:
        frame_str = frame_str[frame_str.index(start_byte.decode("utf-8")) :]
        return frame_str.encode("utf-8")
    except ValueError:
        print("no start byte in frame")
    return None


def bytes_list_to_frame_string(bytes_list: list[bytes]) -> str:
    frame_str = ""
    for byte in bytes_list:
        hex_decimal_string = hex(int.from_bytes(byte, "little"))
        hex_decimal_string = hex_decimal_string[2:]  # delete "0x"
        if len(hex_decimal_string) < 2:
            hex_decimal_string = "0" + hex_decimal_string
        frame_str += hex_decimal_string + " "
    return frame_str


def string_to_bytes_list(frame_str: str) -> list[bytes]:
    return list(map(lambda x: bytes.fromhex(x), frame_str.strip().split(" ")))


def string_to_bytes(frame_str: str) -> bytes:
    return bytes.fromhex(frame_str)


def sum_list_bytes(bytes_list: list[bytes]) -> bytes:
    frame_length = len(bytes_list) - 1
    s = (
        sum(
            list(
                map(
                    lambda x: int.from_bytes(x, "little"),
                    bytes_list[1 : frame_length + 2],
                )
            )
        )
        % 256
    )
    return s.to_bytes(1, "little")
