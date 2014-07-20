from pygments.lexer import RegexLexer
from pygments.token import *
import re

class CndLexer(RegexLexer):
    """
    For JCR Compact Namespace and Node Type Definition files.
    """

    name = 'Cnd'
    aliases = ['cnd']
    filenames = ['*.cnd']

    tokens = {
        'root': [
            (r'^<.*?>', Name.Namespace),
            (r'^//.*$', Comment),
            (r'/\*\*/', Comment.Multiline),
            (r'/\*.*?\*/', Comment.Multiline),
            (r'\[.*?\]', Name.Entity, 'nodetype'),
            (r'\((string|binary|long|double|date|boolean|name|path|reference|weakreference|uri|decimal)\)', Name.Label),
            (r'(\[|\(|\)|\])', Name.Tag),
            (r'^\+', Keyword.Declaration),
            (r'^\-', Keyword.Declaration),
            (r'(mandatory|autocreated|protected|version|primary)', Keyword),
            (r'(mixin|orderable)', Keyword),
            (r'(mandatory|autocreated|protected|multiple|version|primary)', Keyword),
            (r'(>|=|<|\*)', Operator),
            (r'\'.*?\'', String.Single),
            (r',', Punctuation),
            (r'\s+', Text),
            (r'[\w:]', Text),
        ],
        'nodetype': [
            (r'>', Name.Punctuation),
            (r'[\w:]', Name.Class),
            (r',', Punctuation),
            (r' ', Text),
        ]
    }
