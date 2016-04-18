from setuptools import setup

setup(name='rock_paper_scissors',
      version='0.1.0',
      packages=['rock_paper_scissors'],
      entry_points={
          'console_scripts': [
              'rock_paper_scissors = rock_paper_scissors.__main__:main'
          ]
      },
      )