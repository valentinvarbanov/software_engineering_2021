from sockets import SocketAddress


def test_socket():
    socket = SocketAddress('127.0.0.1:8080')
    assert isinstance(socket, SocketAddress)


def test_port():
    socket = SocketAddress('127.0.0.1:8080')
    assert socket.port == 8080


def test_invalid_socket():
     socket = SocketAddress('127.0.0.1:-1')
     assert socket.is_valid() is False


def test_valid_socket():
     socket = SocketAddress('127.0.0.1:65535')
     assert socket.is_valid() is True


def test_invalid_socket():
    socket1 = SocketAddress('127.0.0.1:')
    socket2 = SocketAddress('127.0.0.1')

    assert socket1.is_valid() is False
    assert socket2.is_valid() is False
