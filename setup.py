from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="zycelium.ansiformat",
    version="0.1.1",
    description="ANSI Formatted Text for Terminals.",
    author="Harshad Sharma",
    author_email="harshad@sharma.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zycelium/python-ansiformat",
    project_urls={
        "Bug Tracker": "https://github.com/zycelium/python-ansiformat/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ],
    packages=['zycelium.ansiformat'],
    package_dir={"": "src"},
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
        "sty>=1.0.0rc1",
        "colour>=0.1.5",
    ],
    extras_require={
        "devel": [
            "bump2version>=1.0",
            "pytest>=6.2",
        ],
    },
)
