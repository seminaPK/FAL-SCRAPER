FAL-SCRAPER
===========

Prototipo di applicazione in Python e Javascript che in due step fa scraping dei file PDF contenenti gli orari dei treni delle Ferrovie Appulo Lucane (FAL) e li inserisce in un oggetto JSON. I dati ottenuti possono essere utilizzati per sviluppare nuove applicazioni Web.

--------------------------------------------

SCRAPING DELLE INFORMAZIONI SU LINEE ED ORARI DAL SITO DELLE FERROVIE APPULO LUCANE - http://ferrovieappulolucane.it -

--------------------------------------------

TEAM:

Silvia GIANNINI <slv.giannini@gmail.com>
Rosario SANTORO <rosario.santoro1@gmail.com>

--------------------------------------------

Applicazione composta di due parti da eseguire in quest'ordine:

	1) mhoo14_fal_step1: script python per l'invio di richieste POST alla pagina di ricerca degli orari. Queste richieste coprono tutte le tratte treno/bus nell'arco di una giornata feriale a partire dalle ore 00.
	OUTPUT: sequenza di pagine html dei risultati il cui nome è "mhoo14_fal_X.html" dove la X è un progressivo che identifica le richieste numerandole da 0. Queste pagine vanno copiate nella cartella "data" del secondo step dell'applicazione.

	2) mhoo14_fal_step2: elaborazione con javascript del contenuto delle pagine prodotte dallo step1. L'output (visualizzabile nella console del browser dal quale viene invocato l'index.html) mostra man mano le seguenti informazioni:

	ID_CORSA - PARTENZA - ORARIO_PARTENZA - ARRIVO - ORARIO_ARRIVO
	
	Esempio: 22 - Altamura - 19:16 - Toritto - 19:39

	e al termine comporrà un oggetto JSON contenente tutte queste info (oggetto di nome "fal" in index.html).

	NOTA: ID_CORSA è univoco per coppie di stazioni. Per avere una chiave primaria è necessario associargli anche l'orario di partenza.

	NOTA: l'elaborazione richiede un po' di tempo.


NOTA: all'interno della cartella step2/example ci sono anche due esempi di risultati di ricerca nei casi in cui vengano restituiti dei risultati oppure no.

----------------------------------------------
TO DO: Aggregazione delle info nell'oggetto JSON a formare i percorsi di andata/ritorno
