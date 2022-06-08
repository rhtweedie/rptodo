"""This module provides the RP to-do model-controller"""
# rptodo/rptodo.py

from typing import Any, Dict, NamedTuple

class CurrentTodo(NamedTuple):
    todo: Dict[str, Any]
    error: int
