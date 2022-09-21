import argparse

parser = argparse.ArgumentParser(
    description="This program prints the name of dogs."
)

parser.add_argument('-n', '--name', metavar='name', required=True, choices={'Kuro', 'Yuki'}, help='The name of the dog')

args = parser.parse_args()

print(args.name)