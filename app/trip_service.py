# -*- coding: utf-8 -*-
from exceptions import UserNotLoggedInException
from user_session import UserSession
from trip import Trip


class TripService(object):

    @staticmethod
    def get_trips_by_user(user):
        logged_user = UserSession.get_logged_user()
        if logged_user:
            if logged_user in user.get_friends():
                return Trip.find_trips_by_user(user)
            else:
                return []
        else:
            raise UserNotLoggedInException()
