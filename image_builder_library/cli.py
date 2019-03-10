# -*- coding: utf-8 -*-

"""Console script for image_builder_library."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for image_builder_library."""
    click.echo("Replace this message by putting your code into "
               "image_builder_library.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
