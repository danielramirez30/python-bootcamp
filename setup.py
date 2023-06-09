from setuptools import find_packages, setup

__version__ = "0.1.0"

setup(
    name="web_utils_software",
    version=__version__,
    description="Python Project Package Template",
    author="Wilson Ramirez",
    author_email="wil_ramirez02@hotmail.com",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=["requests"],
    include_package_data=True,
    url="https://github.com/danielramirez30/python-project-template",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    # entry_points={
    #     "console_scripts": [
    #         "get-data=src.json_utils:get_json",
    #         "get-image=src.image_utils:get_image",
    #     ]
    # },
)
