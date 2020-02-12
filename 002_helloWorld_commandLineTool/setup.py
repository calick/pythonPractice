from setuptools import setup

setup(
    name="helloWorld",
    version="0.0.0",
    install_requires=["pytest"],
    entry_points={
        "console_scripts": [
            "helloWorld = src.app:main"
        ]
    }    
)