def verifica_partizioni_avanzata(shipper, worker_per_shipper, topic_partitions, scaling_factor=1):
    # Calcolare il numero totale di worker attivi nel sistema
    worker_totali = shipper * worker_per_shipper
    
    # Messaggio iniziale
    print(f"Numero di Shipper: {shipper}")
    print(f"Numero di Worker per Shipper: {worker_per_shipper}")
    print(f"Totale Worker attivi: {worker_totali}\n")
    
    # Lista per i suggerimenti di partizionamento
    suggerimenti = []
    
    # Loop attraverso i topic per fare la verifica delle partizioni
    for topic, partizioni_topic in topic_partitions.items():
        # Calcolare il numero di partizioni richiesto con il fattore di scalabilità
        partizioni_richieste = int(worker_totali * scaling_factor)
        
        print(f"Topic '{topic}': {partizioni_topic} partizioni attuali, {partizioni_richieste} richieste.")
        
        # Verifica se il numero di partizioni attuali è inferiore a quello richiesto
        if partizioni_topic < partizioni_richieste:
            partizioni_da_aggiungere = partizioni_richieste - partizioni_topic
            suggerimenti.append(f"Topic '{topic}' è sottodimensionato. Aggiungere almeno {partizioni_da_aggiungere} partizioni.")
        else:
            suggerimenti.append(f"Topic '{topic}' ha un numero sufficiente di partizioni.")
    
    # Stampare i suggerimenti
    print("\nSuggerimenti:")
    for suggerimento in suggerimenti:
        print(suggerimento)

# Esempio di utilizzo con venti topic e partizioni differenti
shipper = 3  # Numero di shipper (istanze di Logstash)
worker_per_shipper = 4  # Numero di worker per ogni istanza Logstash

# Dizionario con topic e numero di partizioni correnti
topic_partitions = {
    'topic1': 8,
    'topic2': 10,
    'topic3': 12,
    'topic4': 15,
    'topic5': 6,
    'topic6': 20,
    'topic7': 4,
    'topic8': 25,
    'topic9': 14,
    'topic10': 10,
    'topic11': 12,
    'topic12': 8,
    'topic13': 18,
    'topic14': 10,
    'topic15': 6,
    'topic16': 10,
    'topic17': 12,
    'topic18': 7,
    'topic19': 9,
    'topic20': 11
}

scaling_factor = 1.2  # Fattore di scalabilità opzionale

verifica_partizioni_avanzata(shipper, worker_per_shipper, topic_partitions, scaling_factor)

