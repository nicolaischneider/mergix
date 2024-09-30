from mergix import mergix
from args import parse_arguments


if __name__ == "__main__":
    args = parse_arguments()

#    if args.open:
#        print(f"Opening files with conflicts using command: {args.open}")
#    if args.info:
#        print("Showing detailed conflict information")

    mergix(args)