import argparse
import .Parser


parser = argparse.ArgumentParser(description='Calculate word frequency of messages')
parser.add_argument('file', type=argparse.FileType('r', encoding='UTF-8'), help='File with messages to parse')


