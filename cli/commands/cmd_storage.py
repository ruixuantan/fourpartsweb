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

    midi_path = app.config['MIDISTORE_PATH']
    csv_path = app.config['RESULTSTORE_PATH']
    midi_files = os.listdir(midi_path) 
    csv_files = os.listdir(csv_path)

    for m in midi_files:
        os.remove(midi_path + m)
    
    for c in csv_files:
        os.remove(csv_path + c)

    click.echo("All files in storage deleted")

    if del_db:
        reset_db()
        click.echo("Database reset")

    return None


cli.add_command(del_storage)