from mopidy import MopidyException

class MpdAckError(MopidyException):
    """
    Available MPD error codes::

        ACK_ERROR_NOT_LIST = 1
        ACK_ERROR_ARG = 2
        ACK_ERROR_PASSWORD = 3
        ACK_ERROR_PERMISSION = 4
        ACK_ERROR_UNKNOWN = 5
        ACK_ERROR_NO_EXIST = 50
        ACK_ERROR_PLAYLIST_MAX = 51
        ACK_ERROR_SYSTEM = 52
        ACK_ERROR_PLAYLIST_LOAD = 53
        ACK_ERROR_UPDATE_ALREADY = 54
        ACK_ERROR_PLAYER_SYNC = 55
        ACK_ERROR_EXIST = 56
    """

    def __init__(self, message=u'', error_code=0, position=0, command=u''):
        self.message = message
        self.error_code = error_code
        self.position = position
        self.command = command

    def get_mpd_ack(self):
        """
        MPD error code format::

            ACK [%(error_code)i@%(position)i] {%(command)s} description
        """
        return u'ACK [%i@%i] {%s} %s' % (
            self.error_code, self.position, self.command, self.message)

class MpdUnknownCommand(MpdAckError):
    def __init__(self, *args, **kwargs):
        super(MpdUnknownCommand, self).__init__(*args, **kwargs)
        self.message = u'unknown command "%s"' % self.command
        self.command = u''
        self.error_code = 5 # ACK_ERROR_UNKNOWN

class MpdNotImplemented(MpdAckError):
    def __init__(self, *args, **kwargs):
        super(MpdNotImplemented, self).__init__(*args, **kwargs)
        self.message = u'Not implemented'
