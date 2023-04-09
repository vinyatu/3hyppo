import pandas as pd
import numpy as np
from scipy import stats

chat_id = 5991293770

def solution(x, y) -> bool:
    pval = stats.ttest_ind(x, y).pvalue
    return pval < 0.01
