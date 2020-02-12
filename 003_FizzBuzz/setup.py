from setuptools import setup

setup(
    name="fizzbuzz",
    version="0.0.0",
    install_requires=["pytest"],
    entry_points={
        "console_scripts": [
            "fizzbuzz = src.app:main"
        ]
    }    
)