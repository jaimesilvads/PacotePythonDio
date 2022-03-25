from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='pacotepypi',
    version='0.0.1',
    url='https://github.com/caiocarneloz/pacotepypi',
    license='MIT License',
    author='Jaime Silva',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='fjaimesilva@gmail.com',
    keywords='Pacote',
    description=u'Exemplo de pacote Calculadora',
    packages=['pacotepypi'],
    install_requires=['numpy'],)