---
name: "ecriture-sans-tics-ia"
description: "Écrire, relire ou nettoyer un texte sans les tics d'écriture IA recensés par Wikipédia (EN et FR) : phrases creuses, règle de trois, ton de brochure, vocabulaire IA, gras et listes en trop, et jamais de \"—\" ni \"–\". À utiliser dès qu'il faut rédiger un texte, un post, une fiche produit, un e-mail ou un article, ou quand l'utilisateur demande un texte qui ne sonne pas IA, même sans le dire explicitement."
---

# Écrire sans tics d'IA

Ce skill rassemble les signes d'écriture IA listés par deux pages de Wikipédia :

- "Wikipedia:Signs of AI writing" (WikiProject AI Cleanup, version anglaise)
- "Aide:Identifier l'usage d'une IA générative" et "Aide:Identifier une source générée par IA" (Observatoire des IA, version française)

Il sert dans deux situations :

1. Rédiger un texte neuf qui ne porte aucun de ces tics.
2. Relire le texte de quelqu'un (ou le sien) pour repérer les tics et les corriger.

## Le principe à garder en tête

Les deux pages insistent sur un point : ces signes sont des symptômes, pas le problème. Un modèle de langage prédit la suite la plus probable, il tire donc vers la moyenne. Le texte perd les faits précis et les remplace par des formules valables pour n'importe quel sujet. Les tics de surface (gras, tirets longs, mots à la mode) sont la trace visible de ce lissage.

Conséquence pratique : supprimer les tics sans rien mettre à la place produit un texte plus difficile à détecter et tout aussi creux. La page anglaise met en garde exactement contre ça. Quand tu retires un tic, remplace-le par une information concrète : un chiffre, un nom, une date, un exemple réel, une cause. Si tu n'as pas cette information, raccourcis la phrase ou supprime-la, et ne l'invente jamais.

Aucun signe isolé ne prouve qu'un texte vient d'une IA. Les modèles sont entraînés sur des textes humains et beaucoup de rédacteurs ont ces habitudes. Quand tu relis le texte de quelqu'un, parle de "tics" ou de "formulations à revoir", sans l'accuser d'avoir utilisé une IA.

## Les tics, rangés par cause

Chaque famille part du mécanisme qui produit les tics. Comprendre la cause permet de reconnaître une variante qui n'est pas dans la liste.

### Cause 1 : le lissage vers la moyenne (le fond)

Le modèle ne sait pas ce qui est remarquable dans le sujet, alors il affirme que tout l'est.

- Importance gonflée. Rattacher un détail à une grande tendance : "stands as", "is a testament to", "plays a pivotal/key role", "setting the stage for". En français : "joue un rôle clé", "témoigne de", "marque un tournant", "s'inscrit dans". Correction : dire le fait et laisser le lecteur juger.
- Notoriété prouvée par une liste de médias. "Featured in", "profiled in", "independent coverage", "a été relayé par de nombreux médias". Correction : dire ce que la source affirme, pas qu'elle existe.
- Analyse creuse en fin de phrase. Un participe présent qui ajoute du sens vague : "highlighting...", "ensuring...", "fostering...", "soulignant ainsi...", "favorisant...", "reflétant...". Correction : couper la phrase au point, ou écrire une vraie conséquence avec sa source.
- Ton de brochure. "Boasts", "vibrant", "rich", "nestled", "in the heart of", "groundbreaking", "commitment to". En français : "niché au cœur de", "riche patrimoine", "incontournable", "à couper le souffle", "véritable joyau". Cause : les brochures et communiqués présents dans les données d'entraînement.
- Attributions vagues. "Experts argue", "industry reports", "some critics", "selon plusieurs sources" quand une seule est citée, "de nombreux spécialistes". Correction : nommer la personne ou la source, ou retirer l'affirmation.
- Conclusion formatée sur les défis. "Despite its... faces several challenges", "Malgré ces défis", section "Perspectives" ou "Future Outlook". Parler des difficultés reste normal, c'est le gabarit qui trahit.
- Phrases stéréotypées, creuses ou superficielles (page française). Test : la phrase resterait-elle vraie si on changeait le sujet ? Si oui, elle ne dit rien.
- Traiter un titre descriptif comme un nom propre ("Cette liste est une compilation soigneusement établie de...").

