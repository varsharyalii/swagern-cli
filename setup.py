from setuptools import setup, find_packages

setup(
    name='swagern',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['swagern/templates/tavern_template_default.yaml'],
    },
    install_requires=[
        'click',
        'PyYAML',
        'jinja2==3.1.2',
        'requests==2.26.0',
        'Tavern==1.0.0',
        'fuzzywuzzy==0.18.0',
        'python-Levenshtein==0.12.2',
    ],
    entry_points='''
        [console_scripts]
        swagern=swagern.main:cli
    ''',
)
