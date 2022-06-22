# innoleaps
This repository contains modules for Python data structure processing.

This application is tested to run in Python 3.6.5.

## Sample module usage
```python
from src.modules.list_processor import ListProcessor


flattened_list = ListProcessor.flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Unit Test
```shell
pip install virtualenv
python -m virtualenv venv
source venv/bin/activate
pip install -r tests/requirements.txt
pytest --cov=. tests/
```