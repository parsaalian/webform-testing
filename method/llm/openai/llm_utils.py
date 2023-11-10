# from: https://github.com/Significant-Gravitas/Auto-GPT/tree/master/autogpt/llm
from __future__ import annotations

import os
import functools
import time
from dotenv import load_dotenv
from itertools import islice
from typing import List, Optional

import numpy as np
from openai import OpenAI
from openai import APIError, RateLimitError, Timeout

import tiktoken
from colorama import Fore, Style

from method.llm.openai.api_manager import ApiManager
from method.llm.openai.base import Message
from method.logger import logger

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def retry_openai_api(
    num_retries: int = 10,
    backoff_base: float = 2.0,
    warn_user: bool = True,
):
    """Retry an OpenAI API call.

    Args:
        num_retries int: Number of retries. Defaults to 10.
        backoff_base float: Base for exponential backoff. Defaults to 2.
        warn_user bool: Whether to warn the user. Defaults to True.
    """
    retry_limit_msg = f"{Fore.RED}Error: " f"Reached rate limit, passing...{Fore.RESET}"
    api_key_error_msg = (
        f"Please double check that you have setup a "
        f"{Fore.CYAN + Style.BRIGHT}PAID{Style.RESET_ALL} OpenAI API Account. You can "
        f"read more here: {Fore.CYAN}https://docs.agpt.co/setup/#getting-an-api-key{Fore.RESET}"
    )
    backoff_msg = (
        f"{Fore.RED}Error: API Bad gateway. Waiting {{backoff}} seconds...{Fore.RESET}"
    )

    def _wrapper(func):
        @functools.wraps(func)
        def _wrapped(*args, **kwargs):
            user_warned = not warn_user
            num_attempts = num_retries + 1  # +1 for the first attempt
            for attempt in range(1, num_attempts + 1):
                try:
                    return func(*args, **kwargs)

                except RateLimitError:
                    if attempt == num_attempts:
                        raise

                    logger.debug(retry_limit_msg)
                    if not user_warned:
                        logger.double_check(api_key_error_msg)
                        user_warned = True

                except APIError as e:
                    if (e.http_status != 502) or (attempt == num_attempts):
                        raise

                backoff = backoff_base ** (attempt + 2)
                logger.debug(backoff_msg.format(backoff=backoff))
                time.sleep(backoff)

        return _wrapped

    return _wrapper


def call_ai_function(
    function: str, args: list, description: str, model: str = 'gpt-4'
) -> str:
    """Call an AI function

    This is a magic function that can do anything with no-code. See
    https://github.com/Torantulino/AI-Functions for more info.

    Args:
        function (str): The function to call
        args (list): The arguments to pass to the function
        description (str): The description of the function
        model (str, optional): The model to use. Defaults to None.

    Returns:
        str: The response from the function
    """
    # For each arg, if any are None, convert to "None":
    args = [str(arg) if arg is not None else "None" for arg in args]
    # parse args to comma separated string
    args: str = ", ".join(args)
    messages: List[Message] = [
        {
            "role": "system",
            "content": f"You are now the following python function: ```# {description}"
            f"\n{function}```\n\nOnly respond with your `return` value.",
        },
        {"role": "user", "content": args},
    ]

    return create_chat_completion(model=model, messages=messages, temperature=0)


