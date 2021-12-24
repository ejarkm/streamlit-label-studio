from src.pages.home import Home
from src.pages.about import About
from src.pages.annotate import Annotate
from src.pages.upload import Upload
from src.pages.analysis import Analysis

PAGES = {
    "Home": Home,
    "About": About,
    "Upload": Upload,
    "Annotate": Annotate,
    "Analysis": Analysis,
}

__all__ = ["PAGES"]
