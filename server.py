import socket
import time


def get_time_shift(filename) -> int:
    with open(filename) as file:
        for line in file:
            return int(line)


def get_time() -> str:
    return time.ctime(time.time() + get_time_shift('conf'))


def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', 123))
    while True:
        conn, addr = sock.recvfrom(1024)
        sock.sendto(get_time().encode('utf-8'), addr)


if __name__ == '__main__':
    run()
