class Node:
    """Node of binary tree"""
    def __init__(self, name, email):
        self.name = name  # Fixed from 'value'
        self.email = email
        self.left = None
        self.right = None

    @property
    def first_name(self):
        """The first name of the contact"""
        # TODO: Implement this method
        pass

    @property
    def last_name(self):
        """The last name of the contact"""
        # TODO: Implement this method
        pass

    def __str__(self):
        """String representation of the contact"""
        return f"{self.last_name}, {self.first_name} | ({self.email})"

"""
Mock Contact Data for testing and development
"""
MOCK_CONTACTS = [
    ("Alice Smith", "alice.smith@email.com"),
    ("Bob Johnson", "bob.j@email.com"),
    ("Carol Wilson", "carol.w@email.com"),
    ("David Thompson", "david.t@email.com"),
    ("Amy Brown", "amy.brown@email.com"),
]