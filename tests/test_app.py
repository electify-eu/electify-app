import os
import sys

import dotenv

dotenv.load_dotenv()
# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from streamlit.testing.v1 import AppTest

at = AppTest.from_file("App.py")
at.run()


def test_app_runs():
    assert not at.exception
