
def handle_graph(self, e):
    """ Handler per gestire creazione del grafo """
    self._model.BuildGraf()

    self._view.lista_visualizzazione_1.controls.clear()
    self._view.lista_visualizzazione_1.controls.append(ft.Text(f' '))

    self._view.button.disabled = False
    self._view.update()
########################################################################
#PUNTO 2

def handle_ricerca(self, e):
    """ Handler per gestire il problema ricorsivo di ricerca del cammino """""

try:
    threshold = float(self._view.txt_name.value)
    self._model.ricerca_cammino(threshold)
    self._view.lista_visualizzazione_3.controls.clear()
    self._view.lista_visualizzazione_3.controls.append(
        ft.Text(f"Numero archi percorso più lungo: {len(self._model.soluzione_best)}"))
    self._view.update()

    self._view.lista_visualizzazione_3.controls.append(ft.Text(
        f"Peso cammino massimo: {str(self._model.compute_weight_path(self._model.soluzione_best))}"))

    '''for ii in self._model.soluzione_best:
        self._view.lista_visualizzazione_3.controls.append(ft.Text(
            f"{ii[0]} --> {ii[1]}: {str(ii[2]['weight'])}"))
    '''
except ValueError:
    self._view.show_alert("    ")