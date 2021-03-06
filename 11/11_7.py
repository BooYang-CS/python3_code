#解析Html
#python用HTMLParser来解析HTML
#-*- coding:utf-8 -*-
from html.parser import HTMLParser 
from html.entities import name2codepoint
class MyHTMLParser(HTMLParser):
	def handle_starttag(self,tag,attrs):
		print('<%s>' % tag)
	def handle_endtag(self,tag):
		print('</%s>' % tag)
	def handle_starendtag(self,tag,attrs):
		print('<%s/>' % tag)
	def handle_data(self,data):
		print(data)
	def handle_comment(self,data):
		print('<!--',data,'-->')
	def handle_entityref(self,name):
		print('&%s:' % name)
	def handle_charref(self,name):
		print('&#%s:' % name)
parser=MyHTMLParser()
parser.feed('''<html>
	<head></head>
	<meta charset='utf-8'>
	<body>
	<!--test html parser -->
	<p> some <a href=\"#\"> html</a>HTML&nbsp:tutorial...<br>END</p>
	</body>
	</html>''')