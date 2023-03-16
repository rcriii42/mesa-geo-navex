"""run.py - Launch the server

Created by R. Ramsdell 2023-03-16
"""
import argparse

from server import server

parser = argparse.ArgumentParser(description='Show nav chart with various layers')
parser.add_argument('--layers',
                    help='Comma delimited list of layers to show (no spaces)')
parser.add_argument('--type',
                    help='The map type (Paper, ENC, Street)')

args = parser.parse_args()

server(layers=args.layers, chart_type=str.lower(args.type)).launch()
