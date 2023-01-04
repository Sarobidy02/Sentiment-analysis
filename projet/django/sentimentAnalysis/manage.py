#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from nltk.stem import LancasterStemmer
from sklearn.feature_extraction.text import CountVectorizer

class StemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(StemmedCountVectorizer, self).build_analyzer()
        stemmer = LancasterStemmer()
        return lambda doc: ([stemmer.stem(w) for w in analyzer(doc)])

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sentimentAnalysis.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
