# https://peps.python.org/pep-0484/#the-problem-of-forward-declarations
from __future__ import annotations
from typing import TypeVar, Generic, Union, Optional


T = TypeVar('T')


class NavigableString(Generic[T]):
    def __init__(self):
        pass


class Tag(Generic[T]):
    def __init__(self):
        self.level = 0
        self.parent = None
        self.tag_name = None
        self.children = []
        self.attrs = {}
    
    # getters
    def get_level(self) -> int:
        return self.level
    
    
    def get_tag_name(self) -> str:
        return self.tag_name
    
    
    # setters
    def set_parent(self, parent: Tag[T]) -> None:
        self.parent = parent
        self.level = parent.get_level() + 1
    
    
    def set_tag_name(self, tag_name: str) -> None:
        self.tag_name = tag_name
    
    
    def append_child(self, child: Union(NavigableString[T], Tag[T])) -> None:
        self.children.append(child)
        child.set_parent(self)
    
    
    def set_attribute(self, key: str, value: str) -> None:
        self.attrs[key] = value
    
    
    # utility functions
    def find(self, tag: str) -> Optional(Tag[T]):
        for child in self.children:
            if child.get_tag_name() == tag:
                return child
        return None
    
    
    def find_all(self, tag: str) -> list[Tag[T]]:
        return list(filter(lambda x: x.get_tag_name() == tag, self.children))
    
    
    # function overloads
    def __str__(self) -> str:
        attributes_string = ' '.join(list(map(lambda key_value: '{0}="{1}"'.format(key_value[0], key_value[1]), self.attrs.items())))
        children_string = '\n'.join(list(map(lambda x: str(x), self.children)))
        
        return '''{base_indent}<{tag_name}{space_if}{attributes}>\n{children}\n{base_indent}</{tag_name}>'''.format(
            base_indent=self.level * '\t',
            tag_name=self.tag_name,
            space_if=' ' if len(self.attrs) > 0 else '',
            attributes=attributes_string,
            children=children_string
        )


tag = Tag()
tag.set_tag_name('form')
tag.set_attribute('test', 1)
tag.set_attribute('other', 2)
child = Tag()
child.set_tag_name('input')
tag.append_child(child)

print(tag)