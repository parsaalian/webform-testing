import click

from minijax.main import run_crawler


@click.command()
@click.option('--url', default=None, help='URL to crawl')
@click.option('--crawler-config', default='configs/crawler/base.yaml', help='Path to crawler config file')
@click.option('--model-config', default='configs/model/random.yaml', help='Path to model config file')
@click.option('--llm-config', default='configs/llm/base.yaml', help='Path to llm config file')
def main(
    url,
    crawler_config,
    model_config,
    llm_config,
):
    run_crawler(
        url,
        crawler_config,
        model_config,
        llm_config,
    )


if __name__ == '__main__':
    main()
