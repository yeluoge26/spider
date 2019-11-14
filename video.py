import os
import csv
import pandas as pd
from browser import Browser
import shutil
import requests
import subprocess


def youtube_dl(savedir, url):

    cmd = f'youtube-dl --output \'{savedir}/%(title)s.%(ext)s\' {url}'
    print(">>shell run:", cmd)
    # os.system(cmd)
    try:
        subprocess.call(cmd, shell=True, stdout=subprocess.DEVNULL)
    except Exception as err:
        print("failed to run {}".format(cmd))


def save_cover(img_url, fpath):
    try:
        response = requests.get(img_url, stream=True)
        to_file = os.path.join(fpath, 'cover.jpg')
        with open(to_file, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
    except Exception as err:
        print(err)


def save_detail(text, fpath):
    to_file = os.path.join(fpath, 'detail.txt')
    with open(to_file, 'w') as f:
        f.write(text)


def save_tag(text, fpath):
    to_file = os.path.join(fpath, 'tag.txt')
    with open(to_file, 'w') as f:
        f.write(text)


def check_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def check_is_downloaded(fpath):
    is_downloaded = False
    entries = os.listdir(fpath)
    # print(entries)
    for entry in entries:
        if os.path.splitext(entry)[-1] == '.mp4':
            is_downloaded = True
    return is_downloaded


def download_video(csvfile='output/page_index.csv'):
    browser = Browser()
    df = pd.read_csv(csvfile)
    for index, row in df.iterrows():

        dest_dir = os.path.join(row['vtype'], row['title'])
        dest_dir = os.path.join('output', dest_dir)
        check_dir(dest_dir)

        if check_is_downloaded(dest_dir):
            continue

        print(row['link'], row['cover'])

        # save cover
        save_cover(row['cover'], dest_dir)

        try:
            browser.open_url(row['link'])
            info = browser.get_info()
            print(info)
        except Exception as err:
            print(err)
            continue

        # save detail
        save_detail(info['desc'], dest_dir)

        # save tag
        save_tag(info['tags'], dest_dir)

        if info['mp4']:
            youtube_dl(dest_dir, info['mp4'])
        elif info['m3u8']:
            youtube_dl(dest_dir, info['m3u8'])
        else:
            print('Unable to fetch {}'.format(row['link']))


if __name__ == '__main__':
    download_video()
