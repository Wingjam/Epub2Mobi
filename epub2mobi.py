#!/usr/bin/env python

import os

def epub2mobi(from_dir):
    """
    Convert .epub to .mobi.
    Requires ebook-convert from calibre (http://calibre-ebook.com).
    """

    converted_files = []
    unconverted_files = []
    for root, dirs, files in os.walk(from_dir):
        for filename in files:
            _, ext = os.path.splitext(filename)
            if ext == '.epub':
                epub_file_path = os.path.join(root, filename)
                mobi_file_path = epub_file_path.replace('.epub', '.mobi')
                if not os.path.exists(mobi_file_path):
                    print(f"🕒 Converting \"{epub_file_path}\" to \"{mobi_file_path}\" ...")
                    ret = os.system(f"ebook-convert \"{epub_file_path}\" \"{mobi_file_path}\"")
                    if (ret == 0):
                        print(f"✅ Converted {epub_file_path.replace(from_dir, '')}")
                        converted_files.append(epub_file_path.replace(from_dir, ''))
                    else:
                        print(f"❌ Error converting {epub_file_path.replace(from_dir, '')}")
                        unconverted_files.append(epub_file_path.replace(from_dir, ''))

    print("")
    print("✅ Done")
    print("Converted files:", converted_files)
    print("Unconverted files:", unconverted_files)

if __name__ == '__main__':
    import sys
    from_dir = '.'
    if len(sys.argv) == 2:
        from_dir = sys.argv[1]

    epub2mobi(from_dir)