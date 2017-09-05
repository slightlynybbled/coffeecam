import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'readme.rst')) as f:
    README = f.read()
exec(open(os.path.join(here, 'coffeecam/version.py')).read())

requires = [
    'flask',
    'picamera',
    'waitress'
]

setup(
    name='coffeecam',
    version=__version__,
    description='coffeecam',
    long_description=README,
    classifiers=[
      "Programming Language :: Python",
      "Framework :: Flask",
      "Topic :: Internet :: WWW/HTTP",
      "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='Jason R. Jones',
    author_email='slightlynybbled@gmail.com',
    url='https://github.com/slightlynybbled/coffeecam',
    keywords='web flask camera pi',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={'console_scripts': ['coffeecam = coffeecam.__main__:main']}
)
