#
# pyPhpTree
# Author: Alexey Torgashin, UVviewsoft.com
# License: MPL 2.0
#

import string
CHARS = string.ascii_letters + string.digits + '_$'


def is_wordchar(ch):
    return ch in CHARS


def get_token(s, pos):
    '''
    gets token info (pos_after_token, str_token)
    '''
    r = pos
    if r>=len(s):
        return (r, '')
    ch = s[r]

    # space?
    if ch in ' \t':
        return (r+1, ' ')

    # word char?
    if is_wordchar(ch):
        while r<len(s) and is_wordchar(s[r]):
            r += 1
        return (r, s[pos:r])

    # special symbols?
    if r+1<len(s):
        sub = s[r:r+2]
        if sub in ('<?', '?>', '/*', '*/', '//', '==') \
            or sub.startswith('\\'):
            # '\\' to support backslash escape in strings, must not be bad outside of str
            return (r+2, sub)

    # some unknown char
    return (r+1, ch)


def get_headers(filename, lines):
    '''
    gets list of tuples for classes/funcs:
    (line_index, level, caption, kind)
    '''

    in_php = False
    in_cmt = False
    in_str = False
    level = 0
    _kind = None

    for line_index, s in enumerate(lines):
        pos = 0
        while pos<len(s):
            pos, token = get_token(s, pos)

            # skip spaces/tabs
            if token in ('', ' '):
                continue

            if in_cmt:
                if token=='*/':
                    in_cmt = False
                continue # ignore all until cmt end

            if in_str:
                if token=="'":
                    in_str = False
                continue # ignore all until str end

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
                in_cmt = True
                continue

            # consider strings
            if token=="'":
                in_str = True
                continue

            # now we have OK php token
            if token=='{':
                level += 1
                continue
            if token=='}':
                if level>0:
                    level -= 1
                continue

            if token=='class':
                _kind = 'c'
                continue
            if token=='function':
                _kind = 'f'
                continue

            if _kind:
                yield line_index, level, token, _kind
                _kind = None

            # debug tokens
            #print('    '*level+' (lev '+str(level)+') token "'+token+'"')
