from setuptools import setup, find_packages

setup(name='botutils',
      version='0.1',
      description='A Collection of Twitter bot utilities',
      url='https://github.com/jimmytheleaf/botutils',
      author='Jim Fingal',
      author_email='jim@jimfingal.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'Pillow',
          'nltk',
          'tweepy',
          'requests==2.4.3'
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'sure', 'unittest2'],
      zip_safe=False)