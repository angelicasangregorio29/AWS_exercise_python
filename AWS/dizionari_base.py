# dizionari_base.py

# Creazione del dizionario config
config = {
    "host": "192.168.1.1",
    "port": 8080,
    "ssl": True,
    "timeout": 30
}

# Stampare il valore di "host"
print("Host:", config["host"])

# Modificare "port" in 443
config["port"] = 443

# Aggiungere una nuova chiave "protocol" con valore "https"
config["protocol"] = "https"

# Stampare il dizionario completo
print(config)