### Cause 2 : les habitudes de langue apprises

- Vocabulaire IA en grappe. "Delve", "tapestry", "testament", "pivotal", "underscore", "showcase", "intricate", "additionally", "crucial", "landscape", "realm". Équivalents français à surveiller : "plonger dans", "tapisserie", "témoignage", "crucial", "essentiel", "souligner", "mettre en lumière", "mettre en avant", "de plus", "en outre", "notamment", "paysage", "univers", "incontournable". Un mot seul ne veut rien dire, l'accumulation est le signal.
- Fuite devant "est/sont". "Serves as", "stands as", "represents", "marks", "boasts", "offers". En français : "sert de", "se dresse comme", "constitue", "représente", "se positionne comme". Correction : "est", "a", "compte".
- Parallélisme négatif. Corriger une affirmation que personne n'a faite : "It's not X, it's Y", "Ce n'est pas seulement X, c'est Y", "Non pas X, mais Y", "Pas de X, pas de Y, juste Z". Ça simule de l'équilibre. Correction : affirmer Y directement.
- Règle de trois. Idées, adjectifs ou exemples groupés par trois ("innovant, transformateur et révolutionnaire"). Ça fait paraître complète une analyse mince. Correction : donner le nombre d'éléments qu'on a réellement, deux, quatre ou un seul.
- Variation élégante. Remplacer le nom du sujet par des synonymes pour éviter la répétition ("le protagoniste", "l'acteur clé", "la figure emblématique"). Cause : la pénalité de répétition du mécanisme de génération. Correction : répéter le nom ou utiliser un pronom.
- Mots de liaison en série en début de phrase ("De plus", "Par ailleurs", "En outre", "Cependant"). Seuls ils ne prouvent rien, en chaîne ils alourdissent.

### Cause 3 : les genres d'origine (README, diapositives, argumentaires)

Le modèle a beaucoup vu de documents conçus pour être survolés, et il en reprend la mise en forme partout.

- Majuscule à chaque mot des titres (Title Case). En français c'est en plus une faute de typographie.
- Gras posé mécaniquement sur des termes, façon "points clés".
- Listes à en-tête intégré : puce, mot en gras, deux-points, explication. Puces tapées à la main ("•", "–"), numérotation manuelle. Si une puce manuelle est nécessaire, utilise "-".
- Listes à puces là où une phrase suffit (page française : usage régulier de listes à puces).
- Émojis dans les titres ou les puces.
- Tiret cadratin (—) et tiret demi-cadratin (–). C'est le tic le plus visible : l'IA met "—" là où un humain mettrait une virgule, des parenthèses ou deux-points, avec un effet de slogan. Ces signes n'existent pas sur un clavier ordinaire, donc un humain ne les tape presque jamais, alors que le modèle les produit directement. Règle sans exception : n'écris jamais "—" ni "–". Quand un tiret est vraiment nécessaire (incise, intervalle comme 2018-2023, liste), utilise le trait d'union du clavier "-". Le plus souvent, une virgule, des parenthèses, deux-points ou un point font mieux le travail. En relecture, remplace chaque "—" et chaque "–" du texte par "-" ou par la ponctuation qui convient.
- Petits tableaux là où une ou deux phrases suffisent.
- Sections calibrées de 1 à 3 paragraphes chacune, toutes de la même taille (page française). Un humain écrit long là où il a de la matière.
- Titres de sections formulés en questions (page française).
- Ligne horizontale avant chaque titre, niveaux de titres sautés.
- Résumé "En bref" ou "Points clés" en liste à puces, "Foire aux questions" plaquée en fin de texte (page française sur les sources).
- Section finale "Conclusion", "En résumé", "Héritage", ou phrase finale vague de portée générale ("Dans l'ensemble", "En définitive", "Overall").
- Plan qui semble correct mais redit les mêmes éléments dans plusieurs sections pour faire du volume (page française).

