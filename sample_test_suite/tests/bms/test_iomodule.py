"""
.. module:: BMSIOmodule
.. moduleauthor:: Ajay Gowda
"""
import time
from pytest import mark


@mark.ioModule
@mark.bms
class BMSioModuleTests:
    """
       **BMS IO TESTS**
    """
    @mark.can_hs
    class CANHighSpeedTests:
        """
           **BMS CAN HS TESTS**
            Markers:
                1. ioModule
                2. bms
                3. can_hs
        """
        @staticmethod
        def test_can_hs_build():
            """
               **CAN HS PACKET BUILD TEST**
                .. note::
                     This is a mock test that  waits for n seconds before asserting true
            """
            time.sleep(.5)
            assert True


        @staticmethod
        def test_can_hs_parse():
            """
               **CAN HS PACKET PARSE TEST**
                .. note::
                     This is a mock test that  waits for n seconds before asserting true
            """
            time.sleep(.5)
            assert True

        @staticmethod
        def test_can_hs_receive():
            """
               **CAN HS PACKET RECEIVE TEST**
                .. note::
                     This is a mock test that  waits for n seconds before asserting true
            """
            time.sleep(.5)
            assert True

        @staticmethod
        def test_can_hs_transmit():
            """
               **CAN HS PACKET TRANSMIT TEST**
                .. note::
                     This is a mock test that  waits for n seconds before asserting true
            """
            time.sleep(.5)
            assert True

    @mark.can_ms
    class CANMediumSpeedTests:
        """
        CAN MS CAN tests
        """

        @staticmethod
        def test_can_ms_build():
            time.sleep(1)
            assert True

        @staticmethod
        def test_can_ms_parse():
            time.sleep(1)
            assert True

        @staticmethod
        def test_can_ms_receive():
            time.sleep(1)
            assert True

        @staticmethod
        def test_can_ms_transmit():
            time.sleep(1)
            assert True

    @mark.sensors
    class SensorTests:
        """
        Sensor tests
        """
        @mark.volt_sens
        class VoltageSensorTests:
            """
            All test pertaining to voltage sensing
            """

            @mark.signal_conditioning
            class SignalConditioningTests:
                """
                All test pertaining to the signal conditioning
                """

                @staticmethod
                def test_volt_sens_signal_conditioning():
                    time.sleep(1)
                    assert True

            @mark.fault_detection
            class FaultDetectionTests:
                """
                All test pertaining to the fault detection of the voltage sensor
                """

                @staticmethod
                def test_volt_sens_pin_fault_detection():
                    time.sleep(1)
                    assert True

        @mark.cur_sens
        class CurrentSensorTests:
            """
            All test pertaining to voltage sensing
            """

            @mark.signal_conditioning

            class SignalConditioningTests:
                """
                All test pertaining to the signal conditioning
                """

                @staticmethod
                @mark.skip(reason="testing functionality of mark skip")
                def test_cur_sens_signal_conditioning():
                    time.sleep(1)
                    assert False

            @mark.fault_detection
            class FaultDetectionTests:
                """
                All test pertaining to the fault detection of the current sensor
                """

                @staticmethod
                def test_cur_sens_pin_fault_detection():
                    time.sleep(1)
                    assert True

    @mark.actuators
    class ActuatorsTests:
        """
        All test pertaining to the Actuators
        """
        @mark.contactor
        class ContactorTests:
            """
            All test pertaining to contactors
            """

            class ActuationTests:
                """
                All tests pertaining to the actuation of the contactors
                """
                @staticmethod
                def test_contactor_actuation():
                    time.sleep(1)
                    assert True

        @mark.fault_detection
        class FaultDetectionTests:
            """
            All test pertaining to the fault detection of the contactors
            """

            @staticmethod
            def test_contactor_fault_detection():
                time.sleep(1)
                assert True

