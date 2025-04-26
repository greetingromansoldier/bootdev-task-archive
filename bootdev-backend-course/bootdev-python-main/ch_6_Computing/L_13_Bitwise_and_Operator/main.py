# code before changes:

# can_create_guild = 0b1000
# can_review_guild = 0b0100
# can_delete_guild = 0b0010
# can_edit_guild = 0b0001


# def get_create_bits(user_permissions):
#     pass


# def get_review_bits(user_permissions):
#     pass


# def get_delete_bits(user_permissions):
#     pass


# def get_edit_bits(user_permissions):
#     pass

# task

# actual code:

can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
    user_permissions = user_permissions & can_create_guild
    return user_permissions


def get_review_bits(user_permissions):
    user_permissions = user_permissions & can_review_guild
    return user_permissions

def get_delete_bits(user_permissions):
    user_permissions = user_permissions & can_delete_guild
    return user_permissions

def get_edit_bits(user_permissions):
    user_permissions = user_permissions & can_edit_guild
    return user_permissions

