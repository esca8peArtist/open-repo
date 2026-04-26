"""
Shared models used across AgentCore channel modules.

Re-exports ChannelMessage from base so that channel implementations
can import from a single well-known location:

    from agentcore.channels.models import ChannelMessage
"""

from .base import ChannelMessage

__all__ = ["ChannelMessage"]
