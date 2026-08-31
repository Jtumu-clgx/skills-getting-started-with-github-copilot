from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


_INITIAL_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset in-memory activities before every test for isolation."""
    app_module.activities.clear()
    app_module.activities.update(deepcopy(_INITIAL_ACTIVITIES))
    yield


@pytest.fixture
def client():
    return TestClient(app_module.app)
