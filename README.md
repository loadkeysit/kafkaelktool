# kafkaelktool
Repository con alcuni tool utili per la gestione di ambienti ELK e Kafka

# Kafka Partition Checker

## Descrizione

### kafkapartitionchecker.py
 
Questo script è progettato per verificare se il numero di partizioni configurate per i topic Kafka è sufficiente rispetto al numero di istanze di Logstash (Shipper) e i loro worker attivi. Kafka non consente di ridurre il numero di partizioni, quindi lo script aiuta a determinare se le partizioni esistenti sono sottodimensionate e fornisce suggerimenti su quante partizioni aggiungere per garantire un bilanciamento efficiente del carico.

### Caratteristiche:
- Calcola il numero totale di worker in base al numero di Shipper e worker per istanza.
- Verifica il numero di partizioni per ciascun topic Kafka rispetto ai worker disponibili.
- Suggerisce quante partizioni devono essere aggiunte per evitare sovraccarichi.
- Supporta un fattore di scalabilità per anticipare espansioni future.

## Esempio di utilizzo

```python
# Parametri di configurazione
shipper = 3  # Numero di istanze Logstash
worker_per_shipper = 4  # Numero di worker per ogni Shipper
topic_partitions = {
    'topic1': 8,
    'topic2': 10,
    'topic3': 12,
    ...
}
scaling_factor = 1.2  # Fattore di scalabilità opzionale

# Esecuzione della funzione di verifica
verifica_partizioni_avanzata(shipper, worker_per_shipper, topic_partitions, scaling_factor)
