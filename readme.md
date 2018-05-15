# pyPhpTree module

Module is a tiny parser of PHP source code, which finds lines with "class"/"function" declarations. It reads PHP code only inside `<? ... ?>` tags (any count of fragments in one file), and outside of `/* ... */` and `// ...` comments, and outside of single/double-quoted strings (multi-line strings supported, escape backslash supported).

# API

Function `get_headers(filename, lines)` finds all classes/functions, in given "lines" list, and gets tuples:

    (line_index, level, caption, kind)
    
It's generator (yield), so to get list of tuples, use `list(get_headers(...))`.
  
Fields:

- line_index: 0-based line index in the "lines" list.
- level: 0-based level of item. each item of level K+1 is nested into (nearest higher) item of level K.
- caption: name of class/function.
- kind: kind of item: "c" for class, "f" for function.

# About

- Author: Alexey Torgashin, UVviewsoft.com 
- License: Mozilla Public License 2.0 (MPL-2.0)
