from argparse import ArgumentParser


def set_parser():
    parser = ArgumentParser()
    parser.add_argument("fname", help="Name of the file")
    return parser


def get_parameters(parser):
    argv = parser.parse_args()
    fname = argv.fname
    print(fname)


if __name__ == "__main__":
    parser = set_parser()
    get_parameters(parser)
