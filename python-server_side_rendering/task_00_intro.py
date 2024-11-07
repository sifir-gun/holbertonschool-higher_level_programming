import os

def generate_invitations(template, attendees):
    # Vérification du type de template
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    
    # Vérification du type de attendees
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Vérification du modèle vide
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Vérification de la liste des invités vide
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Traitement de chaque invité et création des fichiers
    for i, attendee in enumerate(attendees, start=1):
        # Remplacer les valeurs manquantes par "N/A"
        filled_template = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        # Écriture dans le fichier de sortie
        output_file = f"output_{i}.txt"
        with open(output_file, 'w') as file:
            file.write(filled_template)
        print(f"File {output_file} generated.")
