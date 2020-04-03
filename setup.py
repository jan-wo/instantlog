from distutils.core import setup
setup(
  name = 'instantlog',        
  packages = ['instantlog'],   
  version = '0.1',      
  license='MIT',       
  description = 'Simple colorful logger info/waring/error; Screen and file logs',  
  author = 'Wojciech Jankiewicz',
  author_email = 'wojtekjankiewicz@gmail.com',
  url = 'https://github.com/jan-wo/instantlog',  
  download_url = 'https://github.com/jan-wo/instantlog/archive/v_01.tar.gz',#
  keywords = ['LOGGER', 'COLORS', 'INSTANT'],
  install_requires=[
          'colorama'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
)
