import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="universal-parser",
    version="1.0.0",
    author="Ilya Matveyeu",
    author_email="ilyamatveev12902@gmail.com",
    description="Json | Pickle | Toml | Yaml Parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="git",
    project_urls={
        "Issues": "git/issues",
    },
    entry_points={
        "console_scripts": ["format_converter=universal_parser.main:main"],
    },
    packages=setuptools.find_packages(),
    install_requires=[
        "PyYAML>=5.4.1",
        "pytomlpp>=0.3.5",
    ],
    python_requires=">=3.6",
)
