# -*- coding: utf-8 -*-
from exceptions import DependendClassCallDuringUnitTestException


class Trip:


    @staticmethod
    def find_trips_by_user(user):
        raise DependendClassCallDuringUnitTestException(
            "Trip should not be invoked on an unit test."
        )

