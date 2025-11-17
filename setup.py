from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="lineament_detector",
    version="1.0.0",
    description="A Python library for geological lineament detection in images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sergey-K21/Lineament-Detector.git",
    author="Sergey Kostin",
    author_email="kostin.ss@phystech.edu",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Scientific/Engineering :: Geology",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="geology, lineament, detection, image-processing, remote-sensing",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    install_requires=[
        "opencv-python>=4.5.0",
        "numpy>=1.21.0",
        "matplotlib>=3.5.0",
    ],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0"],
    },
    project_urls={
        "Bug Reports": "https://github.com/Sergey-K21/Lineament-Detector.git/issues",
        "Source": "https://github.com/Sergey-K21/Lineament-Detector.git",
    },
)
