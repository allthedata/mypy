# Stubs for functools (Python 2.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from abc import ABCMeta, abstractmethod
from typing import Any, Callable, Dict, Sequence
from collections import namedtuple

_AnyCallable = Callable[..., Any]

def reduce(function, iterable, initializer=None): ...

WRAPPER_ASSIGNMENTS = ... # type: Sequence[str]
WRAPPER_UPDATES = ... # type: Sequence[str]

def update_wrapper(wrapper: _AnyCallable, wrapped: _AnyCallable, assigned: Sequence[str] = ...,
                   updated: Sequence[str] = ...) -> None: ...
def wraps(wrapped: _AnyCallable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[_AnyCallable], _AnyCallable]: ...
def total_ordering(cls: type) -> type: ...
def cmp_to_key(mycmp): ...

# TODO: give a more specific return type for partial (a callable object with some attributes).
def partial(func: _AnyCallable, *args, **keywords) -> Any: ...