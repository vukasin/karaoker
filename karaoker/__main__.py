import youtube_dl.extractor
from spleeter.separator import Separator
import youtube_dl
import os
import pathlib
import tempfile
import sys
import re


def clean_path(fname: str) -> str:
    fname = re.sub("/", "\\/", fname)
    fname = re.sub("\.", "\\.", fname)
    if os.path.normpath(fname) != fname:
        raise ValueError(fname)
    s = os.path.split(fname)
    if s != ("", fname):
        raise ValueError(fname)
    return fname


def entrypoint():
    input_data = open(sys.argv[1]).readlines()
    base = os.path.expanduser(os.path.join("~", "Music", "karaoker"))
    tmpdir = os.path.join(base, "tmp")
    os.makedirs(base, exist_ok=True)
    os.makedirs(tmpdir, exist_ok=True)
    os.chdir(base)
    errors = open("errors.txt", "w")

    for url in input_data:
        tmpfile = tempfile.mktemp(suffix=".m4a", dir="tmp")
        try:
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
        except:
            errors.writelines([url])
        finally:
            if os.path.exists(tmpfile):
                os.unlink(tmpfile)


"""
"""
