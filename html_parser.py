# https://peps.python.org/pep-0484/#the-problem-of-forward-declarations
from __future__ import annotations
from typing import TypeVar, Generic, Optional


T = TypeVar('T')


class Tag(Generic[T]):
    def __init__(self):
        self.parent = None
        self.tag_name = None
        self.children = []
        self.attrs = {}
    
    
    def set_parent(self, parent: Tag[T]) -> None:
        self.parent = parent
    
    
    def set_tag_name(self, tag_name: str) -> None:
        self.tag_name = tag_name
    
    
    def append_child(self, child: Tag[T]) -> None:
        self.children.append(child)
        child.set_parent(self)
    
    
    def set_attribute(self, key: str, value: str) -> None:
        self.attrs[key] = value