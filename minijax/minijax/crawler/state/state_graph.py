class StateGraph:
    def __init__(self):
        self.graph = {}
        self.url_action_map = {}
    
    
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

    
    def add_executed_action_to_url(self, url, action_id, new_state):
        if url not in self.url_action_map:
            self.url_action_map[url] = {}
        self.url_action_map[url][action_id] = new_state
    
    
    def get_executed_actions_in_url(self, url):
        if url not in self.url_action_map:
            return {}
        return self.url_action_map[url]
    
    
    def has_executed_action_in_url(self, url, action_id):
        if url not in self.url_action_map:
            return False
        if action_id not in self.url_action_map[url]:
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
