from setuptools import setup, find_packages

setup(
    name='manajemen_keuangan_pribadi',
    version='0.1',
    packages=find_packages(),
    install_requires=['pandas', 'matplotlib'],
    author='Nama Tim',
    description='Library untuk mengelola keuangan pribadi',
    url='',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
