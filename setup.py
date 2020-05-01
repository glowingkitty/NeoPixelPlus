import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="neopixel_plus",  # Replace with your own username
    version="0.3.0",
    author="Marco",
    author_email=None,
    description="The NeoPixel library plus some extras, for example a testing mode - so you can see how your LEDs would behave directly in the terminal, without any extra hardware..",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcoEDU/NeoPixelPlus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'colr'
    ]
)
