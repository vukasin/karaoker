import youtube_dl.extractor
import youtube_dl
import os
import pathlib
import tempfile
import sys
import re
import multiprocessing
from tqdm import tqdm

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def clean_path(fname: str) -> str:
    fname = re.sub("/", "\\/", fname)
    fname = re.sub("\.", "\\.", fname)
    if os.path.normpath(fname) != fname:
        raise ValueError(fname)
    s = os.path.split(fname)
    if s != ("", fname):
        raise ValueError(fname)
    return fname


def process(url):
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    from spleeter.separator import Separator
    import logging

    logging.basicConfig(filename='spleeter.log', level=logging.INFO)
    tmpfile = tempfile.mktemp(suffix=".m4a", dir="tmp")

    try:
        sys.stdout = open("log.txt", "w")
        sys.stderr = open("err.txt", "w")

        ydl_opts = {"outtmpl": tmpfile,
                    "format": "m4a", "max_downloads": 1}

        print(tmpfile)
        fname = None
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            info = ydl.get_info_extractor("Youtube").extract(url)
            fname = clean_path(info["title"])
            # os.makedirs(info["title"])
            os.rename(tmpfile, fname + ".m4a")
            tmpfile = fname + ".m4a"
        separator = Separator("spleeter:2stems-16kHz")
        separator.separate_to_file(tmpfile, "output",
                                   codec="mp3",
                                   bitrate="196k")
        os.rename(tmpfile, os.path.join("output", fname, "complete.m4a"))
        os.rename(os.path.join("output", fname, "accompaniment.mp3"),
                  os.path.join("output", fname, fname + ".mp3"))

    finally:
        if os.path.exists(tmpfile):
            os.unlink(tmpfile)


def entrypoint():
    input_data = open(sys.argv[1]).readlines()
    base = os.path.expanduser(os.path.join("~", "Music", "karaoker"))
    tmpdir = os.path.join(base, "tmp")
    os.makedirs(base, exist_ok=True)
    os.makedirs(tmpdir, exist_ok=True)
    os.chdir(base)

    errors = open("errors.txt", "w")
    for url in tqdm(input_data):
        url = url.strip()
        if url:
            p = multiprocessing.Process(target=process, args=(url,))
            p.start()
            p.join()
            if p.exitcode != 0:
                errors.writelines([url])


if __name__ == "__main__":
    entrypoint()