### Cause 4 : la fuite de la conversation

Le chatbot répond à une personne, et ce registre se retrouve dans le texte final.

- Formules de service : "I hope this helps", "Of course!", "Bien sûr !", "Excellente question", "N'hésitez pas à...", "Faites-moi savoir si...", "Souhaitez-vous que je...", "Would you like...".
- Avertissements didactiques : "It's important to note", "Il est important de noter", "Il convient de souligner", "Il est crucial de se rappeler", "Cela peut varier".
- Précautions de date limite : "as of my last knowledge update", "à ma connaissance", "peu documenté". Puis spéculation pour combler le vide ("cette personne garde un profil discret"). Correction : dire qu'on ne sait pas, sans inventer de raison.
- Ligne "Objet :" ou "Subject:" en tête d'un message qui n'est pas un e-mail. Formules de lettre plaquées ("Chers éditeurs", "Merci pour votre temps et votre considération").
- Gabarits à trous non remplis : "[Nom de l'artiste]", "2025-XX-XX", "INSERT_SOURCE_URL".
- Refus de modèle : "En tant que modèle de langage...".

### Cause 5 : les références produites sans vérification

Le modèle produit l'apparence d'une bibliographie. Ce n'est plus du style, c'est un problème de fiabilité, le plus grave de la liste.

- Liens morts introuvables dans les archives, URL inventées.
- ISBN à somme de contrôle invalide, DOI qui ne mènent nulle part ou vers un autre article.
- Livres réels cités sans page, ou avec une page qui ne soutient pas l'affirmation.
- Source en double (une fois en note, une fois en bibliographie), références déclarées jamais utilisées, une référence collée à chaque phrase.
- Toutes les références au même gabarit, alors que des sources de types différents se citent différemment.
- Hallucinations, affirmations fausses, confusions dues à des homonymes (page française).
- Paramètres de pistage dans les URL : "utm_source=chatgpt.com", "utm_source=copilot.com", "referrer=grok.com".
- Résidus de code de citation : "citeturn0search0", ":contentReference[oaicite:16]{index=16}", "oai_citation", "[attached_file:1]", "<grok-card>", {"attribution":{"attributableIndex":...}}.
- Sources listées en bas de texte hors de toute phrase, signe des sites qui reformulent d'autres sources (page française).

Correction : ne cite que ce que tu as réellement lu ou récupéré dans la session. Si une source manque, écris que l'information n'est pas sourcée au lieu de fabriquer une référence.

### Cause 6 : les ruptures de style

- Style hétérogène : passages à la syntaxe parfaite qui alternent avec des passages pleins d'erreurs (page française). La couture entre partie humaine et partie générée se voit.
- Changement soudain de registre ou de variante de langue (anglais américain sur un sujet indien, français de France sur un sujet québécois sans raison).
- Guillemets et apostrophes courbes mélangés aux droits. Choisis un style et garde-le dans tout le texte. Par défaut, guillemets droits "..." et apostrophe droite ', sauf si l'utilisateur ou le support impose les guillemets français « ».
- Texte coupé en pleine phrase.

### Spécifique à Wikipédia (à appliquer seulement pour du wikitexte)

Markdown ("##", "**gras**") au lieu du wikitexte, wikitexte cassé, catégories ou modèles inexistants (liens rouges), raccourcis de règles inventés (WP:NOTELOCAL), résumés de modification longs et à la première personne, "déclarations de soumission" adressées aux relecteurs, bandeaux de maintenance posés d'avance.

## Ce qui n'est pas un tic

La page anglaise liste des indices inefficaces. Ne les "corrige" pas pour paraître humain, ça dégraderait le texte :

