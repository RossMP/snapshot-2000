from setuptools import setup

setup (
    name='snapshot-2000',
    version='0.1',
    author='Ross Prior',
    author_email='ross@gmail.com',
    description='snapshot-2000 is a tool to manage AWS EC2 snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url="https://github.com/RossMP/snapshot-2000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
