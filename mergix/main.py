from mergix import mergix
from .args import parse_arguments


if __name__ == "__main__":
    args = parse_arguments()
    mergix(args)
