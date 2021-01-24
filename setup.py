from setuptools import setup, find_packages

setup(
    name='a-discord-webhook',
    author='thiagola92',
    version='0.0.1',
    license='MIT',
    description='Just a discord webhook package',
    keywords=['discord', 'webhook'],
    url='https://github.com/thiagola92/a-discord-webhook',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
    ],
)