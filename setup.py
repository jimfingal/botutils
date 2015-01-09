from setuptools import setup

setup(name='botutils',
      version='0.1',
      description='A Collection of Twitter bot utilities',
      url='https://github.com/jimmytheleaf/botutils',
      author='Jim Fingal',
      author_email='jim@jimfingal.com',
      license='MIT',
      packages=['botutils'],
      include_package_data=True,
      install_requires=[
          'Pillow',
          'nltk',
          'tweepy',
          'requests'
      ],
      zip_safe=False)