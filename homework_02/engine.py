"""
create dataclass `Engine`
"""

from dataclasses import dataclass


@dataclass
class Engine:
    volume: float # Объём двигателя
    pistons: int # Кол-во поршней (цилиндров)
