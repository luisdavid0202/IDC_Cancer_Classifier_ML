from setuptools import find_packages, setup

setup(
    name='IDC_Cancer_Classifier',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'opencv-python',
        'tensorflow',
        'keras',
        'numpy'
    ],
)
