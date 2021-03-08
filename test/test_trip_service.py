# -*- coding: utf-8 -*-
import unittest
from unittest import mock

from app.trip_service import TripService
from exceptions import UserNotLoggedInException
from trip import Trip
from user import User


class TestGetTripsByUser(unittest.TestCase):
    GUEST_USER = None
    A_USER = User()
    ANOTHER_USER = User()

    @mock.patch.object(TripService, '_get_logged_user_from_session', side_effect=UserNotLoggedInException,  autospec=True)
    def test_raise_exception_if_user_not_logged_in(self, mock_get_user):
        trip_service = TripService()
        with self.assertRaises(UserNotLoggedInException):
            trip_service.get_trips_by_user(self.A_USER)
        mock_get_user.assert_called_once_with(trip_service)

    @mock.patch.object(TripService, '_get_logged_user_from_session', return_value=A_USER,  autospec=True)
    def test_no_trips_returned_if_users_are_not_friends(self, mock_get_user):
        trip_service = TripService()
        result = trip_service.get_trips_by_user(self.ANOTHER_USER)
        self.assertListEqual(result, [])
        mock_get_user.assert_called_once_with(trip_service)

    @mock.patch.object(TripService, '_get_trips_of_user', return_value=[Trip()], autospec=True)
    @mock.patch.object(TripService, '_get_logged_user_from_session', return_value=A_USER,  autospec=True)
    def test_return_trips_if_users_are_friends(self, mock_get_user, mock_get_trips_from_user):
        friend_one = User()
        friend_one.add_friend(self.A_USER)
        friend_one.add_trip(Trip())
        trip_service = TripService()
        result = trip_service.get_trips_by_user(friend_one)

        self.assertEquals(len(result), 1)
