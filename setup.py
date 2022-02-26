import setuptools

with open("requirements.txt") as fp:
    requirements = fp.read().splitlines()
with open("LICENSE") as fp:
    license = fp.read()
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oCrypt0r",
    version="0.1",
    author="therealOri",
    url="https://github.com/therealOri/oCrypt0r",
    license=license,
    install_requires=requirements,
    author_email="therealOri@duck.com",
    description="A minimalistic, simple AES encryption library written in python3.",
    long_description=long_description,
    long_description_content_type="text/markdown"
)
