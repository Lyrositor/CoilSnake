import os
import tempfile

import mock


class CoilSnakeTestCase(object):
    TEST_DATA_DIR = os.environ['COILSNAKE_TEST_DATA_DIR']

    def setup_mock(self):
        self.mock = mock.Mock()

    def setup_temporary_wo_file(self):
        self.temporary_wo_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        self.temporary_wo_file_name = self.temporary_wo_file.name

    def teardown_temporary_wo_file(self):
        if not self.temporary_wo_file.closed:
            self.temporary_wo_file.close()
        os.remove(self.temporary_wo_file_name)