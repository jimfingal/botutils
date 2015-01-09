from setuptools import setup

setup(name='pybottools',
      version='0.1',
      description='A Collection',
      url='http://github.com/storborg/funniest',
      author='Jim Fingal',
      author_email='jim@jimfingal.com',
      license='MIT',
      packages=['bottools'],
      include_package_data=True,
      install_requires=[
          'Pillow',
          'nltk',
          'tweepy',
          'requests'
      ],
      zip_safe=False)