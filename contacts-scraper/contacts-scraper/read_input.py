import click
import validators


@click.command()
@click.option('--input-url', prompt='Input URL')
def read_input_url(input_url):
    input_url = input_url.strip()
    valid = validators.url(input_url)
    if valid:
        return input_url
    else:
        click.echo("invalid url")
        quit()
