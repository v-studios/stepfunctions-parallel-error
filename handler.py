from random import randint


class UserError(Exception):
    pass


def error_system(event, context):
    print('ERROR SYSTEM')


def error_user(event, context):
    print('ERROR USER')


def json(event, context):
    if randint(1, 4) == 1:
        raise UserError('JSON USER')
    if randint(1, 4) == 1:
        raise SystemError('JSON SYSTEM')


def pdf(event, context):
    if randint(1, 4) == 1:
        raise UserError('PDF USER')
    if randint(1, 4) == 1:
        raise SystemError('PDF SYSTEM')
