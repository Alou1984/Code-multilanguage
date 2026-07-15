from .emailer import send_email

def main():
    message = '''
Agent professionnalisation IA Data PRO

Recherche :
- Contrat de professionnalisation
- Graduate Program
- Big Data
- IA
- LLM
- MLOps
- Energie
- Oil & Gas
- Mining
- Aéronautique

Le moteur de recherche sera connecté aux sources configurées.
'''
    send_email("Agent professionnalisation IA Data PRO", message)

if __name__ == "__main__":
    main()
