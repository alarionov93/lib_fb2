from bs4 import BeautifulSoup as BS
from PIL import Image
from io import BytesIO

import base64
import sys

# TODO: get all stuff without dividing fb2 file to html and binary
# TODO: and pass filename as a second arg
work_path = sys.argv[1] # e.g. /Users/sanya/Downloads

f = open('%s/binary_fb2.html')

soup = BS(f.read(), 'lxml')
imgs = soup.find_all('binary')

for i in imgs:
	img = Image.open(BytesIO(base64.b64decode(i.text)))
	i.attrs['id']
	img.save('%s/imgs/%s' % i.attrs['id'])

# <image l:href="#image0.jpg"/>
f1 = open('%s/fb2_as_html_test.html', 'r')
soup1 = BS(f1.read(), 'lxml')
imgs1 = soup1.find_all('image')
for i_file in imgs1:
	i_file.replaceWith('<img src="%s">' % i_file.attrs['l:href'].split('#')[1])
f_last = open('%s/fb2_as_html_test.html', 'w').write(str(soup1))

