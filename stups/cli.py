import click


def main():
    click.secho('''
  ___ _____ _   _ ___  ___
 / __|_   _| | | | _ \/ __| by ZALANDO
 \__ \ | | | |_| |  _/\__ \\
 |___/ |_|  \___/|_|  |___/

 STUPS - To Unleash Penguin Swarms
''', bold=True)
    click.secho(' Homepage:      ', nl=False)
    click.secho('http://stups.io', fg='blue', bold=True)
    click.secho(' Documentation: ', nl=False)
    click.secho('http://docs.stups.io', fg='blue', bold=True)
    click.secho(' GitHub Repos:  ', nl=False)
    click.secho('https://github.com/zalando-stups', fg='blue', bold=True)
    click.secho('')

    if click.confirm('Do you want to configure the STUPS CLI tools now?', default=True):
        import stups_cli
        stups_cli.config.configure()
