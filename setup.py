"""
============================
Author:柠檬班-木森
Time:2020/7/16   16:20
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
from setuptools import setup, find_packages

with open("readme.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setup(
    name='unittest-ApiTestEngine',
    version='0.0.1',
    author='MuSen',
    author_email='musen_nmb@qq.com',
    url='https://github.com/musen123/unittest-ApiTestEngine',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["Faker==13.4.0",
                      "jsonpath==0.82",
                      "mysqlclient==1.3.14",
                      "requests-toolbelt==0.9.1",
                      "rsa==4.8"
                      ],
    packages=find_packages(),
    package_data={
        "": ["*.html",'*.md'],
    },
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
