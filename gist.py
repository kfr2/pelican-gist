import re

from pelican import signals


def gist(content):
    """Converts [[ gist username:ID ]] in an article into its embedded <script> equivalent."""
    pattern = r'\[\[ gist (\w+):(\d+) \]\]'
    replacement = r'<script src="https://gist.github.com/\1/\2.js"></script>'
    content._content = re.sub(pattern, replacement, unicode(content._content))


def register():
    signals.content_object_init.connect(gist)
