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
    try:
        frame = frame[frame.index(start_byte) :]
        return frame
    except ValueError:
        print("no start byte in frame")
    return None
