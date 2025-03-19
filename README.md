http://stackoverflow.com/questions/39528736/how-do-you-directly-run-a-python-script-that-is-inside-your-own-package

##### 1. Create `my_tool/__init__.py`.

##### 2. In the files directly under in my_tool: change the import statements to load the modules from the current package. So in my_tool.py change:

```python
import c
import d
import k
import s
```
to:

```python
from . import c
from . import d
from . import k
from . import s
```

You need to make a similar change to all your other files.

##### 3. In the files located in my_tool/tests: change the import statements that import the code you want to test to relative imports that load from one package up in the hierarchy. So in test_my_tool.py change:

```python
import my_tool
```

to:

```python
from .. import my_tool
```

Similarly for all the other test files.

##### 4. Run the module scripts directly

```bash
❯ python3 -m my_tool.my_tool
C!
D!
F!
V!
K!
T!
S!
my_tool!
my_tool main!
|main tool!||detected||tar edit!||installed||keys||LOL||ssl connect||parse ASN.1||config|

❯ python3 -m my_tool.c
C!
C main!
|config|
```
##### 5. Run tests

```bash
✦ ❯ pytest
============================== test session starts =============================
platform darwin -- Python 3.13.2, pytest-8.3.4, pluggy-1.5.0
collected 8 items

my_tool/tests/test_c.py .                                                 [ 12%]
my_tool/tests/test_d.py .                                                 [ 25%]
my_tool/tests/test_f.py .                                                 [ 37%]
my_tool/tests/test_k.py .                                                 [ 50%]
my_tool/tests/test_my_tool.py .                                           [ 62%]
my_tool/tests/test_s.py .                                                 [ 75%]
my_tool/tests/test_t.py .                                                 [ 87%]
my_tool/tests/test_v.py .                                                 [100%]

============================== 8 passed in 0.02s ===============================

```
