# Importazioni
import copy
from functools import lru_cache

# Creare la classe model
class Model:

    # Definire il metodo __init__
    def __init__(self):
        self._anagrammi = []

    # Definire il metodo calcola_anagrammi, che restituirà la lista degli anagrammi della parola
    def calcola_anagrammi(self, parola):
        self._anagrammi =[]
        self.ricorsione("", parola)
        return self._anagrammi

    # Definire il metodo ricorsione, che rappresenta una funzione ricorsiva
    def ricorsione(self, parziale, lettere_rimanenti):
        # Caso terminale: non ci sono lettere rimanenti
        if len(lettere_rimanenti) == 0:
            self._anagrammi.append(parziale)
            return
        # Altrimenti, bisogna aggiungere una lettera per volta e andare avanti con la ricorsione
        else:
            for i in range(0, len(lettere_rimanenti)):
                # "Aggiungi una lettera"
                parziale = parziale + lettere_rimanenti[i]
                # "Aggiorna le lettere rimanenti"
                nuove_lettere_rimanenti = lettere_rimanenti[:i] + lettere_rimanenti[i+1:]
                # "Continua con la ricorsione"
                self.ricorsione(parziale, nuove_lettere_rimanenti)
                # Bisogna ancora fare il backtraking, ossia togliere l'ultima lettera che è stata aggiunta
                parziale = parziale[:-1] # se non si aggiunge questo pezzo di codice, allora una lettera in più
                # rimarrebbe sempre

    # E se il parziale non è una lista, ma una stringa?
    def calcola_anagrammi_lista(self, parola):
        self._anagrammi = []
        self.ricorsione_lista([], parola)
        return self._anagrammi

    def ricorsione_lista(self, parziale, lettere_rimanenti):
        if len(lettere_rimanenti) == 0:
            self._anagrammi.append(copy.deepcopy(parziale)) # bisogna copiare "profondamente" il parziale: se non lo
            # copiassimo, il parziale verrebbe continuatamente modificato ritornando alla sua versione iniziale, ossia
            # la lista vuota
            return
        # Altrimenti, bisogna aggiungere una lettera per volta e andare avanti con la ricorsione
        else:
            for i in range(0, len(lettere_rimanenti)):
                # "Aggiungi una lettera"
                parziale.append(lettere_rimanenti[i])
                # "Aggiorna le lettere rimanenti"
                nuove_lettere_rimanenti = lettere_rimanenti[:i] + lettere_rimanenti[i+1:]
                # "Continua con la ricorsione"
                self.ricorsione_lista(parziale, nuove_lettere_rimanenti)
                # Bisogna ancora fare il backtraking, ossia togliere l'ultima lettera che è stata aggiunta
                parziale.pop() # se non si aggiunge questo pezzo di codice, allora una lettera in più
                # rimarrebbe sempre

    # Come si gestiscono le parole che presentano delle lettere ripetute?
    # La soluzione migliore è quella di utilizzare gli insiemi

    def calcola_anagrammi_set(self, parola):
        self._anagrammi = set()
        self.ricorsione_set("", "".join(sorted(parola)))
        return self._anagrammi

    # Definire il metodo ricorsione, che rappresenta una funzione ricorsiva
    @lru_cache(maxsize=None)
    def ricorsione_set(self, parziale, lettere_rimanenti):
        # Caso terminale: non ci sono lettere rimanenti
        if len(lettere_rimanenti) == 0:
            self._anagrammi.add(parziale)
            return
        # Altrimenti, bisogna aggiungere una lettera per volta e andare avanti con la ricorsione
        else:
            for i in range(0, len(lettere_rimanenti)):
                # "Aggiungi una lettera"
                parziale = parziale + lettere_rimanenti[i]
                # "Aggiorna le lettere rimanenti"
                nuove_lettere_rimanenti = lettere_rimanenti[:i] + lettere_rimanenti[i+1:]
                # "Continua con la ricorsione"
                self.ricorsione_set(parziale, nuove_lettere_rimanenti)
                # Bisogna ancora fare il backtraking, ossia togliere l'ultima lettera che è stata aggiunta
                parziale = parziale[:-1] # se non si aggiunge questo pezzo di codice, allora una lettera in più
                # rimarrebbe sempre

    # Per impiegare meno tempo e alleggerire il programma conviene usare la cache?
    # La cache stampa gli input e gli output
    # Si può capire se utilizzarla o meno calcolando i tempi di esecuzione con la cache e senza
    # In questo casa è utile nel metodo che utilizza i set: si pensi, infatti, ai casi in cui ci sono delle lettere
    # ripetute... si avranno, infatti, dei risultati uguali e la cache, quindi, aiuta
    # Per massimizzare la cache, si può fare una sorting: in questo modo non vengono considerati gli indici ("casaaa")
    # Per fare ciò, si aggiunge sorted nel metodo anagrammi_set
    # Nel metodo calcola_anagrammi_lista si osserva, invece, che l'utilizzo della cache non è ottimale

if __name__ == "__main__":
    model = Model()
    print(model.calcola_anagrammi("Dog"))
    print(model.calcola_anagrammi_lista("Dog"))
    print(model.calcola_anagrammi_set("casa"))