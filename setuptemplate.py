import setuptools

_ver = "<PLACEHOLDER>"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Implug",
    version=_ver,
    author="NekoMimi",
    author_email="nekomimi@tilde.team",
    description="Python plugin system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NekoMimiOfficial/Implug",
    project_urls={
        "Bug Tracker": "https://github.com/NekoMimiOfficial/Implug/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache2 License",
        "Operating System :: OS Independent",
    ],
    package_dir={"./": "Implug/"},
    install_requires = [],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
