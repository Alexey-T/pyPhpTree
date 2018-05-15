'''
Function
  def get_headers(lines)
finds all classes/functions in PHP source code, and gives list of tuples:
  (line_index, header_level, header_text, kind)
Fields:
  - line_index: 0-based index of header in the list of source code lines.
  - header_level: 1-based level of header: each item of level K+1 
    is sub-item if nearest higher item of level K.
  - header_text: caption of header, ie name of a class or function.
  - kind: kind of header item: "c" for class, "f" for function.

Author: Alexey Torgashin, UVviewsoft.com
License: MPL 2.0
'''

