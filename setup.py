from setuptools import setup

setup(
    name='skeleton',
    version='0.0.1',
    description='Python package walking-skeleton',
    url='https://github.com/pmerlo/skeleton',
    author='pmerlo',
    author_email='',
    include_package_data=True,
    install_requires=[],
    license='',
    packages=[
        'skeleton'
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest',
        'pytest-cov'
    ],
    entry_points={
        'console_scripts': [
            'skeleton=skeleton.command_line:main'
        ]
    },
    zip_safe=False)

