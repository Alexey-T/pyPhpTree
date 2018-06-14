#
# pyPhpTree
# Author: Alexey Torgashin, UVviewsoft.com
# License: MPL 2.0
#

import string
CHARS = string.ascii_letters + string.digits + '_$'

DBG_TOKEN = 0
DBG_LEVEL = 0

TOKENS_LEN2 = (
    '<?', '?>', '/*', '*/', '//', '::',
    '==', '!=', '->', '=>', '<=', '>=',
    '--', '++', '||', '&&', '<<', '>>',
    '+=', '-=', '*=', '/=', '.=', '%=', '&=', '|=', '^=',
    )

TOKENS_LEN3 = (
    '<<<', '>>>',
    '===', '!==', '<<=', '>>=',
    )

KEYWORDS_NEED = (
    'function',
    'class',
    'namespace',
    'trait',
    )

ST_NONE = 0 # at usual tokens
ST_STR1 = 1 # inside 'string'
ST_STR2 = 2 # inside "string"
ST_CMT = 3  # inside /* comment */
ST_DOC = 4  # inside <<<TT heredoc TT;


def is_wordchar(ch):
    return ch in CHARS


def is_wordtoken(s):
    if not s:
        return False
    return is_wordchar(s[0])


def get_token(s, pos, state):
    '''
    gets token info (pos_after_token, str_token)
    '''
    r = pos
    if r>=len(s):
        return (r, '')
    ch = s[r]

    # inside strings - find only end of string
    if state==ST_STR1:
        while r<len(s):
            if s[r]=="'":
                return (r+1, "'")
            if s[r]=='\\':
                r += 2
            else:
                r += 1
        return (r, '##')

    if state==ST_STR2:
        while r<len(s):
            if s[r]=='"':
                return (r+1, '"')
            if s[r]=='\\':
                r += 2
            else:
                r += 1
        return (r, '##')

    # inside comment - find only comment end
    if state==ST_CMT:
        while r<len(s):
            if s[r:r+2]=='*/':
                return (r+2, '*/')
            r += 1
        return (r, '##')

    # space?
    if ch in ' \t':
        return (r+1, ' ')

    # word char?
    if is_wordchar(ch):
        # \ char can be in the middle of namespace name
        while r<len(s) and (is_wordchar(s[r]) or s[r]=='\\'):
            r += 1
        return (r, s[pos:r])

    # special operators
    if r+2<len(s):
        sub = s[r:r+3]
        if sub in TOKENS_LEN3:
            return (r+3, sub)

    if r+1<len(s):
        sub = s[r:r+2]
        if sub in TOKENS_LEN2:
            return (r+2, sub)

    # some unknown char
    return (r+1, ch)


def get_headers(filename, lines):
    '''
    gets dicts for class/function declarations
    '''

    in_php = False # for <?..?> tags
    in_state = ST_NONE
    in_doc_name = '' # name of heredoc

    level = 0 # increased by {, decreased by }
    _kind = None

    for line_index, s in enumerate(lines):
        pos = 0
        while pos<len(s):
            pos, token = get_token(s, pos, in_state)

            # skip spaces/tabs
            if token in ('', ' '):
                continue

            if DBG_TOKEN:
                print('get token: "'+token+'"')

            if in_state==ST_CMT:
                if token=='*/':
                    in_state = ST_NONE
                continue # ignore all until cmt end

            if in_state==ST_STR1:
                if token=="'":
                    in_state = ST_NONE
                continue # ignore all until str end

            if in_state==ST_STR2:
                if token=='"':
                    in_state = ST_NONE
                continue # ignore all until str end

            if in_state==ST_DOC:
                # end must be at line start
                if pos-len(token)==0 and token==in_doc_name:
                    pos, token = get_token(s, pos, in_state)
                    if token==';':
                        in_state = ST_NONE
                        in_doc_name = ''
                continue # ignore all until heredoc end

            # ignore non-PHP parts
            if token=='<?':
                in_php = True
                continue
            if token=='?>':
                in_php = False
                continue
            if not in_php:
                continue

            # consider comments
            if token=='//':
                # skip until EOL or until ?>
                pos = s.find('?>', pos)
                if pos<0: # until EOL
                    break
            if token=='/*':
                in_state = ST_CMT
                continue

            # consider strings
            if token=="'":
                in_state = ST_STR1
                continue
            if token=='"':
                in_state = ST_STR2
                continue

            # consider heredoc
            if token=='<<<':
                # analyze next 3 tokens
                pos, t1 = get_token(s, pos, in_state)
                pos, t2 = get_token(s, pos, in_state)
                pos, t3 = get_token(s, pos, in_state)

                if is_wordtoken(t1):
                    in_state = ST_DOC
                    in_doc_name = t1
                    continue
                if t1=="'" and is_wordtoken(t2) and t3=="'":
                    in_state = ST_DOC
                    in_doc_name = t2
                    continue
                if t1=='"' and is_wordtoken(t2) and t3=='"':
                    in_state = ST_DOC
                    in_doc_name = t2
                    continue

            # now we have OK php token
            if token=='{':
                _kind = None
                level += 1
                continue
            if token=='}':
                _kind = None
                if level>0:
                    level -= 1
                continue

            if DBG_LEVEL:
                print('    '*level+' (lev '+str(level)+') token "'+token+'"')

            if token in KEYWORDS_NEED:
                _kind = token
                continue

            if _kind:
                yield {
                    'line': line_index,
                    'level': level,
                    'name': token if is_wordtoken(token) else '',
                    'col': pos-len(token),
                    'kind': _kind,
                    }
                _kind = None

