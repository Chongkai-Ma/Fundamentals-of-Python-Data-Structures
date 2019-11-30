#!/usr/bin/python3

class Node(object):
    """Represent a singly linked node."""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next
