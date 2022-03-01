import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oCrypt0r",
    packages=["ocryptor"],
    version="1.0.6",
    author="therealOri",
    license="GPL-3.0",
    install_requires=[
        "pycryptodome==3.14.1",
    ],
    author_email="therealOri@duck.com",
    description="A minimalistic, simple AES encryption library written in python3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/therealOri/oCrypt0r",
)
