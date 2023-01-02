import os
from time import strftime, time

from touchtouch import touch


def get_timestamp(sep="_"):
    return (
        strftime(f"%Y{sep}%m{sep}%d{sep}%H{sep}%M{sep}%S")
        + f"{sep}"
        + (str(time()).split(".")[-1] + "0" * 10)[:6]
    )


def create_file_with_timestamp(
    folder=None, extension=".tmp", prefix="", suffix="", sep="_", create_file=False
):
    tsfile = get_timestamp(sep=sep)
    if folder is not None:
        tsfile = os.path.normpath(
            os.path.join(folder, f"{prefix}{tsfile}{suffix}{extension}")
        )
    else:
        tsfile = os.path.normpath(f"{prefix}{tsfile}{suffix}{extension}")
    if create_file:
        touch(tsfile)
    return tsfile


def create_folder_with_timestamp(
    folder, prefix="", suffix="", sep="_", create_folder=False
):
    tsfile = get_timestamp(sep=sep)
    tsfile = os.path.normpath(os.path.join(folder, f"{prefix}{tsfile}{suffix}"))
    if create_folder:
        if not os.path.exists(tsfile):
            os.makedirs(tsfile)
    return tsfile


