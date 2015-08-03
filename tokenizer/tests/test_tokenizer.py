from unittest import TestCase

import numpy as np
from tokenizer.tokenizer import TokenzierMixin


class TestTokenzierMixin(TestCase):

    def setUp(self):
        self.test_doc = """
        This's a sent tokenize test. this is sent two.
        this is this sent three? Sent 4 is here!
        """
        
        self.test_sent = "This's a word \ntokenize test.   \n"

        self.tokenizer = TokenzierMixin()

    def test_sent_tokenize(self):
        sents = self.tokenizer.sent_tokenize(self.test_doc)
        self.assertTrue(isinstance(sents, np.ndarray))
        self.assertEqual(sents.shape[0], 4)
        self.assertEqual(sents[0], "This's a sent tokenize test.")
        self.assertEqual(sents[1], "this is sent two.")
        self.assertEqual(sents[3], "Sent 4 is here!")

    def test_word_tokenize(self):
        words = self.tokenizer.word_tokenize(self.test_sent)
        self.assertTrue(isinstance(words, np.ndarray))
        self.assertEqual(words.shape[0], 7)
        self.assertEqual(words[0], "This")
        self.assertEqual(words[6], ".")

    def test_generate_phrases(self):
        pass

