import networkx as nx


class Model:
    def __init__(self):
        #inizializza liste DAO

        self._G= nx.Graph()         #grafo non orientato   nx.DiGraph   grafo orientato
        self._lista_nodi = []
        self._dict_nodi = {}
        self._lista_archi = []

    #  def load_materiale_dao(self):
    #           inizializza liste DAO= funzioni DAO
    #
    #   SE HANNO PARAMETRO FAI SOLO RETURN E LE CHIAMO NEL CONTROLLER

    # CREO DIZIONARIO PER NODI.ID ---> OBJ
    self._dict_nodi = {}
    for node in self._lista_nodi:
        self._dict_nodi[node.cromosoma] = node
    #O in BuildGraf oppure in load_nodi dal DAO




    def BuildGraf(self):
        self._G.clear()
        self._lista_nodi = []
        self._lista_archi = []

        #CREAZIONE NODI GRAFO
        for node in self.lista_dao:
            self._lista_nodi.append(node)
        self._G.add_nodes_from(self._lista_nodi)




        #CREAZIONE ARCHI GRAFO

        #metodo1 (LAB13 geni)
        #Il peso di ciascun arco dovrà essere calcolato come la somma algebrica della correlazione
        #(tabella interazione, colonna correlazione), facendo attenzione a contare ogni coppia di geni una sola volta.
        edges = {}
        for id1, id2, peso in self._lista_edge_dao:
            obj1 = self._dict_nodi[id1]
            obj2 = self._dict_nodi[id2]

            if (obj1, obj2) not in edges:
                edges[( obj1, obj2)] = float(PESO)
            else:
                edges[(obj1, obj2 )] += float(PESO)

        for k, v in edges.items():
            self.lista_edges.append((k[0], k[1], v))
        self.G.add_weighted_edges_from(self._edges)




        #Ultima Parte punto 1
        #METODO1 LAB13 geni
        # Alla pressione del bottone “Conta Archi” stampare il numero di archi il cui peso è <S, ed il numero di archi il cui peso è >S.
        def count_edges(self, t):
            count_bigger = 0
            count_smaller = 0
            for x in self.get_edges():            #self.G.edges(data=True) restituisce (n1,n2, dizionario['weight']= peso)
                if x[2]['weight'] > t:
                    count_bigger += 1
                elif x[2]['weight'] < t:
                    count_smaller += 1
            return count_bigger, count_smaller

        #i valori minimo e massimo dei pesi degli archi.
        def get_min_weight(self):
            return min([x[2]['weight'] for x in self.get_edges()])

        def get_max_weight(self):
            return max([x[2]['weight'] for x in self.get_edges()])


        #METODO 2 Itunes
        #"""Restituisce la componente connessa di un nodo"""
        def get_component(self, album):
            """Restituisce la componente connessa di un album"""
            if album not in self.G:
                return []
            return list(nx.node_connected_component(self.G, album))

    #######################################################################################################################àà
    #PUNTO 2
    #METODO 1 LAB 13 (geni)
    #metodo ricorsivo per cercare dato un grafo pesato, il cammino massimo passando solo per archi
    #con peso > o < di una soglia partendo da un nodo a caso
    def ricerca_cammino(self, soglia):
        self.soluzione_best.clear()

        for n in self.lista_nodi():
            partial = []
            partial_edges = []

            partial.append(n)
            self.ricorsione(partial, partial_edges, soglia)

        return self.soluzione_best

    def ricorsione(self, partial_nodes, partial_edges, t):
        n_last = partial_nodes[-1]

        #cerco i vicini ammissibili dell'ultimo nodo cioe che rispettano i vincoli
        neigh = self._get_admissible_neighbors(n_last, partial_edges, t)

        # stop
        if len(neigh) == 0:
            weight_path = self.compute_weight_path(partial_edges)
            weight_path_best = self.compute_weight_path(self.soluzione_best)
            #PUOI ANCHE PASSARLO ALLA RICORSIONE COME PREDEFINITO E AGGIORNARLO OGNI VOLTA CHE SI SUPERA
            if weight_path > weight_path_best:
                self.soluzione_best = partial_edges[:]
            return

        for n in neigh:
            print("...")
            partial_nodes.append(n)
            partial_edges.append((n_last, n, self.G.get_edge_data(n_last, n))) #self.G[n_last][n]['weight']
            self.ricorsione(partial_nodes, partial_edges, soglia)
            partial_nodes.pop()
            partial_edges.pop()

    def _get_admissible_neighbors(self, node, partial_edges, soglia):
        result = []
        for u, v, data in self.G.out_edges(node, data=True):
            if data["weight"] > soglia:
                # controllo SOLO l'arco diretto
                if (u, v) not in [(x[0], x[1]) for x in partial_edges]:
                    result.append(v)
        return result

    def compute_weight_path(self, mylist):
        weight = 0
        for e in mylist:
            weight += e[2]['weight']
        return weight

    #METODO 2 Itunes
    #Ricerca cammino con peso non superiore a peso soglia con maggiorn numero di nodi che siano connessi al nodo di partenza e lo icluda
    """ def get_component(self, album):
        if album not in self.G:
            return []
        return list(nx.node_connected_component(self.G, album))
    """

    def compute_best_set(self, start_album, max_duration):
        """Ricerca ricorsiva del set massimo di album nella componente connessa"""
        component = self.get_component(start_album)
        self.soluzione_best = []
        self._ricorsione(component, [start_album], start_album.duration, max_duration)
        return self.soluzione_best

    def _ricorsione(self, albums, current_set, current_duration, max_duration):
        if len(current_set) > len(self.soluzione_best):
            self.soluzione_best = current_set[:]### == copy.deepcopy(current_set)

        for album in albums:
            if album in current_set:
                continue
            new_duration = current_duration + album.duration
            if new_duration <= max_duration:
                current_set.append(album)
                self._ricorsione(albums, current_set, new_duration, max_duration)
                current_set.pop()

    #METODO 3 BaseBall
    #Metodo ricorsivo da un nodo di partenza per cercare il cammino di peso massimo che passi per nodi con peso strettamente decrescente:
    #Per limitare i tempi di esecuzione, la procedura ricorsiva deve considerare solo i primi K archi
    # adiacenti ordinati per peso decrescente (ad esempio K=3), cioè ogni vertice esplora al massimo i K vicini più pesanti che rispettano il vincolo decrescente.

    def get_neighbors(self, team):
        vicini = []
        for n in self.G.neighbors(team):
            w = self.G[team][n]["weight"]
            vicini.append((n, w))
        return sorted(vicini, key=lambda x: x[1], reverse=True)

    def compute_best_path(self, start):
        """Calcola percorso di peso massimo con archi strettamente decrescenti"""
        self.best_path = []
        self.best_weight = 0
        self._ricorsione([start], 0, float("inf"))
        return self.best_path, self.best_weight

    def _ricorsione(self, path, weight, last_edge_weight):
        last = path[-1]
        if weight > self.best_weight:
            self.best_weight = weight
            self.best_path = path.copy()

        vicini = self.get_neighbors(last)
        neighbors = []
        counter = 0
        for node, edge_w in vicini:
            if node in path:
                continue
            if edge_w <= last_edge_weight:
                neighbors.append((node, edge_w))
                counter += 1
                if counter == self.K:
                    break

        for node, edge_w in neighbors:
            path.append(node)
            self._ricorsione(path, weight + edge_w, edge_w)
            path.pop()
