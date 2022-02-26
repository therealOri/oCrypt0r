import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oCrypt0r",
    packages=["ocryptor"],
    version="1.0.0",
    author="therealOri",
    license="GPL-3.0",
    install_requires=[
        "colorama==0.4.4",
        "halo==0.0.31",
        "log-symbols==0.0.14",
        "pycryptodome==3.14.1",
        "six==1.16.0",
        "spinners==0.0.24",
        "termcolor==1.1.0",
    ],
    author_email="therealOri@duck.com",
    description="A minimalistic, simple AES encryption library written in python3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/therealOri/oCrypt0r",
)
