# ActivityRecognition

## Installazione librerie
Al fine di utilizzare il codice del progetto, è necessario installare le librerie pandas: https://github.com/pandas-dev/pandas e sklearn: https://github.com/scikit-learn/scikit-learn.
La libreria pandas permette di estrarre i dati dal Dataset.
La libreria sklearn permette di utilizzare l'implementazione di Random Forest e la costruzione della matrice di confusione.

## Download del Dataset
Il programma utilizza il seguente Dataset: http://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones

Per scaricare il Dataset è necessario scaricare la cartella "UCI HAR Dataset.names" al seguente link: http://archive.ics.uci.edu/ml/machine-learning-databases/00240/ , raggiungibile a partire dal precedente link.

Una volta effettuato il download sarà visibile una cartella chiamata UCI HAR Dataset, che contiene due sottocartelle: "_ MACOSX" e "UCI HAR Dataset".
E' necessario prendere la sottocartella "UCI HAR Dataset" e posizionarla nella stessa cartella dove viene posizionato il codice AR_RandomForest.py

## Esecuzione del codice
Una volta effettuato il Download del Dataset e delle librerie, il codice è pronto per essere eseguito. Non vengono chiesti input all'utente.
Il programma elabora i dati presenti nel Dataset, ne stampa il contenuto, costruisce e stampa la matrice di confusione e ulteriori informazioni di classificazione.
