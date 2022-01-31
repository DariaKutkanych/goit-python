from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='clean_folder_030920',
    version='1.0.0',
    description='Folder sorting package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Daria Kutkanych',
    author_email='d.goubenko@gmail.com',
    license='MIT',
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src", exclude=['test']),
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.command_line:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
