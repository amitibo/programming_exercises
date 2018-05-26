"""Find if team A can beat team B.
"""

import collections


MatchResult = collections.namedtuple("MatchResult", ("winning", "loosing"))


def can_team_A_beat_team_B(matches : MatchResult, team_A : str, team_B : str):

    graph = collections.defaultdict(set)
    def create_graph():
        for match in matches:
            graph[match.winning] = match.loosing

        return graph

    def find_path(graph, src, dst, visited=set()):

        if src == dst:
            return True

        visited.add(src)

        return any(find_path(graph, child, dst, visited) \
                   for child in graph[src] if child not in visited)

    return find_path(create_graph(), team_A, team_B)