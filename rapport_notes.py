# rapport_notes.py - rapport de notes lisible pour un enseignant

SEUIL = 10      # note minimale pour être "valide"
BONUS = 1.0     # points de bonus ajoutés à chaque note
NOTE_MAX = 20   # le bonus ne peut pas dépasser cette valeur


def generer_rapport(notes, seuil=SEUIL, bonus=BONUS, note_max=NOTE_MAX):
    nb_notes = len(notes)
    if nb_notes == 0:
        return "=== Rapport des notes ===\nAucune note à analyser."

    # Indicateurs
    notes_bonus = [min(note + bonus, note_max) for note in notes]
    notes_valides = [note for note in notes if note >= seuil]
    moyenne_initiale = sum(notes) / nb_notes
    moyenne_bonus = sum(notes_bonus) / len(notes_bonus)

    # Construction du texte petit à petit
    lignes = []
    lignes.append("=== Rapport des notes ===")
    lignes.append(f"Nombre d'étudiants : {nb_notes}")
    lignes.append(f"Notes originales : {notes}")
    lignes.append(f"Notes après bonus : {notes_bonus}")
    lignes.append(f"Moyenne initiale : {moyenne_initiale:.2f}")
    lignes.append(f"Moyenne après bonus : {moyenne_bonus:.2f}")
    lignes.append(f"Notes ≥ {seuil} : {notes_valides} (soit {len(notes_valides)} étudiants)")
    lignes.append(f"Top 3 des notes : {sorted(notes, reverse=True)[:3]}")
    lignes.append("Détails par étudiant :")

    for index, note in enumerate(notes, start=1):
        bonus_note = notes_bonus[index - 1]
        lignes.append(f"  Étudiant {index:02d} — note {note:>5.2f} → bonus {bonus_note:>5.2f}")

    return "\n".join(lignes)


if __name__ == "__main__":
    notes = [12.5, 8.0, 15.0, 9.5, 18.0, 10.0]

    rapport = generer_rapport(notes)
    print(rapport)

    # Sauvegarde pour un collègue
    with open("rapport_notes.txt", "w", encoding="utf-8") as f:
        f.write(rapport)
    print("\nRapport sauvegardé dans rapport_notes.txt")
