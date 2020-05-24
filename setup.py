from setuptools import setup, find_packages
 
with open("README.md", "r", encoding="utf8") as fh:
    long_desc = fh.read()

setup(
    name="pyweathercli",
    version="0.0.2",
    author="Gavyn Stanley",
    description="A cli using click for weather",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/A-Trash-Coder/pyweathercli",
    packages=find_packages(),
    include_package_data=True,
    package_data={'pyweathercli': ['*.json']},
    install_requires=["click", "pyfiglet", "pyowm", "colorama"],
    entry_points={
        "console_scripts":["weather=pyweathercli.cli:weather"]
    }
)