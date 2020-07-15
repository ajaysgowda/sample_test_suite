"""
BMS Health and Safety unit tests
"""
import time

from pytest import mark


@mark.bms
@mark.health
class BatHealthTests:
    """
    BMS battery Health unit tests
    """
    @staticmethod
    def test_heath():
        assert True


@mark.bms
@mark.safety
class BatSafetyTests:
    """
    BMS battery safety unit tests
    """
    # class BatLimitTest:
    #     @staticmethod
    #     @mark.bat_limit
    #     def test_bat_limit():




    @staticmethod
    @mark.xfail(reason="Test Fail")
    def test_safety():
        time.sleep(2)
        assert False
