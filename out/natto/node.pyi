# Stubs for natto.node (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class MeCabNode:
    NOR_NODE: int = ...
    UNK_NODE: int = ...
    BOS_NODE: int = ...
    EOS_NODE: int = ...
    EON_NODE: int = ...
    ptr: Any = ...
    prev: Any = ...
    next: Any = ...
    enext: Any = ...
    bnext: Any = ...
    rpath: Any = ...
    lpath: Any = ...
    surface: Any = ...
    feature: Any = ...
    nodeid: Any = ...
    length: Any = ...
    rlength: Any = ...
    rcattr: Any = ...
    lcattr: Any = ...
    posid: Any = ...
    char_type: Any = ...
    stat: Any = ...
    isbest: Any = ...
    alpha: Any = ...
    beta: Any = ...
    prob: Any = ...
    wcost: Any = ...
    cost: Any = ...
    def __init__(self, nptr: Any, surface: Any, feature: Any) -> None: ...
    def is_nor(self): ...
    def is_unk(self): ...
    def is_bos(self): ...
    def is_eos(self) -> bool: ...
    def is_eon(self): ...