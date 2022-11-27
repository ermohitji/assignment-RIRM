import click


def print_output(results):
    socials = results["social"]
    if socials:
        click.echo("Social Links - ")
        for s in socials:
            click.echo(s)
        click.echo()

    emails = results["emails"]
    if emails:
        click.echo("Emails/s - ")
        for e in emails:
            click.echo(e)
        click.echo()

    phones = results["phones"]
    if emails:
        click.echo("Contacts - ")
        for p in phones:
            click.echo(p)
        click.echo()
