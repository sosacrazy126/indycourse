"""
Utilities for slugification, stopwords, and text helpers.
"""

import re

STOPWORDS = {
    # Minimal English stopwords for keyword extraction
    "the", "and", "for", "are", "but", "not", "you", "with", "that", "this",
    "from", "your", "have", "all", "was", "can", "has", "get", "out", "use",
    "our", "will", "let", "now", "see", "how", "its", "too", "had", "his",
    "her", "him", "she", "they", "them", "got", "who", "why", "what", "when",
    "where", "which", "been", "did", "the", "was", "were", "if", "then", "than",
    "just", "into", "more", "about", "also", "any", "may", "must", "could",
    "would", "should", "such", "over", "after", "before", "like", "very", "each",
    "only", "much", "some", "most", "many", "other", "these", "those", "because",
    "while", "between", "within", "along", "during", "without", "under", "again",
    "always", "never", "every"
}

def slugify(text):
    """
    Convert text to a lowercase, hyphen-separated slug.
    Non-alphanumeric chars become hyphens. Collapse repeats. Strip leading/trailing hyphens.
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-")

def tokenize(text):
    """
    Tokenize text into lowercase words, stripping punctuation.
    """
    return re.findall(r"\b[a-zA-Z0-9]{4,}\b", text.lower())

def get_top_keywords(text, stopwords=STOPWORDS, topn=10):
    """
    Return top N frequent words >3 chars not in stopwords.
    """
    words = tokenize(text)
    freq = {}
    for w in words:
        if w not in stopwords:
            freq[w] = freq.get(w, 0) + 1
    return [w for w, _ in sorted(freq.items(), key=lambda x: (-x[1], x[0]))][:topn]