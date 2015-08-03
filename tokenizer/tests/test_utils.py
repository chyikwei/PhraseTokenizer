import numpy as np
from unittest import TestCase
from numpy.testing import assert_approx_equal

from tokenizer.utils import aggragate_by_cnt, get_entropy


class TestUtils(TestCase):

    def test_aggragate_by_cnt(self):
        random_ints = np.random.randint(1, 10, size=(200,))
        agg_cnts = aggragate_by_cnt(random_ints)

        for num, cnt in agg_cnts.iteritems():
            self.assertEqual(cnt, len(np.where(random_ints == num)[0]))

    def test_get_entropy_value(self):
        freqs = np.ones((2,))
        assert_approx_equal(get_entropy(freqs), 0.6931, 4)

        freqs = np.array([2, 1, 2])
        assert_approx_equal(get_entropy(freqs), 1.0549, 4)

    def test_get_entropy_random(self):
        random_freqs = np.random.randint(10, 100, size=(200,))
        random_int = np.random.randint(2, 10)
        entropy_1 = get_entropy(random_freqs)
        entropy_2 = get_entropy(random_freqs * random_int)
        assert_approx_equal(entropy_1, entropy_2)
