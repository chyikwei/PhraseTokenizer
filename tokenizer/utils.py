import numpy as np
from collections import Counter


def aggragate_by_cnt(data_list):
    stats = Counter()
    for t in data_list:
        stats[t] += 1
    return stats


def get_entropy(freqs):
    total = freqs.sum()
    probs = freqs / float(total)
    log_probs = np.log(probs)
    entropy = -1. * np.dot(probs, log_probs)
    return entropy
