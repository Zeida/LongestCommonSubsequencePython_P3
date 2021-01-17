import unittest
import numpy as np
from ks_utils import *


class TestKSP(unittest.TestCase):

    def test_from_data_to_item(self):
        content = """3 10
                    45 5
                    48 8
                    35 3
                    """
        items, capacity = from_data_to_items(content)
        self.assertEqual(10, 10)
        return

