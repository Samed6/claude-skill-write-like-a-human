# claude-skill-write-like-a-human

Un skill pour Claude qui fait écrire l'IA comme un humain : il rédige et relit des textes sans les tics d'écriture IA, sans "—", sans règle de trois, sans ton de brochure.

A Claude skill that makes AI write like a human: it writes and reviews text without the AI writing tics, no em dashes, no rule of three, no brochure tone.

[Français](#français) | [English](#english)

## Français

La liste des tics vient de deux sources tenues par les bénévoles de Wikipédia :

- [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), du WikiProject AI Cleanup (version anglaise)
- [Aide:Identifier l'usage d'une IA générative](https://fr.wikipedia.org/wiki/Aide:Identifier_l'usage_d'une_IA_g%C3%A9n%C3%A9rative) et [Aide:Identifier une source générée par IA](https://fr.wikipedia.org/wiki/Aide:Identifier_une_source_g%C3%A9n%C3%A9r%C3%A9e_par_IA), de l'Observatoire des IA (version française)

### Ce que fait le skill

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

### Contenu du dépôt

- `SKILL.md` : les instructions du skill
- `scripts/check_tics.py` : un script qui compte les tics de surface dans des fichiers texte en français

```bash
python3 scripts/check_tics.py mon-texte.md
```

Le script ne remplace pas une relecture : il ne juge pas les phrases creuses et peut signaler de faux groupes de trois.

### Installation

Avec Claude Code, copie le contenu de ce dépôt dans le dossier `~/.claude/skills/ecriture-sans-tics-ia/` de ton ordinateur.

Le dossier doit porter le nom `ecriture-sans-tics-ia`, celui du champ `name:` de `SKILL.md`, et non celui du dépôt. Si tu clones, renomme le dossier obtenu.

Sur Claude.ai, télécharge le dépôt en .zip et importe-le comme skill personnalisé depuis les paramètres de ton compte.

### Limites

Aucun signe isolé ne prouve qu'un texte vient d'une IA. Les modèles sont entraînés sur des textes humains, et beaucoup de rédacteurs ont ces habitudes. Utilise le skill pour améliorer un texte, pas pour accuser quelqu'un.

Les pages de Wikipédia évoluent. Ce skill reflète leur contenu de novembre 2026.

### Licence

Le contenu de ce skill est dérivé de pages de Wikipédia publiées sous licence [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Il est publié sous la même licence : tu peux le réutiliser et le modifier si tu cites les sources et publies tes modifications sous la même licence.

## English

The list of tics comes from two pages maintained by Wikipedia volunteers:

- [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), from WikiProject AI Cleanup (English Wikipedia)
- [Aide:Identifier l'usage d'une IA générative](https://fr.wikipedia.org/wiki/Aide:Identifier_l'usage_d'une_IA_g%C3%A9n%C3%A9rative) and [Aide:Identifier une source générée par IA](https://fr.wikipedia.org/wiki/Aide:Identifier_une_source_g%C3%A9n%C3%A9r%C3%A9e_par_IA), from the Observatoire des IA (French Wikipedia)

### What the skill does

The tics are not listed at random. They are grouped into six families, by the mechanism that produces them:

1. Smoothing toward the average: the model replaces precise facts with phrases that would be true of any subject (inflated importance, brochure tone, vague attribution, empty sentences).
2. Learned language habits: AI vocabulary, "it's not X, it's Y", rule of three, cascading synonyms.
3. Source genres: README and slide-deck formatting applied everywhere (bold, lists, tables, em dashes).
4. Conversation leaking into the text: "Of course!", "Feel free to", "It is important to note", unfilled template placeholders.
5. References produced without checking: invalid identifiers (DOI, ISBN) and duplicate sources.
6. Breaks in style: flawless passages mixed with faulty ones, inconsistent quotation marks.

Understanding the cause makes it possible to recognise a variant that appears on no list.

The skill also applies two rules the Wikipedia pages insist on. Removing a tic is not enough: it has to be replaced with a precise fact, or the sentence has to go, and nothing may be invented. The signs Wikipedia considers unreliable (flawless grammar, mixed register) are not "corrected", and the skill does not add mistakes to sound human.

One rule is strict: the skill never writes "—" or "–". It uses the keyboard hyphen "-", or a comma, parentheses, a colon.

### What is in this repository

- `SKILL.md`: the skill instructions
- `scripts/check_tics.py`: a script that counts surface tics in French text files

```bash
python3 scripts/check_tics.py my-text.md
```

The script is no substitute for reading the text: it does not judge empty sentences, and it can flag groups of three that are fine.

Note that the instructions in `SKILL.md` are written in French, and the script's patterns target French text. Claude applies the rules to the language you are writing in, but the catalogue itself is French.

### Installation

With Claude Code, copy the contents of this repository into the `~/.claude/skills/ecriture-sans-tics-ia/` folder on your machine.

The folder has to be named `ecriture-sans-tics-ia`, after the `name:` field in `SKILL.md`, not after the repository. If you clone it, rename the resulting folder.

On Claude.ai, download the repository as a .zip and import it as a custom skill from your account settings.

### Limits

No single sign proves that a text came from an AI. Models are trained on human writing, and plenty of writers have these habits. Use the skill to improve a text, not to accuse anyone.

The Wikipedia pages change over time. This skill reflects their content as of November 2026.

### Licence

The content of this skill derives from Wikipedia pages published under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) licence. It is published under the same licence: you may reuse and modify it as long as you credit the sources and publish your changes under the same licence.
