from phpcr.sphinx.lexer_cnd import CndLexer

def setup(app):
    app.add_lexer('cnd', CndLexer())
