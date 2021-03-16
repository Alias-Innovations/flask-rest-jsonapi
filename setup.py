from setuptools import setup, find_packages

__version__ = '1.0.1'

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="flask-rested-jsonapi",
    version=__version__,
    description='Flask extension to create REST web api according to JSONAPI 1.0 specification with Flask, Marshmallow \
                 and data provider of your choice (SQLAlchemy, MongoDB, ...)',
    long_description=long_description,
    url='https://github.com/Alias-Innovations/flask-rested-jsonapi',
    author='Alias Innovations Team',
    author_email='alias-team@aliasinnov.com',
    license='MIT',
    classifiers=[
        'Framework :: Flask',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='web api rest jsonapi flask sqlalchemy marshmallow',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    platforms='any',
    install_requires=[
        'six',
        'Flask',
        'marshmallow',
        'marshmallow_jsonapi',
        'sqlalchemy'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'dev': [
            'pytest',
            'coveralls',
            'coverage'
        ],
        'docs': 'sphinx'
    }
)
