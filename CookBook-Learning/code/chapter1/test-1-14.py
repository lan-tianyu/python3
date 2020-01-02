# class User:
#     def __init__(self, user_id):
#         self.user_id = user_id

#     def __repr__(self):
#         return 'User({})'.format(self.user_id)

# def sort_not_compare():
#     users = [User(23), User(3), User(99)]
#     print(users)
#     print(sorted(users, key=lambda u: u.user_id))

# sort_not_compare()

from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_not_compare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=attrgetter('user_id')))
    print(min(users, key=attrgetter('user_id')))
    print(max(users, key=attrgetter('user_id')))


sort_not_compare()