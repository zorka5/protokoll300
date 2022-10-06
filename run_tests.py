from tests.tests_utils import test_isolate_frame
from tests.tests_frame import (
    test_request_frame_current_params,
    test_frame_checksum,
    test_request_frame_checksum,
)

test_isolate_frame()
test_request_frame_current_params()
test_frame_checksum()
test_request_frame_checksum()
