from sockets import IPAdress, SocketAddress

def test_create_IP():
    address = IPAdress('0.0.0.0')
    assert isinstance(address, IPAdress)

def test_valid_ip():
    address = IPAdress('0.0.0.0')
    assert address.is_valid()
    address = IPAdress('127.0.0.1')
    assert address.is_valid()
    
def test_invalid_IP():
    address = IPAdress('----')
    assert not address.is_valid()
    address = IPAdress('256.0.0.0')
    assert not address.is_valid()

def test_private_IP():
    address = IPAdress('10.10.10.10')
    assert address.is_private()
    address = IPAdress('192.168.10.10')
    assert address.is_private()

def test_public_IP():
    address = IPAdress('0.0.0.0')
    assert address.is_public()
    
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

def test_invalid_ip_in_socket_address():
    socket = SocketAddress('127.0.01:65535')
    assert socket.is_valid() is False