# Overly simple abstraction until we create something better
# simple retry mechanism when getting a rate error or a bad gateway
def create_chat_completion(
    messages: List[Message],  # type: ignore
    model: Optional[str] = None,
    temperature: float = None,
    max_tokens: Optional[int] = None,
) -> str:
    """Create a chat completion using the OpenAI API

    Args:
        messages (List[Message]): The messages to send to the chat completion
        model (str, optional): The model to use. Defaults to None.
        temperature (float, optional): The temperature to use. Defaults to 0.9.
        max_tokens (int, optional): The max tokens to use. Defaults to None.

    Returns:
        str: The response from the chat completion
    """

    num_retries = 10
    warned_user = False
    logger.debug(
        f"{Fore.GREEN}Creating chat completion with model {model}, temperature {temperature}, max_tokens {max_tokens}{Fore.RESET}"
    )
    api_manager = ApiManager()
    response = None
    for attempt in range(num_retries):
        backoff = 2 ** (attempt + 2)
        try:
            response = api_manager.create_chat_completion(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            break
        except RateLimitError:
            logger.debug(
                f"{Fore.RED}Error: ", f"Reached rate limit, passing...{Fore.RESET}"
            )
            if not warned_user:
                logger.warn(
                    f"Please double check that you have setup a {Fore.CYAN + Style.BRIGHT}PAID{Style.RESET_ALL} OpenAI API Account. "
                    + f"You can read more here: {Fore.CYAN}https://docs.agpt.co/setup/#getting-an-api-key{Fore.RESET}"
                )
                warned_user = True
        except (APIError, Timeout) as e:
            if e.http_status != 502:
                raise
            if attempt == num_retries - 1:
                raise
        logger.debug(
            f"{Fore.RED}Error: ",
            f"API Bad gateway. Waiting {backoff} seconds...{Fore.RESET}",
        )
        time.sleep(backoff)
    if response is None:
        logger.error(
            "FAILED TO GET RESPONSE FROM OPENAI",
            Fore.RED,
            "Auto-GPT has failed to get a response from OpenAI's services. "
            + f"Try running Auto-GPT again, and if the problem the persists try running it with `{Fore.CYAN}--debug{Fore.RESET}`.",
        )
        logger.warn()
        raise RuntimeError(f"Failed to get response after {num_retries} retries")
    resp = response.choices[0].message["content"]
    return resp


def batched(iterable, n):
    """Batch data into tuples of length n. The last batch may be shorter."""
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


def chunked_tokens(text, tokenizer_name, chunk_length):
    tokenizer = tiktoken.get_encoding(tokenizer_name)
    tokens = tokenizer.encode(text)
    chunks_iterator = batched(tokens, chunk_length)
    yield from chunks_iterator


def get_ada_embedding(text: str) -> List[float]:
    """Get an embedding from the ada model.

    Args:
        text (str): The text to embed.

    Returns:
        List[float]: The embedding.
    """
    model = 'text-embedding-ada-002'
    text = text.replace("\n", " ")

    kwargs = {"model": model}

    embedding = create_embedding(text, **kwargs)
    return embedding


@retry_openai_api()
def create_embedding(
    text: str,
    *_,
    **kwargs,
) -> openai.Embedding:
    """Create an embedding using the OpenAI API

    Args:
        text (str): The text to embed.
        kwargs: Other arguments to pass to the OpenAI API embedding creation call.

    Returns:
        openai.Embedding: The embedding object.
    """
    models_embedding = 'text-embedding-ada-002'
    models_tokenizer = 'cl100k_base'
    params_embedding_token_limit = 8191
    
    chunk_embeddings = []
    chunk_lengths = []
    for chunk in chunked_tokens(
        text,
        tokenizer_name=models_tokenizer,
        chunk_length=params_embedding_token_limit,
    ):
        embedding = client.embeddings.create(input=[chunk],
        # api_key=cfg.openai_api_key,
        **kwargs)
        api_manager = ApiManager()
        api_manager.update_cost(
            prompt_tokens=embedding.usage.prompt_tokens,
            completion_tokens=0,
            model=models_embedding,
        )
        chunk_embeddings.append(embedding["data"][0]["embedding"])
        chunk_lengths.append(len(chunk))

    # do weighted avg
    chunk_embeddings = np.average(chunk_embeddings, axis=0, weights=chunk_lengths)
    chunk_embeddings = chunk_embeddings / np.linalg.norm(
        chunk_embeddings
    )  # normalize the length to one
    chunk_embeddings = chunk_embeddings.tolist()
    return chunk_embeddings
