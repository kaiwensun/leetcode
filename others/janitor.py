#!/usr/bin/env python3

import shutil, os, sys

FORMAT = "%04d.%s"
FOLDER_SIZE = 500
seen_folders = set()

def clean_root_level_files():
    dryrun = "--dry-run" in sys.argv
    others_path = os.path.dirname(os.path.realpath(__file__))
    root_path = os.path.dirname(others_path)
    fnames = (fname for fname in os.listdir(root_path)
        if os.path.isfile(os.path.join(root_path, fname)))
    moved_cnt = 0
    for fname in fnames:
        num_str, main_name = fname.split(".", 1)
        try:
            num = int(num_str)
        except:
            print("Unhandled: " + fname)
            continue

        if 0 < num <= 9999:
            folder_name_start = num // FOLDER_SIZE * FOLDER_SIZE + 1
            folder_name_end = num // FOLDER_SIZE * FOLDER_SIZE + FOLDER_SIZE
            folder_name = "%04d-%04d" % (folder_name_start, folder_name_end)
            full_folder_name = os.path.join(root_path, folder_name)
            if not folder_exists(full_folder_name):
                if not dryrun:
                    os.mkdir(full_folder_name)
                print("Created folder %s" % full_folder_name)
                seen_folders.add(full_folder_name)
            full_fname = os.path.join(root_path, fname)
            target_file_name = FORMAT % (num, main_name.strip())
            full_target_file_name = os.path.join(full_folder_name, target_file_name)
            if not dryrun:
                shutil.move(full_fname, full_target_file_name)
            moved_cnt += 1
        else:
            print("Unhandled: " + fname)
    print()
    print(f"Moved %d files" % moved_cnt)
    if (dryrun):
        print("This is dry-run")

def folder_exists(full_path):
    return full_path in seen_folders or os.path.isdir(full_path)


if __name__ == "__main__":
    clean_root_level_files()