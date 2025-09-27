# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 04:04:47 2025

@author: FAZİLET
"""


import re
from collections import Counter
import matplotlib.pyplot as plt

# Örnek metin
text = """
Computational social sciences use data, text, and models to understand society.
This project is about text cleaning and word frequency analysis.
Text data can be messy, but Python makes it easier!
"""

# 1. Küçük harfe çevir
text = text.lower()

# 2. Noktalama işaretlerini temizle
text = re.sub(r'[^a-z\s]', '', text)

# 3. Kelimelere ayır
words = text.split()

# 4. En sık geçen kelimeleri bul
word_counts = Counter(words)
common_words = word_counts.most_common(10)

# 5. Sonuçları yazdır
print("Most common words:", common_words)

# 6. Görselleştir
plt.bar([w[0] for w in common_words], [w[1] for w in common_words])
plt.title("Word Frequency")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()
