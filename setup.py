from setuptools import setup, find_packages

setup(
    name="mochi-api-client",  # Name of your package
    version="0.1.1",  # Initial release version
    author="Jorge Sequeira",  # Your name or your organization's name
    author_email="jsequeira03@gmail.com",  # Your contact email
    description="A Python client for interacting with the Mochi API.",  # A short description of the project
    long_description=open("README.md").read(),  # A long description from your README.md
    long_description_content_type="text/markdown",  # Specifies that the long description is in Markdown
    url="https://github.com/gsejas/mochi-api-client",  # Project home page or repository URL
    packages=find_packages(),  # Automatically find and include all packages in the project
    install_requires=[
        "requests",  # Add other dependencies as needed
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",  # Change as appropriate for your project's maturity
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",  # Specify your project's license
        "Programming Language :: Python :: 3",  # Specify the Python versions you support
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.6",  # Minimum version requirement of Python
)
