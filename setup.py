from setuptools import setup, find_packages

setup(
    name='twallery',
    version='0.0.2',
    description='',
    license='GPLv3',
    packages=find_packages(),
    author='patillacode',
    author_email='patillacode@gmail.com',
    url='https://github.com/patillacode/twallery',
    install_requires=['bumpversion>=0.5.3',
                      'Flask>=0.10.1',
                      'tweepy>=3.5.0',
                      'redis>=2.10.5'],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3',
        'Programming Language :: Python :: 2.7']
)
