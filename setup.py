# Copyright (c) 2010 The TracFacebookPlugins Project.
# See LICENSE.txt for details.

from setuptools import find_packages, setup

setup(
    name='TracFacebookPlugins',
    author='Thijs Triemstra',
    author_email='info@collab.nl',
    description='Support for Facebook plugins in Trac.',
    url='http://trac-hacks.org/wiki/TracFacebookPluginsMacro',
    license='MIT',
    version='0.1a1',
    packages=find_packages(exclude=['*.tests*']),
    entry_points = """
        [trac.plugins]
        facebookplugins = facebookplugins
    """,
)
