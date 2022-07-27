import sys
import re

def lex(characters, token_exprs):
	pos = 0
	tokens = []
	while pos < len(characters):
		match = None
		for token_expr in token_exprs:
			pattern, tag = token_expr
			regex = re.compile(pattern)
			match = regex.match(characters, pos)
			if match:
				text = match.group(0)
				if tag:
					token = (text, tag)
					tokens.append(token)
				break
		if not match:
			sys.stderr.write('Illegal character: %s\n' % characters[pos])
			sys.exit(1)
		else:
			pos = match.end(0)
	return tokens


RESERVED = 'RESERVED'
INT      = 'INT'
FLOAT    = 'FLOAT'
STR      = 'STR'
ID       = 'ID'
token_exprs = [(r'[ \n\t]+',              None),
               (r'#[^\n]*',               None),
               (r'\(',                    RESERVED),
               (r'\)',                    RESERVED),
               (r'\{',                    RESERVED),
               (r'\}',                    RESERVED),
               (r':',                     RESERVED),
               (r';',                     RESERVED),
               (r',',                     RESERVED),
               (r'\+',                    RESERVED),
               (r'-',                     RESERVED),
               (r'\*',                    RESERVED),
               (r'/',                     RESERVED),
               (r'<=',                    RESERVED),
               (r'<',                     RESERVED),
               (r'>=',                    RESERVED),
               (r'>',                     RESERVED),
               (r'==',                    RESERVED),
               (r'=',                     RESERVED),
               (r'!=',                    RESERVED),
               (r'если',                  RESERVED),
               (r'иначе',                 RESERVED),
               (r'пока',                  RESERVED),
               (r'ввод',                  RESERVED),
               (r'вывод',                 RESERVED),
               (r"'[^`]*?'",              STR),
               (r"[0-9]+\.[0-9]+",        FLOAT),
               (r'[0-9]+',                INT),
               (r'[A-Za-z][A-Za-z0-9_]*', ID)]


def imp_lex(characters):
    return lex(characters, token_exprs)

print(imp_lex(open('HelloWorld.txt').read()))
