# coding=utf-8

import os
from setuptools import setup, find_packages


def get_version():
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    import vasptools
    return vasptools.__version__


if __name__ == '__main__':
    test_files = [os.path.join('vasptools', 'test', filename)
                  for filename in os.listdir('vasptools/test')]
    print(test_files)
    setup(
        name='vasptools',
        version=get_version(),
        description=(
            'tool collection for parsing vasp inputs & outputs'
        ),
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        author='Sky Zhang',
        author_email='sky.atomse@gmail.com',
        maintainer='Sky Zhang',
        maintainer_email='sky.atomse@gmail.com',
        license='MIT License',
        packages=find_packages(),
        platforms=["Linux", "Darwin"],
        url='https://github.com/atomse/vasptools',
        python_requires='>=3',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Operating System :: MacOS',
            'Operating System :: POSIX',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: Implementation',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
        ],
        install_requires=open('requirements.txt').read().split(),
        entry_points={
            "console_scripts": [
                "vasptools=vasptools.cli:run_vasptools_cli",
            ],
        },
        extras_require={
            'docs': [
                'sphinx',
                'sphinxcontrib-programoutput',
                'sphinx_rtd_theme',
                'numpydoc',
            ],
            'tests': [
                'pytest>=4.0',
                'pytest-cov'
            ],
            'curate': [
                'graphviz'
            ],
        },
        include_package_data=True,
        package_data={'vasptools_test': test_files},
        zip_safe=False,
    )
