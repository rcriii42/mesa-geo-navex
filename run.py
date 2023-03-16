"""run.py - Launch the server

Created by R. Ramsdell 2023-03-16
"""
import argparse

from server import server

parser = argparse.ArgumentParser(description='Show nav chart with various layers')
parser.add_argument('--layers',
                    default="1,2,3,5",
                    help='Comma delimited list of layers to show (no spaces)')
parser.add_argument('--type',
                    default="paper",
                    help='The map type (Paper, ENC)')

args = parser.parse_args()
print(f'{args.type} {args.layers}')

server(layers=args.layers, chart_type=str.lower(args.type)).launch()
