import logging
import pytest
import random

log = logging.getLogger(__name__)


def test_pass():
    """
    """
    log.info("Dummy passing test case")
    assert True


def test_fail():
    """
    """
    log.info("Dummy failing test case")
    assert False


@pytest.mark.parametrize(
    argnames=["test_param"],
    argvalues=[
        pytest.param(
            *["Variant-A"],
        ),
        pytest.param(
            *["Variant-B"],
        ),
        pytest.param(
            *["Variant-C"],
        ),
        pytest.param(
            *["Variant-D"],
        ),
    ],
)
def test_random_parametrized(test_param):
    """
    """
    r = random.randint(0, 2)
    log.info(f"Dummy test case randomly failing: {test_param}, random number: {r}")
    assert r > 0