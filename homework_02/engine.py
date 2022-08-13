"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine:
    volume: float = None
    pistons: float = None
