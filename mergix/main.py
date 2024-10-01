from .mergix import mergix
from .args import parse_arguments

def main():
    args = parse_arguments()
    mergix(args)

if __name__ == "__main__":
    main()
