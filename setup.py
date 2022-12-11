import sys
import os
import pathlib


from setuptools import setup, Extension
from pathlib import Path


def collect_c_extensions():
      c_extensions_dir_path = Path(os.getcwd()) / Path("c_extensions")
      c_extensions = os.listdir()


setup(name='user-manager', version='1.0',
      ext_modules=[Extension('hash_module', ["user_manager/c_extensions/hash/hash.c"])],
      packages=["user_manager","user_manager/scripts"])



