import array
import numpy as np
from collections import defaultdict, Counter
from scipy.sparse import csr_matrix
from nltk.tokenize import sent_tokenize
from nltk import word_tokenize
from .storage import DictTokenStats
from .utils import aggragate_by_cnt, get_entropy


class TokenzierMixin(object):
    """Common utitlity for tokenize text"""

    def _generate_text_array(self, text_list):
        return np.array(text_list, dtype=np.object)

    def word_tokenize(self, text, separator=None):
        """Split sentence into words

        By default this is a wrap of nltk "word_tokenize" function
        """
        if not separator:
            tokens = word_tokenize(text)
        elif callable(separator):
            tokens = separator(text)
        elif isinstance(separator, basestring):
            tokens = text.split(separator)
        else:
            raise ValueError("Invalid separator: %r" % separator)

        return self._generate_text_array(tokens)

    def sent_tokenize(self, text):
        """Split document into sentence

        By default this is a wrap of nltk "sent_tokenize" function
        """
        sent_list = [s.strip() for s in sent_tokenize(text)]
        return self._generate_text_array(sent_list)

    def sent_vectorize(sent, dictionary, update_stats=False):
        tokens = self.word_tokenize(sent)
        size = len(tokens)
        if update_stats:
            # with side-effect
            token_ids = [dictionary.increment_token(t) for t in tokens]
        else:
            token_ids = [dictionary.get_token_id(t) for t in tokens]
        return self._generate_text_array(tokens)


class PhraseMixin(object):
    """Find high frequency ngram tokens"""

    def get_row_idx(self, data, col_idx, token_id):
        return NotImplemented

    def find_ngrams(self, data, row_ids, dictionary, key, max_tokens, min_tf, side):

        col_idx = len(prev_token_ids) + 1
        if col_idx >= data.shape[1]:
            return

        data = data_mtrix[row_ids, :]
        csc_data = data.tocsc()

        tokens = csc_data[:, col_idx]
        token_stats = self._aggragate_by_cnt(tokens)
        entroy = self._get_entropy(token_stats.values())
        dictionary.set_entropy(key, side, value)

        for token_id, cnt in token_stats.iteritems():
            if cnt >= min_tf:
                next_row_ids = self._get_row_indices(csc_data, col_idx, token_id)
                next_key = dictionary.expend_key(key, token_id)
                self.find_ngrams(csc_data, next_row_ids, dictionary, new_key, max_tokens, min_tf, side)
    
    def generate_ngram(self, min_tf, token_ids, dictionary, max_tokens):
        valid_mask = [dictionary.get(t_id) >= min_tf for t_id in token_ids]
        n_col = len(max_tokens) + 1
        ngram_buffer = array.array('i')
        # start from 2 gram
        for start_idx in xrange(len(a)-2, 0, -1):
            n_grams = token_ids[start_idx: start_idx + n_col]


class PhraseTokenizer(TokenzierMixin, PhraseMixin):
    """Phrase tokenizer"""

    def __init__(self, max_phrase_tokens=5, min_tf=10, token_pattern=r'^[-A-Za-z]+$'):
        self.max_phrase_tokens = max_phrase_tokens
        self.min_tf = min_tf
        self.token_pattern_ = token_pattern
        self.stats_dict = DictTokenStats()

    def fit(self, X):
        return NotImplemented

    def transform(self, X):
        return NotImplemented
