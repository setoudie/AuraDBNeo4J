from django.shortcuts import render
from aura_config import get_driver

# Vérifier la connexion
db = get_driver()
print(db)

# Requête Cypher pour créer un nœud 'Prompt'
test_query = """
    CREATE (p:Prompt {pid: '1234', content: 'This is a sample prompt'})
    RETURN p
"""

# Exécution de la requête Cypher
db.run(test_query)
