class User:
    pass


def set_user(user):
    setattr(user, 'sum_market_value_total', '17767208483374.97')
    print(user.sum_market_value_total)


if __name__ == '__main__':
    the_user = User()
    setattr(the_user, 'name', 'Michael')
    set_user(the_user)
    print(the_user.sum_market_value_total)
