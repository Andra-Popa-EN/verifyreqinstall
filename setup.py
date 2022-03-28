from setuptools import setup

setup(
    name="Project-A",
    install_requires = ["enum34"],
    extras_require={
        "PDF": ["ReportLab>=1.2", "RXP"],
    }
)