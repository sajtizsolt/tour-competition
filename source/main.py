from argumentparser import ArgumentParser

import sys

def main():
  argument_parser = ArgumentParser()
  argument_parser.verify_arguments(sys.argv)

if __name__ == '__main__':
  main()
