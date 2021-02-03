# -*- coding: utf-8 -*-

class User:
    def __init__(self):
        self.trips = []
        self.friends = []

    def add_friend(self, user):
        self.friends.append(user)

    def add_trip(self, trip):
        self.trips.append(trip)

    def get_friends(self):
        return self.friends
