import os

import pytest

pytest.main()
os.system("allure generate ./results -o ./report --clean")
