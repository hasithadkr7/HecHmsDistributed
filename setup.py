from setuptools import setup,find_packages

setup(
    name='HecHmsDistributed',
    version='1.0.0',
    packages=find_packages(),
    url='http://www.curwsl.org/',
    license='',
    author='hasitha',
    author_email='hasithadkr7@gmail.com',
    description='HecHms Distributed version',
    include_package_data=True,
    install_requires=['FLASK', 'Flask-Uploads', 'Flask-JSON', 'pandas','numpy'],
    zip_safe=False
)
