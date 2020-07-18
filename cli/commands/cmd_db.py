import click

from fourpartsweb.app import create_app
from fourpartsweb.extensions import db


# Create an app context for db connection.
app = create_app()
db.app = app


def reset_db():
    db.drop_all()
    db.create_all()


@click.group()
def cli():
    pass


@click.command()
def init():
    """Initialises the database.
    """
    reset_db()
    click.echo("Database initialised")

    return None


cli.add_command(init)
