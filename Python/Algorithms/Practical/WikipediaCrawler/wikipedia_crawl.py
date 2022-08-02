import cProfile
import time

import lxml
import cchardet
import math
from collections import deque
from typing import Dict, List, Callable, Tuple

import requests
from bs4 import BeautifulSoup, SoupStrainer
from requests import Session


class WikipediaNode:
    WIKIPEDIA_URL_PREFIX = 'https://en.wikipedia.org'
    other_link_prefixes = ['Template:', 'Template_talk:', 'Special:', 'File:']
    session: Session = None
    title_strainer = SoupStrainer('h1', id='firstHeading')
    wiki_link_strainer = SoupStrainer('a', href=True)

    def __init__(self, url: str) -> None:
        self.url = url
        self._adjacency_list = None
        self.title = None
        self.html_content = None
        if self.session is None:
            self.session = requests.Session()

    @staticmethod
    def removeprefix(text: str, prefix: str) -> str:
        return text[text.startswith(prefix) and len(prefix):]

    def get_title(self) -> str:
        if self.title is not None:
            return self.title

        if self.html_content is None:
            self.html_content = self.session.get(self.url)
            resp = self.html_content
        else:
            resp = self.html_content
            self.html_content = None

        content = BeautifulSoup(resp.content, 'lxml', parse_only=self.title_strainer)
        return content.text

    def get_adjacent_nodes(self) -> List['WikipediaNode']:
        if self._adjacency_list is not None:
            return self._adjacency_list
        else:
            self._adjacency_list = []

        if self.html_content is None:
            self.html_content = self.session.get(self.url)
            resp = self.html_content
        else:
            resp = self.html_content
            self.html_content = None

        links = BeautifulSoup(resp.content, 'lxml', parse_only=self.wiki_link_strainer)

        is_wiki_url: Callable[[str], bool] = lambda url: url.startswith('/wiki/')
        urls = [link['href'] for link in links.find_all('a')]
        urls = list(filter(is_wiki_url, urls))

        for url in urls:
            sub_path = self.removeprefix(url, '/wiki/')
            if any(sub_path.startswith(skip_prefix) for skip_prefix in self.other_link_prefixes):
                continue
            complete_url = self.WIKIPEDIA_URL_PREFIX + url
            self._adjacency_list.append(WikipediaNode(complete_url))

        return self._adjacency_list

    @staticmethod
    def check_url_equality(url1: str, url2: str) -> bool:
        return url1 == url2

    def __eq__(self, other: 'WikipediaNode') -> bool:
        return self.check_url_equality(self.url, other.url)

    def __repr__(self) -> str:
        return f'{self.get_title()} ({self.url})'

    def __hash__(self) -> int:
        return hash(self.get_title())

class BreadthFirstSearch:
    class Path:
        def __init__(self, route: Tuple[WikipediaNode] = None, path_length: int = math.inf) -> None:
            self.route = route
            self.path_length = path_length

        @staticmethod
        def calculate_path(parents: Dict[WikipediaNode, WikipediaNode],
                           start_vertex: WikipediaNode, target_vertex: WikipediaNode) -> 'BreadthFirstSearch.Path':
            path = BreadthFirstSearch.Path()
            route = deque()
            current_vertex = target_vertex
            route.appendleft(current_vertex)
            while current_vertex in parents:
                current_vertex = parents[current_vertex]
                route.appendleft(current_vertex)
                if current_vertex == start_vertex:
                    path.route = tuple(route)
                    path.path_length = len(route) - 1
                    return path

            path.route = None
            path.path_length = math.inf
            return path

        def __repr__(self) -> str:
            return ' -> '.join([str(path_node) for path_node in self.route]) if self.route is not None else 'None'

    def __init__(self) -> None:
        self.visited: Dict[WikipediaNode, bool] = {}
        self.queue: List[WikipediaNode] = []
        self.level: Dict[WikipediaNode, int] = {}
        self.parent: Dict[WikipediaNode: int] = {}

    def bfs(self, start_vertex: WikipediaNode, target_vertex: WikipediaNode) -> Path:
        self.bfs_visit(start_vertex, target_vertex)
        return self.Path.calculate_path(self.parent, start_vertex, target_vertex)

    def bfs_visit(self, start_vertex: WikipediaNode, target_vertex: WikipediaNode) -> None:
        self.visited[start_vertex] = True
        self.queue.append(start_vertex)
        current_level = 0
        while self.queue:
            current_vertex = self.queue.pop(0)
            for neighbor in current_vertex.get_adjacent_nodes():
                if neighbor == target_vertex:
                    self.visited[neighbor] = True
                    self.parent[neighbor] = current_vertex
                    self.level[neighbor] = current_level
                    return
                if not neighbor in self.visited or not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    self.level[neighbor] = current_level
                    self.parent[neighbor] = current_vertex
                    self.queue.append(neighbor)
                if len(self.visited) % 30 == 0:
                    print(f'Nodes visited: {len(self.visited)}')
            current_level += 1


if __name__ == '__main__':
    breadth_first_search = BreadthFirstSearch()
    start_time = time.time()
    path = breadth_first_search.bfs(WikipediaNode('https://en.wikipedia.org/wiki/Martin_Demaine'),
                                    WikipediaNode('https://en.wikipedia.org/wiki/Minimax'))

    print(f'Time taken: {time.time() - start_time} seconds')
    print(f'Nodes visited: {len(breadth_first_search.visited)}')
    print(path)