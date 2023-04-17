# installers:
#   shells:
#       win32
#       darwin
#       arm


from setuptools import setup, find_packages

setup(
    name='altern8',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'numpy==1.20.3',
        'pandas==1.3.3',
        'matplotlib==3.4.3',
    ],
    entry_points={
        'console_scripts': [
            'altern8=altern8.__main__:main',
        ],
    },
)
