from setuptools import setup

setup(name='Odata',
      version='0.2',
      description='A random data generating tool for Odoo',
      url='http://github.com/Yenthe666/Odata',
      author='Yenthe Van Ginneken',
      author_email='yenthevg@gmail.com',
      license='BSD-3-Clause',
      packages=['Odata'],
      install_requires=['names','erppeek'],
      zip_safe=False)

# #so I don't have to keep looking it up: python setup.py sdist upload -r pypi
