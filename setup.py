import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="neopixel_plus",  # Replace with your own username
    version="1.3.1",
    author="Marco",
    author_email=None,
    description="The NeoPixel library plus animations and terminal testing mode - so you can see how your LEDs would behave directly in the terminal, without any microcontroller.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/glowingkitty/NeoPixelPlus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'colr',
        'rpi_ws281x',
        'adafruit-circuitpython-neopixel'
    ]
)
