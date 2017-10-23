from socketIO_client import SocketIO, LoggingNamespace

with SocketIO('lampi-server', 3000, LoggingNamespace) as socketIO:
    socketIO.emit('Echo', {'test': 'data'})