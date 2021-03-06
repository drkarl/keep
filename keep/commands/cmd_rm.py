import click
from keep import cli, utils


@click.command('rm', short_help='Deletes a saved command.')
@cli.pass_context
def cli(ctx):
    """Deletes a saved command."""
    cmd = click.prompt('Command to remove')
    utils.remove_command(ctx, cmd)
