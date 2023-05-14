from setuptools import setup, find_packages

setup(
    name="pdf-annotations-diff",
    version="0.1.0",
    description="A tool to compare PDF annotations",
    author="Sameer Ahuja",
    author_email="pdf-annotations-diff@sameerahuja.com",
    url="https://github.com/sam33r/pdf-annotations-diff",
    py_modules=["pdf-annotations-diff"],
    install_requires=[
        "PyMuPDF",
    ],
    entry_points={
        "console_scripts": [
            "pdf-annotations-diff=pdf-annotations-diff:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",  # choose the appropriate license
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
