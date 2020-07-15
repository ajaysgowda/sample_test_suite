"""
BMS SOC estimator unit tests
"""
import logging
from pytest import mark

@mark.soc_estimator
class SOCEstimatorTests:
    """
    BMS SOC estimator unit tests
    """
    class KalmanFilterTests:
        """
        All tests pertaining to the Kalman filter soc estimation algo
        """

        @staticmethod
        def test_kalman_soc_estimator():
            assert True

    class CoulombCountingTests:
        """
        All tests pertaining to the Coulomb counting soc estimation algo
        """

        @staticmethod
        def test_coulomb_counting_soc_estimator():
            assert True

    class BlendingFunctionTests:
        """
        All tests pertaining to the Hybrid soc estimation algo
        """

        @staticmethod
        def test_blended_soc_estimator():
            assert True
