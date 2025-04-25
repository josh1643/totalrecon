from setuptools import setup, find_packages

setup(
    name="totalrecon",
    version="0.1.0",
    author="Joshua Wasserman",
    description="Passive recon extractor and AI summarizer for CTFs, red teams, and open-source recon tooling.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/josh1643/totalrecon",  
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "transformers>=4.25.1",
        "torch>=1.10.0",
        "requests>=2.28.0",
        "PyMuPDF>=1.22.0",  
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
)