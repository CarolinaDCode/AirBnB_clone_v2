#!/usr/bin/python3
"""
Generates a .tgz archive from the contents
of the web_static folder of the AirBnB Clone repo
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """
    function that creates a compressed file
    """
    try:
        local("mkdir -p versions")
        date_create = datetime.now().strftime("%Y%m%d%H%M%S")
        directory = "versions/web_static_{}.tgz".format(date_create)
        zip_ok = local("tar -cvzf {} web_static".format(directory))
        return directory
    except Exception:
        return None