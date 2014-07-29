from time import time

from bb.extjs.core import ext
from bb.extjs.session.interfaces import ISession
from bb.extjs.session.interfaces import IClientIdentification
from bb.extjs.session.interfaces import DEFAULT_EXPIRATION


class SessionData(dict):

    def __init__(self):
        self.reset_lastchanged()
    
    def reset_lastchanged(self):
        self.lastchanged = time()


ram = dict()
class RamSession(ext.Adapter):
    """ simple session thats store data unencrypted in ram. After shutdown
        the server all data will lost.
        For a persistent session class you properly should 
        inherit from this class.
    """
    ext.implements(ISession)
    ext.context(ext.IRequest)

    session_data_cls = SessionData

    def __init__(self, request):
        self.request = request

    def __setitem__(self, key, value):
        client = IClientIdentification(self.request)
        identification = client.identification()
        if identification is None:
            identification = client.apply()
        data = self.store().setdefault(identification, self.session_data_cls)
        data[key] = value
        data.lastchanged = time()
        self.refresh()

    def __getitem__(self, key):
        identification = IClientIdentification(self.request).identification()
        if identification is None or identification not in self.store():
            raise KeyError('user has no identification or data')
        return self.store()[identification]

    def __delitem__(self, key):
        identification = IClientIdentification(self.request).identification()
        if identification is None or identification not in self.store():
            raise KeyError('user has no identification or data')
        del self.store()[identification]

    def __contain__(self, key):
        identification = IClientIdentification(self.request).identification()
        if identification is None:
            return False
        if identification not in self.store():
            return False
        return key in self.store()[identification]

    def set_expiration_time(self, time):
        """ expiration time in second for session
        """

    def get_expiration_time(self):
        return DEFAULT_EXPIRATION

    def store(self):
        """ return a store in form of a dict
        """
        return ram

    def refresh(self):
        removes = list()
        for key, data in self.store().items():
            if data.lastchanged + self.get_expiration_time() < time():
                removes.append(key)
        for key in removes():
            del self.store()[key]
    