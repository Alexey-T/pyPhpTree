# pyPhpTree
# Author: Alexey Torgashin, UVviewsoft.com
# License: MPL 2.0

import string
CHARS = string.ascii_letters + string.digits + '_$'

def is_wordchar(ch):
    return ch in CHARS

def get_token(s, pos):
    '''
    gets tuple (pos_after_token, str_token)
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
        if sub in ('/*', '*/', '<?', '?>', '=='):
            return (r+2, sub)
          
    # some unknown char
    return (r+1, ch)
    
        
def get_headers(lines):
    
    in_php = False
    in_cmt = False
    level = 0

    for index, s in enumerate(lines):
        pos = 0
        while pos<len(s):
            pos, token = get_token(s, pos)

            if token in ('', ' '):
                continue
                
            # comments must be ignored out of <? ?>
            if token=='<?':
                in_php = True
                continue
            if token=='?>':
                in_php = False
                continue
            if not in_php:
                continue
            
            # now we're inside <? ?>    
            if token=='/*':
                in_cmt = True
                continue
            if token=='*/':
                in_cmt = False
                continue
            if in_cmt:
                continue

            # now we have OK php token
            if token=='{':
                level += 1
                continue
            if token=='}':
                level -= 1
                if level<0:
                    level=0
                continue
                            
            print('    '*level+' (level='+str(level)+') token "'+token+'"')
