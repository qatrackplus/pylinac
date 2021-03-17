from setuptools import find_packages, setup

__version__ = '2.5.0.0'


setup(
    name='pylinac-qatrackplus',
    version=__version__,
    packages=find_packages(),
    package_data={'pylinac': ['watcher_config.yml', 'files/*.png']},
    url='https://github.com/qatrackplus/pylinac',
    keywords="""medical physics AAPM TG142 quality assurance starshot cbct vmat dynalog starshot linac Varian Elekta
             trajectory log kv MV planar Leeds Las Vegas Standard Imaging PipsPro TG51""",
    author='James Kerns',
    author_email='jkerns100@gmail.com',
    description='A toolkit for performing TG-142 QA-related tasks on a linear accelerator',
    install_requires=[
        "numpy >= 1.16",
        "scipy >= 1.1",
        "pydicom >= 2.0",
        "matplotlib >= 2.0",
        "scikit-image >= 0.17",
        "Pillow >= 4.0",
        "tqdm >= 3.8",
        "reportlab >= 3.3",
        "argue",
        "py-linq",
    ],
    license='MIT',
    test_suite='test_basic',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries"]
)
