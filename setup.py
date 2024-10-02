from setuptools import setup, find_packages

setup(
    name="perhitungan_jarak_koordinat",
    version="0.1.0",
    author="Kelompok 1 Algoritma & Pemrograman B",
    author_email="",
    description="Package untuk perhitungan jarak dan fungsi sistem koordinat geografis",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=[
        "geopy",  # library eksternal yang mungkin diperlukan
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
