import argparse
from .Parser import parse_facebook
from .HtmlOutput import generate_html
from os import path


parser = argparse.ArgumentParser(description='Calculate word frequency of messages')
parser.add_argument('file', type=argparse.FileType('r', encoding='UTF-8'), help='File with messages to parse')
args = parser.parse_args()

participants = parse_facebook(args.file)

for name, participant in participants.items():
    participant.count_words()

html = generate_html(participants.values())

html_filename = path.basename(args.file.name).replace('.json', '.html')

with open(html_filename, 'w') as html_file:
    html_file.write(html)
