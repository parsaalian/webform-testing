import numpy as np

from method.ours.relation_graph import RelationEdge, EdgeType
from method.ours.utils import is_input, is_label, get_normal_cutoff_score


def remove_span_wraps(relation_graph):
    for edge in relation_graph.edges():
        if edge.target.element.name == 'span-wrap':
            child = edge.target
            relation_graph.remove_edge(edge)
            relation_graph.remove_node(child)
    
    return relation_graph


def remove_input_input_links(relation_graph):
    for edge in relation_graph.edges():
        if is_input(edge.source.element) and is_input(edge.target.element):
            relation_graph.remove_edge(edge)
    
    return relation_graph


def remove_low_score_inputs_from_label(relation_graph, label_node):
    edges = label_node.edges.values()
    input_edges = list(filter(lambda x: is_input(x.target.element), edges))
    sorted_input_edges = sorted(input_edges, key=lambda x: x.weight, reverse=True)
    
    for i in range(1, len(sorted_input_edges)):
        relation_graph.remove_edge(sorted_input_edges[i])
    
    probable_for_edge = sorted_input_edges[0]
    
    if not probable_for_edge.type.value == 'FOR':
        probable_for_edge.set_type(EdgeType.PROBABLE_FOR)
        relation_graph.add_edge(RelationEdge(
            probable_for_edge.target,
            probable_for_edge.source,
            probable_for_edge.type,
            probable_for_edge.weight
        ))
    
    return relation_graph


def remove_low_score_inputs_from_feedback(relation_graph, feedback_node):
    edges = feedback_node.edges.values()
    input_edges = list(filter(lambda x: is_input(x.target.element), edges))
    sorted_input_edges = sorted(input_edges, key=lambda x: x.weight, reverse=True)
    
    for i in range(1, len(sorted_input_edges)):
        relation_graph.remove_edge(sorted_input_edges[i])
    
    probable_feedback_edge = sorted_input_edges[0]
    
    probable_feedback_edge.set_type(EdgeType.FEEDBACK)
    relation_graph.add_edge(RelationEdge(
        probable_feedback_edge.target,
        probable_feedback_edge.source,
        probable_feedback_edge.type,
        probable_feedback_edge.weight
    ))
    
    return relation_graph


def prune_relation_graph_extra_edges(relation_graph):
    relation_graph = remove_span_wraps(relation_graph)
    relation_graph = remove_input_input_links(relation_graph)
    
    for node in relation_graph.nodes():
        if is_input(node.element):
            continue
        if is_label(node.element):
            remove_low_score_inputs_from_label(relation_graph, node)
        if node.get_is_feedback():
            remove_low_score_inputs_from_feedback(relation_graph, node)
    
    return relation_graph


def is_certain_edge(edge):
    return edge.type == EdgeType.FOR or \
        edge.type == EdgeType.PROBABLE_FOR or \
        edge.type == EdgeType.CHILD or \
        edge.type == EdgeType.FEEDBACK


def prune_low_score_uncertain_edges(relation_graph, factor=0.5):
    scores = []
    for edge in relation_graph.edges():
        if is_certain_edge(edge):
            continue
        scores.append(edge.weight)
    
    cutoff = get_normal_cutoff_score(scores, factor)
    
    for edge in relation_graph.edges():
        if is_certain_edge(edge):
            continue
        if edge.weight < cutoff:
            relation_graph.remove_edge(edge)
    
    return relation_graph