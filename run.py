import argparse
import sys
import os


parser = argparse.ArgumentParser()
parser.add_argument('--server', action='store_true')
parser.add_argument('--client', action='store_true')
parser.add_argument('--populate', action='store_true')
args = parser.parse_args()

if args.server:
    os.system("python -m app.server.server")
elif args.client:
    os.system("python -m app.client.client")
elif args.populate:
    os.system("python -m app.database.populate")
else:
    print("Uso: run.py [--server | --client | --populate]")
