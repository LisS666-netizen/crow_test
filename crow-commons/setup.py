from setuptools import setup


PACKAGE = "crow-commons"

classifiers = [
    'Development Status :: 1 - Development',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Topic :: Software Development :: Quality Assurance',
    'Topic :: Software Development :: Testing',
]

install_requires = [
    "attrs>=20.3.0",
    "pluggy>=0.13.1",
    "six>=1.15.0",
    "enum38;python_version<'3.8",
]


def main():
    setup(
        name=PACKAGE,
        use_scm_version={"root":"..", "relative_to": __file__},
        setup_requires=['setuptools_scm'],
        description="Common module for integrate with python-based framewoks",
        url="https://github.com/LisS666-netizen/crow_test",
        author="TestCompanyTeam, Test Author",
        author_email="test_author@gmail.com",
        packages=['crow_commons'],
        package_dir={"crow_commons": 'src'},
        install_requires=install_requires,
        py_modules=['crow_commons']
    )

if __name__ == '__main__':
    main()