from datetime import datetime
import os.path
import shutil


def make_reserver_arc(source: str, dest=None):
    if dest is None:
        dest = os.path.split(source)[0]
    name = os.path.basename(source)
    arc = shutil.make_archive(name, "zip", source)
    time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    shutil.move(arc, os.path.join(dest, f"{name}_{time}.zip"))


make_reserver_arc("files/4", "files/4")
