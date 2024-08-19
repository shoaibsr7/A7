"""
A tool to generate performance reports for stock portfolios.
"""

from setuptools import setup, find_packages

setup(
    name="portfolio-report-generator",
    version="1.0.0",
    author="Your Name",
    author_email="ahmed.shoaib@dcmail.com",
    description="A tool to generate performance reports for stock portfolios",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "pylint",
        "certifi",
        "charset-normalizer",
        "idna",
        "requests",
        "requests-mock",
        "six",
        "urllib3",
        "yfinance",
    ],
    entry_points={
        'console_scripts': [
            'portfolio_report=portfolio.portfolio_report:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
