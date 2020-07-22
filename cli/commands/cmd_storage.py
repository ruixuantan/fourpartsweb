import click
import os

from cli.commands.cmd_db import reset_db
from fourpartsweb.app import create_app


app = create_app()


@click.group()
def cli():
    pass


@click.command()
@click.option('--del-db', default=False, show_default=True,
              help="True if database is to be reset")
def del_storage(del_db):
    """Deletes all midi and csv files in storage.
    """

    store_path = app.config['STORE_PATH']
    for root, dirs, files in os.walk(store_path):
        for file in files:
            os.remove(os.path.join(root, file))

    click.echo("All files in storage deleted")

    if del_db:
        reset_db()
        click.echo("Database reset")

    return None


cli.add_command(del_storage)
