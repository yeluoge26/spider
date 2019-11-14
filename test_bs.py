from bs4 import BeautifulSoup
import requests

with open('downloads/Caribbeancom 110619-001 Aina Kiuchi My body drawn into pleasure.html', 'r') as f:
    html = f.read()

# #mv-info > div.mvi-content > div.mvic-desc > h3
title = BeautifulSoup(html, 'html.parser').select_one('div.mvic-desc > h3').text
# print(title)

desc = BeautifulSoup(html, 'html.parser').select_one('div.mvic-desc > div.desc').text
desc = desc.replace('by ,', '')
# print(desc)

tags_str = BeautifulSoup(html, 'html.parser').select_one('div.mvic-info > div.mvici-left > p').text
# print(tags_str)


# #media-player > div.jw-media.jw-reset > video
with open('downloads/Brazzers _ Hubby gets cheated on during Anniversary Photoshoot.html', 'r') as f:
    html = f.read()

with open('downloads/Caribbeancom 110619-001 Aina Kiuchi My body drawn into pleasure.html', 'r') as f:
    html = f.read()

mp4 = BeautifulSoup(html, 'html.parser').select_one('div.jw-media.jw-reset > video')
# print(mp4.attrs['src'])


source_url = 'http://javforme.me/movies/fc2-ppv-1195787-gonzo-po-with-active-ca-semen-cum-sex-spree-beauty-slender-cabin-crew-24-years-old-secretly-boyfriend'
req = requests.get(source_url)

mp4 = BeautifulSoup(html, 'html.parser').select_one('div.jw-media.jw-reset > video')
print(mp4.attrs['src'])