- une grammaire parfaite ;
- un mélange de registres familier et soutenu ;
- une prose sobre ou au contraire soutenue (seuls les mots précis listés plus haut posent problème) ;
- le style d'une lettre quand le texte est une lettre ;
- un "cependant" ou un "notamment" isolé.

N'ajoute pas de fautes volontaires, de familiarités forcées ou d'irrégularités artificielles. Le but est un texte précis, pas un texte maquillé.

## Procédure

### Pour rédiger

1. Rassemble d'abord les faits précis dont tu disposes. S'il n'y en a pas assez pour la longueur demandée, écris plus court plutôt que de remplir.
2. Choisis la forme d'après le contenu. Un raisonnement va en prose. Une liste sert seulement si le lecteur va comparer ou cocher des éléments. Un tableau seulement si plusieurs éléments partagent plusieurs attributs.
3. Rédige en commençant par l'information, sans préambule ("Bien sûr", "Voici", "Excellente question").
4. Arrête-toi quand l'information est donnée, sans résumé final ni offre de suite toute faite.
5. Passe la grille de relecture ci-dessous sur ton propre texte avant de le livrer.

### Pour relire le texte de quelqu'un

1. Repère les tics en citant le passage exact, rangés par cause (pas par ordre d'apparition), pour que l'auteur comprenne le mécanisme et pas seulement la règle.
2. Pour chaque tic, propose une réécriture qui ajoute un fait ou qui coupe. Si la correction demande une information que tu n'as pas, dis-le et pose la question au lieu d'inventer.
3. Signale à part les problèmes de sources (cause 5), parce qu'ils touchent la fiabilité et pas seulement le style.
4. Si l'utilisateur veut seulement le texte corrigé, livre le texte, puis une liste courte des changements.

## Grille de relecture rapide

Relis le texte une fois pour chaque question :

- Une phrase resterait-elle vraie si je changeais le sujet ? Alors elle est creuse.
- Y a-t-il un groupe de trois que je n'ai pas compté exprès ?
- Y a-t-il "ce n'est pas X, c'est Y" ou une variante ?
- Un participe présent en fin de phrase ajoute-t-il un sens vague ?
- Ai-je écrit "sert de", "constitue", "se positionne" là où "est" suffisait ?
- Combien de mots de la liste de vocabulaire IA ? Plus d'un par paragraphe, c'est trop.
- Recherche les caractères "—" et "–" dans tout le texte. Il doit y en avoir zéro : remplace chacun par "-" ou par une virgule, des parenthèses, deux-points.
- Y a-t-il du gras, des émojis, des titres en Title Case ?
- Les listes et tableaux sont-ils justifiés par le contenu ?
- Le texte finit-il par un résumé, une conclusion générale, une offre de service ?
- Chaque source citée a-t-elle été vraiment consultée ?
- Les guillemets et la variante de langue sont-ils cohérents du début à la fin ?

## Vérification automatique

Le dossier `scripts/` contient `check_tics.py`, qui compte les tics de surface d'un ou plusieurs fichiers texte en français :

```bash
python3 scripts/check_tics.py mon-texte.md
```

Il repère les tirets longs, le gras, les émojis, les formules de service et une partie du vocabulaire IA. Il ne juge pas les phrases creuses et peut signaler de faux groupes de trois : sa sortie oriente la relecture, elle ne la remplace pas.

## Priorité des consignes

L'interdiction de "—" et "–" s'applique partout, y compris dans le code, la documentation et les textes en anglais, sauf si l'utilisateur demande expressément ces caractères.

Si l'utilisateur demande explicitement un format (des puces, un tableau, du gras, une conclusion, des guillemets français), son choix passe avant ce skill. Le skill fixe le comportement par défaut, il ne contredit pas une demande explicite. Pour du code, de la documentation technique ou un README, le Markdown est normal : applique les règles de fond et de langue, pas celles de mise en forme.