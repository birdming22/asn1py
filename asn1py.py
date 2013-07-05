"""
ASN.1 parser
"""

import tokenize

class Parser(object):

    def __init__(self, filename):
        self.filename = filename

    def parse_source(self):
        print 'parser source'
        f = open(self.filename, 'r')
        lines = f.read().splitlines()
        tokens = tokenize.generate_tokens(lines)

def testing():
    p = Parser('example/s1ap.10.6.0.asn')
    p.parse_source()

if __name__ == '__main__':
    testing()

