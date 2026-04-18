import os
import pytest

os.environ.setdefault("SITE_URL", "http://localhost:8000")


def pytest_configure(config):
    config.addinivalue_line("markers", "e2e: end-to-end tests with playwright")


@pytest.fixture(scope="session")
def screenshots_dir():
    from pathlib import Path
    return Path(__file__).resolve().parent / "screenshots"


@pytest.fixture(scope="session")
def browser_type_launch_options(browser_type_launch_options):
    options = {}
    if "headless" not in str(browser_type_launch_options):
        options["headless"] = True
    return options