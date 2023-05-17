import click

from minijax.main import run_crawler


@click.command()
@click.option('--url', default=None, help='URL to crawl')
@click.option('--debug', default=False, help='Debug mode', is_flag=True)
@click.option('--crawler-config', default='configs/crawler/base.yaml', help='Path to crawler config file')
@click.option('--model-config', default='configs/model/random.yaml', help='Path to model config file')
def main(
    url,
    debug,
    crawler_config,
    model_config,
):
    run_crawler(
        url,
        debug,
        crawler_config,
        model_config,
    )


if __name__ == '__main__':
    main()
