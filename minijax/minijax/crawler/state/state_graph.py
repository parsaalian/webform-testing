class StateGraph:
    def __init__(self):
        self.graph = {}
    
    
    def add_state(self, state):
        if state.url not in self.graph:
            self.graph[state.url] = []
        self.graph[state.url].append(state)
    
    
    def is_in_graph(self, state):
        if state.url not in self.graph:
            return False
        if state not in self.graph[state.url]:
            return False
        return True

    
    def to_json(self):
        return {
            action: [state.to_json() for state in states] for action, states in self.graph.items()
        }
    
    
    def count_urls(self):
        return len(self.graph.keys())
    
    
    def count_states(self):
        return sum([len(states) for states in self.graph.values()])
