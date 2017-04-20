from setuptools import setup

with open('calysto_prolog/__init__.py', 'rb') as fid:
    for line in fid:
        line = line.decode('utf-8')
        if line.startswith('__version__'):
            __version__ = line.strip().split()[-1][1:-1]
            break

setup(name='calysto_prolog',
      version=__version__,
      description='A Prolog kernel for Jupyter that can use Python libraries',
      url="https://github.com/Calysto/calysto_prolog",
      author='Douglas Blank',
      author_email='doug.blank@gmail.com',
      packages=['calysto_prolog'],
      install_requires=["metakernel"],
      classifiers = [
          'Framework :: IPython',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 2',
      ]
)
