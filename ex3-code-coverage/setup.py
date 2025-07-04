from setuptools import setup, find_packages

setup(
    name="python-workshop",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A workshop focused on improving a poorly designed Python module.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[], 
    python_requires=">=3.12",
)