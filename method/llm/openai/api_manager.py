# from: https://github.com/Significant-Gravitas/Auto-GPT/tree/master/autogpt/llm
from __future__ import annotations

import os
import json
from dotenv import load_dotenv
from openai import OpenAI

from method.llm.openai.modelsinfo import COSTS
from method.logger import logger
from method.utils import Singleton


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class ApiManager(metaclass=Singleton):
    def __init__(self):
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_cost = 0
        self.total_budget = 0


    def reset(self):
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_cost = 0
        self.total_budget = 0.0


    def create_chat_completion(
        self,
        messages: list,  # type: ignore
        model: str | None = None,
        temperature: float = None,
        max_tokens: int | None = None,
        openai_api_key: str | None = None,
    ) -> str:
        """
        Create a chat completion and update the cost.
        Args:
        messages (list): The list of messages to send to the API.
        model (str): The model to use for the API call.
        temperature (float): The temperature to use for the API call.
        max_tokens (int): The maximum number of tokens for the API call.
        Returns:
        str: The AI's response.
        """
        logger.debug(f"Prompt: {json.dumps(messages, indent=2)}")
        
        response = client.chat.completions.create(model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens)
        logger.debug(f"Response: {response}")
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
        self.update_cost(prompt_tokens, completion_tokens, model)
        return response


    def create_text_completion(
        self,
        prompt: str,
        model: str | None = None,
        temperature: float = None,
        max_tokens: int | None = None,
        openai_api_key: str | None = None,
    ) -> str:
        """
        Create a text completion and update the cost.
        Args:
        prompt (str): The text completion prompt to send to the API.
        model (str): The model to use for the API call.
        temperature (float): The temperature to use for the API call.
        max_tokens (int): The maximum number of tokens for the API call.
        Returns:
        str: The AI's response.
        """
        logger.debug(f"Prompt: {prompt}")
        
        response = client.completions.create(model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens)
        logger.debug(f"Response: {response}")
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
        self.update_cost(prompt_tokens, completion_tokens, model)
        return response


    def update_cost(self, prompt_tokens, completion_tokens, model):
        """
        Update the total cost, prompt tokens, and completion tokens.

        Args:
        prompt_tokens (int): The number of tokens used in the prompt.
        completion_tokens (int): The number of tokens used in the completion.
        model (str): The model used for the API call.
        """
        self.total_prompt_tokens += prompt_tokens
        self.total_completion_tokens += completion_tokens
        self.total_cost += (
            prompt_tokens * COSTS[model]["prompt"]
            + completion_tokens * COSTS[model]["completion"]
        ) / 1000
        logger.debug(f"Total running cost: ${self.total_cost:.3f}")


    def set_total_budget(self, total_budget):
        """
        Sets the total user-defined budget for API calls.

        Args:
        total_budget (float): The total budget for API calls.
        """
        self.total_budget = total_budget


    def get_total_prompt_tokens(self):
        """
        Get the total number of prompt tokens.

        Returns:
        int: The total number of prompt tokens.
        """
        return self.total_prompt_tokens


    def get_total_completion_tokens(self):
        """
        Get the total number of completion tokens.

        Returns:
        int: The total number of completion tokens.
        """
        return self.total_completion_tokens


    def get_total_cost(self):
        """
        Get the total cost of API calls.

        Returns:
        float: The total cost of API calls.
        """
        return self.total_cost


    def get_total_budget(self):
        """
        Get the total user-defined budget for API calls.

        Returns:
        float: The total budget for API calls.
        """
        return self.total_budget
