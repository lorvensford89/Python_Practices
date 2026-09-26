# This is a simple program:
# TOD0: Bytes to Bits


def main():
    bytes = 100
    bits = Mbps_to_MB_per_second(bytes)
    print(f"{bytes} Mbps is equal to {bits} MB/s")

def Mbps_to_MB_per_second(bytes):
    return bytes / 8

if __name__ == "__main__":
    main()
