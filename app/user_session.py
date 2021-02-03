# -*- coding: utf-8 -*-
from exceptions import DependendClassCallDuringUnitTestException

class UserSession():

    @staticmethod
    def is_user_logged_in(user):
        raise DependendClassCallDuringUnitTestException(
            "UserSession.is_user_logged_in() should not be called in an unit test"
        )

    @staticmethod
    def get_logged_user():
        raise DependendClassCallDuringUnitTestException(
            "UserSession.get_logged_user() should not be called in an unit test"
    )
