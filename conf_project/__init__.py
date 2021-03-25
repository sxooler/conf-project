import os


def get_abs_path_from_source_root(datapath, source_path=__file__):
    return os.path.join(os.path.dirname(os.path.realpath(source_path)), datapath)
