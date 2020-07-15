"""
BMS fault handling unit tests
"""
from pytest import mark

@mark.bms
@mark.fault_handling
class FaultHandlingTests:
    """
    BMS fault handling unit tests
    """

    class IOFaultHandlingTests:
        """
        BMS IO Fault handling unit tests
        """

        @mark.pin_fault
        class PinFaultTests:
            """
            BMS Pin Fault handling unit tests
            """

            @staticmethod
            def test_pin_fault():
                assert True

        @mark.can_hs
        class CANHighSpeedFaultHandlingTests:
            """
            BMS CAN HS pin fault handling tests
            """

            @staticmethod
            def test_can_hs_fault_handling():
                assert True

        @mark.can_ms
        class CANMediumSpeedFaultHandlingTests:
            """
            BMS CAN HS pin fault handling tests
            """

            @staticmethod
            def test_can_ms_fault_handling():
                assert True

    @mark.soc_estimator
    class SOCEstimationFaultHandling:
        """
        BMS SOC estimation fault handling unit tests
        """


        @staticmethod
        def test_soc_estimator_fault_handling():
            assert True
