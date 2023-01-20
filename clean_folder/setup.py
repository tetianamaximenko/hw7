from setuptools import setup

setup(name='sort_your_folder',
      version='2022',
      description='Script will sort your useless folder',
      url='https://github.com/tetianamaximenko/hw6/blob/main/HW6.py',
      author='Tetianamaximenko',
      author_email='tetianamaximenko1994@gmail.com',
      license='MIT',
      packages=['clean_folder'])
      entry_points={'console_scripts':['foldsort = clean_folder.clean:main']}
)