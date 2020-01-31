class Connection:
    def __init__(self):
        self.new_state(CloseConnectionState)

    def new_state(self, newstate):
        self._state = newstate

    def read(self):
        return self._state.read(self)

    def write(self, data):
        return self._state.write(self, data)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)


class ConnectionState:
    @staticmethod
    def read(conn):
        raise NotImplementedError

    @staticmethod
    def write(conn):
        raise NotImplementedError

    @staticmethod
    def open(conn):
        raise NotImplementedError

    @staticmethod
    def close(conn):
        raise NotImplementedError


class CloseConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')

    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not open')

    @staticmethod
    def open(conn):
        print('opening...')
        print('conn {!r:}'.format(conn))
        return conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError('Aleady close')


class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('reading...')
        print('conn {!r:}'.format(conn))

    @staticmethod
    def write(conn, data):
        print('writing...', data)
        print('conn {!r:}'.format(conn))

    @staticmethod
    def open(conn):
        raise RuntimeError('Aleady open')

    @staticmethod
    def close(conn):
        print('closing...')
        print('conn {!r:}'.format(conn))
        conn.new_state(CloseConnectionState)


c = Connection()
c.open()
print(c, c._state)
c.read()
c.write(2324)
c.close()
# c.close()
c.open()
# c.open()
c.close()

