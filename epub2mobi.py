#!/usr/bin/env python

import os

def epub2mobi(fromdir):
    """
    Convert .epub to .mobi.
    Requires ebook-convert from calibre (http://calibre-ebook.com).
    """

    converted_files = []
    for root, dirs, files in os.walk(fromdir):
        for filename in files:
            _, ext = os.path.splitext(filename)
            if ext == '.epub':
                epub_file_path = os.path.join(root, filename)
                mobi_file_path = epub_file_path.replace('.epub', '.mobi')
                if not os.path.exists(mobi_file_path):
                    print(f"🕒 Converting \"{epub_file_path}\" to \"{mobi_file_path}\" ...")
                    ret = os.system(f"ebook-convert \"{epub_file_path}\" \"{mobi_file_path}\"")
                    if (ret == 0):
                        converted_files.append(mobi_file_path)

    print("\nConverted files:")
    for converted_file in converted_files:
        print(converted_file)

if __name__ == '__main__':
    import sys
    fromdir = '.'
    if len(sys.argv) == 2:
        fromdir = sys.argv[1]

    epub2mobi(fromdir)