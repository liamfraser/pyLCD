#!/usr/bin/env python
# Copyright (C) 2013 Julian Metzler
# See the LICENSE file for the full license.

from setuptools import setup, find_packages

setup(
        name = "pyLCD",
        version = "1.1.1",
        description = "A library for controlling LCDs on various hardware backends",
        license = "AGPLv3",
        author = "Julian Metzler",
        author_email = "contact@mezgrman.de",
        install_requires = ["wiringpi2", "PIL"],
        url = "https://github.com/Mezgrman/pyLCD",
        keywords = "library lcd display hd44780 ks0108 interface",
	packages = find_packages(),
)
