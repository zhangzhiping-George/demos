from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        attrlst = []
        for attr in attrs:
            attrlst.append(attr)
        print('<%s>' %tag)
        print('attrlst', attrlst)

    def handle_endtag(self, tag):
        print('</%s>' %tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' %tag)

    def handle_data(self, data):
        print(data.encode('utf-8'))

    def handle_comment(self, comment):
        print('<!--', comment, '-->')

    def handle_entityref(self, name):
        print('&%s' %name)

    def handle_charref(self, name):
        print('&#%s;' %name)

parser = MyHTMLParser()

parser.feed('''<html>
<head></head>
<body>
<!-- html comment content -->
<p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body>
</html>''')