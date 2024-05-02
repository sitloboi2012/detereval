# -*- coding: utf-8 -*-
from __future__ import annotations

from abc import ABC, abstractmethod


class RelevancyMetrics(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def compute(self):
        pass
