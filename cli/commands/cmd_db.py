import click

from fourpartsweb.app import create_app
from fourpartsweb.extensions import db


# Create an app context for db connection.
app = create_app()
db.app = app

@click.group()
def cli():
    pass


@click.command()
def init_db():
    """Initialises the database.
    """

    db.drop_all()
    db.create_all()
    click.echo("Database initialised.")

    return None


cli.add_command(init_db)
