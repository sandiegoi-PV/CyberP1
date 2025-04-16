# goal: to use pythons socket module to attempt to connect a specific IP port
# If the connection is successful I'll know the port is open, if it fails or times out I'll know the port is closed or filtered
import socket


def scan_ports(target, start_port=1, end_port=1024):
    curr_port = start_port
    open_ports = []

    while curr_port != end_port:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # AF_INET = address family internet (IPV4)
        # SOCK_STREAM states that I will be using a stream-based connection like TCP
        sock.settimeout(1)
        # 1 second is the standard balance for deciding to move onto a different port.
        # For faster scans on local networks 0.2 - 0.5 is also reasonable

        result = sock.connect_ex((target, curr_port))
        if result == 0:
            print(curr_port)
            open_ports.append(curr_port)
        curr_port += 1

    sock.close()
    return open_ports


def main():
    target = input("Enter target IP or domain: ").strip()
    print(f"scanning ports 1-1024 for {target}")
    open_ports = scan_ports(target)
    if not open_ports:
        print("No open ports found :(")
    else:
        print(f"Open ports are {open_ports} :)")
    return


if __name__ == "__main__":
    main()