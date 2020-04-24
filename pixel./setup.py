import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pixel", # Replace with your own username
    version="0.0.1",
    author="Install Xdaver",
    author_email="pixmicrox@gmail.com",
    description="This is The coding language for Pixmicro company.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/installX/Pixel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
