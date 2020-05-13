# Packaging a python project


### A local project

```
root/
    animal_pkg/
        __init__.py
```

`__init__.py` initialises a package (tells Python this directory is a package). Simplest `__init__.py` can be an empty file.




### Create package files

```
root/
  animal_pkg/
    __init__.py
  tests/
  setup.py
  LICENSE
  README.md
```

| Item | Remark |
| --- | --- |
|`__init__.py` | Tells python `animal_pkg` is a package |
|`tests/` | A placeholder / folder for unit test files |
|`setup.py` | Build script for setuptools |



### setup.py

Add your username to the package name to ensure uniqueness.

```
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
```

[More details](https://packaging.python.org/guides/distributing-packages-using-setuptools/)



### README.md

```
# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.
```


### LICENSE

[ChooseALicense](https://choosealicense.com/)
Once you have chosen a license, open LICENSE and enter the license text. For example, if you had chosen the MIT license:

```
Copyright (c) 2018 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```



### Generating distribution archives

The next step is to generate distribution packages for the package. These are archives that are uploaded to the Package Index and can be installed by pip.

Install `setuptools` and `wheel`

```
python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
```


After this step the root folder will have a few more items:

```
root/
  animal_pkg/
    __init__.py
    ...
  animal_pkg_lyt.egg-info/
  build/
  dist/
    animal_pkg_lyt-*.whl      <- source archive
    animal_pkg_lyt-*.tar.gz   <- built distribution (*pip)
  tests/
  setup.py
  LICENSE
  README.md
```


### Uploading the distribution archives

Register with [test Pypi](https://test.pypi.org/account/register/) and retrieve your API token

Use twine to upload distribution packages (need to install twine)

```
python3 -m pip install --user --upgrade twine
```

Upload everything under `dist`:

```
python3 -m twine upload --repository testpypi dist/*
```




### Install your newly uploaded package

```
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps animal-pkg-lyt
```