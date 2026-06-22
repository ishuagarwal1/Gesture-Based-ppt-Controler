from setuptools import setup, find_packages

setup(
    name="visionkit",
    version="0.1",
    packages=find_packages(),
    install_requires=["numpy", "pillow"],
    author="Paras Kaushik",
    description="A minimal CV library from scratch",
)
