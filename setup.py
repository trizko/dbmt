from setuptools import setup, find_packages

setup(
    name="pgmigrate",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "psycopg2-binary",
    ],
    entry_points={
        "console_scripts": [
            "pgmigrate=pgmigrate.pgmigrate:main",
        ],
    },
    author="Tony Rizko",
    author_email="tony@rizkocircle.com",
    description="A simple PostgreSQL migration tool.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/trizko/pgmigrate",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)