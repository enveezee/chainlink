from os import path
from setuptools import setup

setup(
    name='chainlink',
    version='0.1',
    description='python link handler',
    author='Katy Tolsen'
    url='https://salsa.debian.org/kbt-guest/chainlink',
    license='MIT',
    platforms='ALL',
    long_description=_read('README.md'),
    long_description_content_type='text/markdown',
    install_requires['newspaper3k','pyyaml'],
    py_modules['config'],
    scripts=['chainlink']
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: DFSG approved',
        'License :: OSI Approved :: MIT Liense',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
    ]
)

def _read(fn):

    fn = path.join(path.dirname(__file__), fn)

    with open(fn, "rb") as f:
        data = f.read()

    return data.decode("utf-8")