import click
import sys


def main():
    click.secho('''
  ___ _____ _   _ ___  ___
 / __|_   _| | | | _ \/ __| by ZALANDO
 \__ \ | | | |_| |  _/\__ \\
 |___/ |_|  \___/|_|  |___/

 STUPS - To Unleash Penguin Swarms
''', bold=True)
    click.secho(' Homepage:      ', nl=False)
    click.secho('https://stups.io', fg='blue', bold=True)
    click.secho(' Documentation: ', nl=False)
    click.secho('https://docs.stups.io', fg='blue', bold=True)
    click.secho(' GitHub Repos:  ', nl=False)
    click.secho('https://github.com/zalando-stups', fg='blue', bold=True)
    click.secho('')

    do_configure = len(sys.argv) > 1 and 'configure'.startswith(sys.argv[1])
    if do_configure or click.confirm('Do you want to configure the STUPS CLI tools now?', default=True):
        import stups_cli.config
        domain = None
        if len(sys.argv) > 2:
            domain = sys.argv[2]
        stups_cli.config.configure(domain)
