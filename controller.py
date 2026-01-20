

#funzione che crea grafo
def handle_graph(self, e):
    """ Handler per gestire creazione del grafo """
    self._model.BuildGraf()

    self._view.lista_visualizzazione_1.controls.clear()
    self._view.lista_visualizzazione_1.controls.append(ft.Text(f' '))

    self._view.button.disabled = False
    self._view.update()



# Metodo per popolare i dropdown
def populate_dd(self):

    for year in self._model.get_year():
        self._view.dd_year.options.append(
            ft.DropdownOption(key=squadra.id, text=squadra.name))

    for shape in self._model.get_shape():
        self._view.dd_shape.options.append(
            ft.DropdownOption(f'{shape}'))

    self._view.update()



#scrittura per scrivere       nodo --> nodo  peso
for i in range(len(path) - 1):
        w = self._model.G[path[i]][path[i + 1]]["weight"]
        self._view.txt_risultato.controls.append(ft.Text(f"{path[i]} -> {path[i + 1]} (peso {w})"))
    self._view.txt_risultato.controls.append(ft.Text(f"Peso totale: {weight}"))
    self._view.update()