from method.ours.utils import is_label, is_input
from method.ours.similarity import get_combined_similarity


class InputGroupNode:
    def __init__(self, input_node):
        self.node = input_node
        self.label = self._get_label(input_node)
        self.group = self._form_group(input_node)
        self.edges = []
    
    
    def add_edge(self, other_group, weight):
        self.edges.append((other_group, weight))
    
    
    def _get_label(self, node):
        candidate_label = list(filter(
            lambda x: is_label(x.target.element) and 'FOR' in x.type.value,
            node.edges.values()
        ))
        if len(candidate_label) > 0:
            return candidate_label[0].target
        return None
    
    
    def _form_group(self, node):
        group = []
        edges = list(node.edges.values())
        
        # label has to be set by _get_label before this step
        if self.label is not None:
            edges.extend(list(self.label.edges.values()))
        
        for edge in edges:
            if not is_input(edge.target.element):
                group.append(edge.target)
        
        group = filter(lambda x: not is_label(x.element), group)
        return list(set(group))
    
    
    def get_similarity(self, model, other_group):
        input_sim = get_combined_similarity(model, self.node, other_group.node)
        label_sim = None
        if self.label is not None and other_group.label is not None:
            label_sim = get_combined_similarity(model, self.label, other_group.label)
        return max(input_sim, label_sim or 0)
    
    
    def __str__(self):
        input_string = f'input:\n{str(self.node.element)}\n'
        
        if self.label is not None:
            input_string += f'with label:\n{str(self.label.element)}\n'
        
        if len(self.group) > 0:
            group_related_node_str = '\n'.join(map(lambda x: str(x.element), self.group))
            input_string += f'with the following relevant text tags:\n{group_related_node_str}\n'
        
        return input_string