# pyPhpTree module

Module for Python 3. Tiny parser of PHP source code, which finds lines with class/function/namespace/trait declarations. It reads PHP code only inside `<? ... ?>` tags (any count of fragments in one file), and outside of `/* ... */` and `// ...` comments, and outside of single/double-quoted strings (multi-line strings supported, escape backslash supported), and outside of heredoc/herenow blocks.

# API

Function `get_headers(filename, lines)` finds all classes/functions, in given "lines" list, and gets dicts:

    {
      'line': int,      # 0-based line index, where name found
      'col': int,       # 0-based position in line, where name found
      'level': int,     # 0-based level of item. each item of level K+1
                        # is nested into (nearest higher) item of level K
      'name': str,      # name of class/function
                        # empty str for anonymous funcs
      'kind': str,      # "class", "function", "namespace", "trait"
    }
    
It's generator (yield), so to get list, use `list(get_headers(...))`.

# About

- Author: Alexey Torgashin, UVviewsoft.com 
- License: Mozilla Public License 2.0 (MPL-2.0)
