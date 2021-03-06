from zope import interface


DEFAULT_EXPIRATION = 15 * 60


class IClientIdentification(interface.Interface):

    def __init__(self, request):
        """ as param request that implement IRequest
        """

    def identification(self):
        """ return per user a unique id. E.g. Session id
            that was autogenerated. If no id was found return None.
        """

    def apply(self):
        """ set identification. eg as cookie
            return the new id
        """


class ISession(interface.Interface):

    def __init__(self, request):
        """ as param request that implement IRequest
        """

    def __setitem__(self, key, value):
        """ set data to corresponding user. If no session exist
            a session will be created.
        """

    def __getitem__(self, key):
        """ return data for a given user and key. Key error will
            raised if no key was found.
        """

    def __delitem__(self, key):
        """ remove items in users data
        """

    def __contain__(self, key):
        """ return True if a key was found for the actual user.
        """

    def set_expiration_time(self, time):
        """ expiration time in second for session
        """
