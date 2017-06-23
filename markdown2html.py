"""Provides a translate function that convert markdown syntax into HTML."""
import re
rules = (   (r'^([^#\*\d-].+$)',r'<p>\1</p>'),
            (r'_(.+)_',      r'<em>\1</em>'),
            (r'\*\*(.+)\*\*',r'<strong>\1</strong>'),
            (r'`(.+)`',      r'<code>\1</code>'))
line_rules =((r'((^\* .+$\n)+)',     r'<ul>\n\1</ul>'),
            (r'((^\d+\. .+$\n)+)',     r'<ol>\n\1</ol>'),
            (r'^\* (.+)',    r'\t<li>\1</li>'),
            (r'^\d+\. (.+)', r'\t<li>\1</li>'),
            (r'^###(.+)',    r'<h1>\1</h1>'), 
            (r'^##(.+)',     r'<h2>\1</h2>'),
            (r'^#(.+)',      r'<h3>\1</h3>'),
            (r'^---$',       r'<hr />'))
def translate(fn):
    file = open(fn)
    result = "<html>\n"
    for line in file:
        for pattern, repl in rules:
            line = re.sub(pattern, repl, line)
        result += line
    for pattern, repl in line_rules:
        result = re.sub(pattern, repl, result, flags = re.MULTILINE)

    result+= "\n</html>"
    return result

if __name__ == "__main__":
    for fn in sys.argv[1:]:
        print(translate(fn))
