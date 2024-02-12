#! /usr/bin/env python3

#######################################################
#
#  Netzint GmbH 2024
#  lukas.spitznagel@netzint.de
#  https://github.com/hermanntoast
#
#######################################################

import argparse
import base64

from cryptography.fernet import Fernet

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--secret-key", required=False, help="The secret key to decrypt password later. If not set, machine-id is used!", dest="secretkey")
    parser.add_argument("--password", required=True, help="The password you want to decrypt")
    args = parser.parse_args()

    if args.secretkey:
        crypt = Fernet(base64.urlsafe_b64encode(args.secretkey.encode()))
        password = crypt.encrypt(args.password.encode()).decode()
    else:
        with open("/etc/machine-id", "r") as f:
            crypt = Fernet(base64.urlsafe_b64encode(f.read().replace("\n", "").encode()))
            password = crypt.encrypt(args.password.encode()).decode()

    print("########################################################")
    print("Your hashed password is:")
    print(password)
    print("########################################################")


if __name__ == "__main__":
    main()