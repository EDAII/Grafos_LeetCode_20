from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)
        
        # Ordena tickets em ordem inversa para usar pop() como se fosse min-heap
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        
        itinerary = []
        
        def dfs(airport: str):
            # enquanto houver voos saindo desse aeroporto
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            # quando não há mais para onde ir, adiciona na rota
            itinerary.append(airport)
        
        dfs("JFK")
        # inverte para ter a ordem correta do itinerário
        return itinerary[::-1]
