USE pokemontcg_db;

-- Populate weakness and resistance on all cards already inserted
UPDATE tbl_cards
SET weakness = CASE name
    WHEN 'Decidueye GX' THEN 'Fire, Flying'
    WHEN 'Rowlet' THEN 'Fire, Flying'
    WHEN 'Dartrix' THEN 'Fire, Flying'
    WHEN 'Charizard GX' THEN 'Water, Rock'
    WHEN 'Charmander' THEN 'Water, Rock'
    WHEN 'Charmeleon' THEN 'Water, Rock'
    WHEN 'Pikachu' THEN 'Fighting'
    WHEN 'Mewtwo GX' THEN 'Psychic'
    WHEN 'Rayquaza EX' THEN 'Ice'
    WHEN 'Snorlax VMAX' THEN 'Fighting'
    WHEN 'Bulbasaur' THEN 'Fire, Psychic'
    WHEN 'Ivysaur' THEN 'Fire, Psychic'
    WHEN 'Venusaur' THEN 'Fire, Psychic'
    WHEN 'Squirtle' THEN 'Electric, Grass'
    WHEN 'Wartortle' THEN 'Electric, Grass'
    WHEN 'Blastoise' THEN 'Electric, Grass'
    WHEN 'Jigglypuff' THEN 'Fighting'
    WHEN 'Wigglytuff GX' THEN 'Fighting'
    WHEN 'Eevee' THEN 'Fighting'
    WHEN 'Umbreon GX' THEN 'Fighting'
    WHEN 'Espeon GX' THEN 'Dark'
    WHEN 'Machop' THEN 'Psychic'
    WHEN 'Machoke' THEN 'Psychic'
    WHEN 'Machamp' THEN 'Psychic'
    WHEN 'Gastly' THEN 'Dark'
    WHEN 'Haunter' THEN 'Dark'
    WHEN 'Gengar' THEN 'Dark'
    WHEN 'Abra' THEN 'Psychic'
    WHEN 'Kadabra' THEN 'Psychic'
    WHEN 'Alakazam' THEN 'Psychic'
    WHEN 'Dragonite EX' THEN 'Ice'
    WHEN 'Lapras VMAX' THEN 'Electric, Grass'
    ELSE NULL
END,
resistance = CASE name
    WHEN 'Decidueye GX' THEN 'Water, Fighting'
    WHEN 'Rowlet' THEN NULL
    WHEN 'Dartrix' THEN NULL
    WHEN 'Charizard GX' THEN 'Fighting'
    WHEN 'Charmander' THEN NULL
    WHEN 'Charmeleon' THEN NULL
    WHEN 'Pikachu' THEN NULL
    WHEN 'Mewtwo GX' THEN 'Fighting'
    WHEN 'Rayquaza EX' THEN 'Fighting'
    WHEN 'Snorlax VMAX' THEN NULL
    WHEN 'Bulbasaur' THEN 'Water, Electric'
    WHEN 'Ivysaur' THEN 'Water, Electric'
    WHEN 'Venusaur' THEN 'Water, Electric'
    WHEN 'Squirtle' THEN NULL
    WHEN 'Wartortle' THEN NULL
    WHEN 'Blastoise' THEN NULL
    WHEN 'Jigglypuff' THEN NULL
    WHEN 'Wigglytuff GX' THEN NULL
    WHEN 'Eevee' THEN NULL
    WHEN 'Umbreon GX' THEN 'Psychic'
    WHEN 'Espeon GX' THEN 'Psychic'
    WHEN 'Machop' THEN NULL
    WHEN 'Machoke' THEN NULL
    WHEN 'Machamp' THEN NULL
    WHEN 'Gastly' THEN NULL
    WHEN 'Haunter' THEN NULL
    WHEN 'Gengar' THEN NULL
    WHEN 'Abra' THEN NULL
    WHEN 'Kadabra' THEN NULL
    WHEN 'Alakazam' THEN NULL
    WHEN 'Dragonite EX' THEN 'Fighting'
    WHEN 'Lapras VMAX' THEN NULL
    ELSE NULL
END;
