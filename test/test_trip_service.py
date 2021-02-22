# -*- coding: utf-8 -*-
import unittest

from app.trip_service import TripService
from exceptions import UserNotLoggedInException
from trip import Trip
from user import User


class TestGetTripsByUser(unittest.TestCase):
    GUEST_USER = None
    A_USER = User()
    ANOTHER_USER = User()

    def test_raise_exception_if_user_not_logged_in(self):
        trip_service = TestableTripService().with_user_being(self.GUEST_USER).with_second_user_being(self.A_USER)
        with self.assertRaises(UserNotLoggedInException):
            trip_service.get_trips_by_user(self.A_USER)

    def test_no_trips_returned_if_users_are_not_friends(self):
        trip_service = TestableTripService().with_user_being(self.A_USER)
        result = trip_service.get_trips_by_user(self.ANOTHER_USER)
        self.assertListEqual(result, [])


    def test_return_trips_if_users_are_friends(self):
        friend_one = User()
        friend_one.add_friend(self.A_USER)
        friend_one.add_trip(Trip())
        trip_service = TestableTripService().with_user_being(self.A_USER)
        result = trip_service.get_trips_by_user(friend_one)

        self.assertEquals(len(result), 1)


class TestableTripService(TripService):

    def _get_logged_user_from_session(self):
        return self.logged_in_user

    def _get_trips_of_user(self, user):
        return user.trips

    def with_user_being(self, user):
        self.logged_in_user = user
        return self

    def with_second_user_being(self, user):
        self.logged_in_user = user
        return self
