import streamlit as st
import os
from typing import Any, Generator
from llama_index.llms.base import LLM, CompletionResponse
from groq import Groq as GroqClient

# ===============================================================
# C U S T O M   L L M   W R A P P E R   F O R   G R O Q
# This class is built specifically for the LlamaIndex v0.9.x API
# It REMOVES all the incorrect decorators and modern imports.
# ===============================================================

class CustomGroq(LLM):
    model: str = "mixtral-8x7b-32768"
    api_key: str

    @property
    def metadata(self) -> dict:
        """LLM metadata."""
        return {"model_name": self.model}

    def complete(self, prompt: str, **kwargs: Any) -> CompletionResponse:
        """Completion endpoint."""
        client = GroqClient(api_key=self.api_key)
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=self.model,
        )
        response_text = chat_completion.choices[0].message.content
        return CompletionResponse(text=response_text)

    def stream_complete(
        self, prompt: str, **kwargs: Any
    ) -> Generator[CompletionResponse, None, None]:
        """Streaming completion endpoint."""
        client = GroqClient(api_key=self.api_key)
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=self.model,
        )
        response_text = chat_completion.choices[0].message.content

        # Yield a single CompletionResponse inside a generator
        yield CompletionResponse(text=response_text)

# ===============================================================
# I N S T A N T I A T E   T H E   L L M
# ===============================================================

# Set your Groq API key from Streamlit secrets
os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_KEY", "")

# Use our custom Groq class as the builder LLM
BUILDER_LLM = CustomGroq(
    model="mixtral-8x7b-32768", api_key=os.environ.get("GROQ_API_KEY")
)
