import re
import sys

CHECKS = {
    "tiret cadratin ou demi-cadratin": r"[—–]",
    "gras markdown": r"\*\*",
    "emoji": r"[\U0001F300-\U0001FAFF☀-➿]",
    "parallelisme negatif": r"(n'est pas (seulement|juste|qu)|non pas .{1,40} mais|ce n'est pas .{1,60}, c'est)",
    "avertissement didactique": r"(il est (important|crucial|essentiel) de|il convient de)",
    "conclusion / resume": r"(en conclusion|en résumé|en définitive|dans l'ensemble)",
    "formule de service": r"(n'hésitez pas|faites-moi savoir|bien sûr !|souhaitez-vous)",
    "participe creux": r", (soulignant|favorisant|reflétant|témoignant|mettant en)",
    "fuite du verbe etre": r"(se positionne comme|sert de|se dresse comme|constitue|représente)",
    "attribution vague": r"(de nombreux experts|plusieurs sources|certains spécialistes|selon des experts)",
    "ton brochure": r"(niché|au cœur de|incontournable|véritable|riche patrimoine|à couper le souffle|révolution)",
    "vocabulaire IA": r"\b(crucial|essentiel|rôle clé|écosystème|de plus|en outre|notamment|mettre en lumière|souligner|témoign\w*|paysage|plonger)\b",
}
TRIAD = r"\b[\wéèêàç'-]+, [\wéèêàç' -]+ (et|ou) [\wéèêàç'-]+\b"

for path in sys.argv[1:]:
    text = open(path, encoding="utf-8").read()
    low = text.lower()
    hits = []
    for name, pat in CHECKS.items():
        n = len(re.findall(pat, low))
        if n:
            hits.append(f"{name} x{n}")
    n = len(re.findall(TRIAD, low))
    if n:
        hits.append(f"groupe de trois possible x{n}")
    words = len(re.findall(r"\w+", text))
    print(f"{path.split('/')[-1]} ({words} mots): " + (", ".join(hits) if hits else "aucun tic détecté"))
