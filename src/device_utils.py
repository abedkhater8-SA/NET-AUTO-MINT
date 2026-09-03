from netmiko import ConnectHandler


def get_device_status(device):
    try:
        connection = ConnectHandler(**device)
        connection.disconnect()
        return f"{device['host']} is reachable"

    except Exception:
        return f"{device['host']} is not reachable"