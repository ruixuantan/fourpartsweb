from setuptools import setup

setup(
    name='fourpartsweb-CLI',
    version='v0.0.1',
    packages=['cli', 'cli.commands'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points="""
        [console_scripts]
        fourpartsweb=cli.cli:cli
    """,
)
