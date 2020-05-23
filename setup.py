from setuptools import setup, find_packages
 
setup(
    name="pyweathercli",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click", "pyfiglet", "pyowm", "colorama"],
    entry_points={
        "console_scripts":["weather=pyweathercli.cli:weather"]
    }
)