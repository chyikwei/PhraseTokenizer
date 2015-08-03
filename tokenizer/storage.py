from abc import ABCMeta, abstractmethod
from collections import defaultdict
import array


class BaseTokenStats(object):
    """Abstract class that store word & phrase statistics
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_token_id(self, token):
        return NotImplemented

    @abstractmethod
    def set_token_stats(self, token, value):
        return NotImplemented

    @abstractmethod
    def increment_token(self, token, value):
        return NotImplemented

    @abstractmethod
    def get_token_stats(self, token):
        return NotImplemented


class DictTokenStats(BaseTokenStats):
    """DictTokenStats with python dictionary implementation"""

    def __init__(self, stats_type='i'):
        self.dictionary = defaultdict()
        # index starts from 1
        self.dictionary.default_factory = lambda: len(self.dictionary) + 1
        self.stats = array.array(stats_type)
        self.stats.append(0)

    def _token_exists(self, token_id):
        stats_array_size = len(self.stats)
        if stats_array_size > token_id:
            return True
        elif token_id == stats_array_size:
            return False
        else:
            err_msg = "dim mismatch: token id=%d, array size=%d" % (token_id, stats_array_size)
            raise ValueError(err_msg)

    def get_token_id(self, token):
        if token in self.dictionary:
            return self.dictionary[token]
        else:
            return None

    def set_token_stats(self, token, value):
        # TODO: check check value format
        token_id = self.dictionary[token]
        if self._token_exists(token_id):
            self.stats[token_id] = value
        else:
            self.stats.append(value)
        return token_id

    def increment_token(self, token, value=1):
        token_id = self.dictionary[token]
        if self._token_exists(token_id):
            self.stats[token_id] += value
        else:
            self.stats.append(value)
        return token_id

    def get_token_stats(self, token, default=None):
        if token in self.dictionary:
            return self.stats[self.dictionary[token]]
        else:
            return default
