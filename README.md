# ecriture-sans-tics-ia

Un skill pour Claude qui écrit et relit des textes sans les tics d'écriture IA.

La liste des tics vient de deux sources tenues par les bénévoles de Wikipédia :

- [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), du WikiProject AI Cleanup (version anglaise)
- [Aide:Identifier l'usage d'une IA générative](https://fr.wikipedia.org/wiki/Aide:Identifier_l'usage_d'une_IA_g%C3%A9n%C3%A9rative) et [Aide:Identifier une source générée par IA](https://fr.wikipedia.org/wiki/Aide:Identifier_une_source_g%C3%A9n%C3%A9r%C3%A9e_par_IA), de l'Observatoire des IA (version française)

## Ce que fait le skill

Les tics ne sont pas listés dans le désordre. Ils sont rangés en six familles, selon le mécanisme qui les produit :

1. Le lissage vers la moyenne : le modèle remplace les faits précis par des formules valables pour n'importe quel sujet (importance gonflée, ton de brochure, attributions vagues, phrases creuses).
2. Les habitudes de langue apprises : vocabulaire IA, "ce n'est pas X, c'est Y", règle de trois, synonymes en cascade.
3. Les genres d'origine : la mise en forme des README et des diapositives appliquée partout (gras, listes, tableaux, tirets longs).
4. La fuite de la conversation : "Bien sûr !", "N'hésitez pas", "Il est important de noter", gabarits à trous.
5. Les références produites sans vérification : identifiants invalides (DOI, ISBN) et sources en double.
6. Les ruptures de style : passages parfaits mêlés à des passages fautifs, guillemets incohérents.

Comprendre la cause permet de reconnaître une variante qui n'est dans aucune liste.

Le skill applique aussi deux règles que les pages de Wikipédia mettent en avant. Retirer un tic ne suffit pas : il faut le remplacer par un fait précis ou couper la phrase, sans jamais inventer. Les indices que Wikipédia juge inefficaces (grammaire parfaite, registre mélangé) ne sont pas "corrigés", et le skill n'ajoute pas de fautes pour paraître humain.

Une règle est stricte : le skill n'écrit jamais "—" ni "–". Il utilise le trait d'union du clavier "-", ou une virgule, des parenthèses, deux-points.

## Contenu du dépôt

- `SKILL.md` : les instructions du skill
- `scripts/check_tics.py` : un script qui compte les tics de surface dans des fichiers texte en français

```bash
python3 scripts/check_tics.py mon-texte.md
```

Le script ne remplace pas une relecture : il ne juge pas les phrases creuses et peut signaler de faux groupes de trois.

## Installation

Avec Claude Code, copie le contenu de ce dépôt dans le dossier `~/.claude/skills/ecriture-sans-tics-ia/` de ton ordinateur.

Sur Claude.ai, télécharge le dépôt en .zip et importe-le comme skill personnalisé depuis les paramètres de ton compte.

## Limites

Aucun signe isolé ne prouve qu'un texte vient d'une IA. Les modèles sont entraînés sur des textes humains, et beaucoup de rédacteurs ont ces habitudes. Utilise le skill pour améliorer un texte, pas pour accuser quelqu'un.

Les pages de Wikipédia évoluent. Ce skill reflète leur contenu de novembre 2026.

## Licence

Le contenu de ce skill est dérivé de pages de Wikipédia publiées sous licence [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Il est publié sous la même licence : tu peux le réutiliser et le modifier si tu cites les sources et publies tes modifications sous la même licence.

## English summary

A Claude skill that writes and reviews text without the AI writing tics catalogued by Wikipedia volunteers (WikiProject AI Cleanup and the French Observatoire des IA). Tics are grouped by the mechanism that produces them, so that new variants can be recognised. The instructions are in French. Licensed CC BY-SA 4.0, like its Wikipedia sources.
