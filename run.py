import os
import argparse
import category
import page
import video

OUTPUT_DIR = 'output'


def check_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def cmd_parser():
    parser = argparse.ArgumentParser(description='spider')
    parser.add_argument('--index_category', action='store_true', help='get all category links')
    parser.add_argument('--index_page', action='store_true', help='crawl all videos links')
    parser.add_argument('--download_video', action='store_true', help='begin to download all videos to disk')
    args = parser.parse_args()
    return args


def main():
    check_dir(OUTPUT_DIR)
    args = cmd_parser()

    # get all category by website menubar
    if args.index_category:
        category.index_category()

    # get category all videos
    if args.index_page:
        page.index_page()

    # visit every video link and get details
    if args.download_video:
        video.download_video()


if __name__ == '__main__':
    main()
