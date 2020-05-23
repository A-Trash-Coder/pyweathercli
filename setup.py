from setuptools import setup, find_packages
 
setup(
    name="pyweathercli",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={'pyweathercli': ['*.json']},
    install_requires=["click", "pyfiglet", "pyowm", "colorama"],
    entry_points={
        "console_scripts":["weather=pyweathercli.cli:weather"]
    }
)