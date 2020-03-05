# Pretty print as JSON the contents of the clipboard

### Installing to the pyenv 'tools3'

**Installation**

`pip install .`


**Uninstalling**

`pip uninstall ppj`

**Usage**
ppj [-h]

Copy logs to the clipboard and type 'ppj' at the command line
Or pipe output to 'ppj'

**Development**

```
pyenv local tools3
pip install -e .
py.test -vs
```

**Testing**
```
py.test -v

py.test --cov-report html --cov ppjson.ppj
open htmlcov/index.html
```
