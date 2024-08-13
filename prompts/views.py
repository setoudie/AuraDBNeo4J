from django.shortcuts import render
from py2neo import Graph

# Create your views here.
db = Graph('bolt://localhost:7687', auth=("neo4j", "tryagain"))

test_querry = """
    CREATE (p:Prompt {pid: '1234', content: 'This is a sample prompt'})
    RETURN p
"""

db.run(test_querry)