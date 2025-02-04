import os
import sys

import dotenv
import pandas as pd
from streamlit.testing.v1 import AppTest

dotenv.load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


language_dictionary = pd.read_csv("streamlit_app/utils/language_dictionary.csv", delimiter=";")

language_dictionary = language_dictionary.set_index("key")["de"]


def test_streamlit_app():
    app = AppTest.from_file("App.py", default_timeout=30)
    # Run first example prompt
    app.run()

    # Assert whether there are no exception
    assert not app.exception

    # Click on the first example prompt button
    buttons = app.get("button")
    button_example_prompt_1 = [b for b in buttons if b.key == "example_prompt_1"][0]
    button_example_prompt_1.click().run()

    # Assert whether there are no exception
    assert not app.exception

    # Assert whether sources are there
    sources_labels = [src.label for src in app.get("expander") if "Quellen" in src.label]
    assert len(sources_labels) == 6
