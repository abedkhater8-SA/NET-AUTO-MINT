import argparse
import os

import yaml
from netmiko import ConnectHandler


def load_change(change_type):
    file_path = f"configs/{change_type}.yml"

    with open(file_path, encoding="utf-8") as file:
        return yaml.safe_load(file)


def connect_to_device(device):
    return ConnectHandler(
        device_type=device["device_type"],
        host=device["host"],
        username=os.environ["DEVICE_USERNAME"],
        password=os.environ["DEVICE_PASSWORD"],
        secret=os.environ["DEVICE_SECRET"],
    )


def deploy_change(change):
    for device in change["devices"]:
        print(f"Connecting to {device['host']}...")

        connection = connect_to_device(device)
        connection.enable()

        output = connection.send_config_set(device["commands"])

        print(output)

        connection.save_config()
        connection.disconnect()


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--change",
        required=True,
        help="Change definition to deploy",
    )

    args = parser.parse_args()

    change = load_change(args.change)

    deploy_change(change)


if __name__ == "__main__":
    main()