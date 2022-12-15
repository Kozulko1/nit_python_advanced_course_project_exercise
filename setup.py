from setuptools import setup, Extension


setup(
    name="user-manager",
    version="1.0",
    ext_modules=[Extension("hash_module", ["user_manager/c_extensions/hash/hash.c"])],
    packages=["user_manager", "user_manager/scripts"],
)
