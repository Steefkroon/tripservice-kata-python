# -*- coding: utf-8 -*-
from exceptions import UserNotLoggedInException
from user_session import UserSession
from trip import Trip


class TripService(object):

    def get_trips_by_user(self, user):
        logged_user = self._get_logged_user_from_session()
        if logged_user:
            if logged_user in user.get_friends():
                return self._get_trips_of_user(user)
            else:
                return []
        else:
            raise UserNotLoggedInException()

    def _get_trips_of_user(self, user):
        return Trip.find_trips_by_user(user)

    def _get_logged_user_from_session(self):
        return UserSession.get_logged_user()
