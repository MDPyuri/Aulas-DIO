-- Complementary inserts: more Pokémon (30+ total)

-- Add extra stages for evolutions not yet covered
INSERT INTO tbl_stages (name, evolves_from, evolution_rule, description)
VALUES
('Stage 1', 'Eevee', 'Must evolve from Eevee.', 'Umbreon evolution'),
('Stage 1', 'Eevee', 'Must evolve from Eevee.', 'Espeon evolution'),
('Stage 1', 'Machop', 'Must evolve from Machop.', 'Machoke evolution'),
('Stage 2', 'Machoke', 'Must evolve from Machoke.', 'Machamp evolution'),
('Stage 1', 'Gastly', 'Must evolve from Gastly.', 'Haunter evolution'),
('Stage 2', 'Haunter', 'Must evolve from Haunter.', 'Gengar evolution'),
('Stage 1', 'Abra', 'Must evolve from Abra.', 'Kadabra evolution'),
('Stage 2', 'Kadabra', 'Must evolve from Kadabra.', 'Alakazam evolution');

-- Add more collections to support the complementary cards
INSERT INTO tbl_collections (id, name, release_date, total_cards)
VALUES
(3, 'Pokémon TCG Collection', '2020-01-01', 20);

-- Add more Pokémon cards (complementary to initial 10)
INSERT INTO tbl_cards (hp, name, type, card_number, collection_id, stage_id, additional_id)
VALUES
(50, 'Bulbasaur', 'Grass', '44/102', 3, 1, NULL),
(80, 'Ivysaur', 'Grass', '2/102', 3, 6, NULL),
(160, 'Venusaur', 'Grass', '15/102', 3, 7, NULL),
(50, 'Squirtle', 'Water', '7/102', 3, 1, NULL),
(80, 'Wartortle', 'Water', '42/102', 3, 8, NULL),
(160, 'Blastoise', 'Water', '2/102', 3, 9, NULL),
(60, 'Jigglypuff', 'Fairy', '54/163', 1, 1, NULL),
(120, 'Wigglytuff GX', 'Fairy', '55/163', 1, 3, 1),
(70, 'Eevee', 'Colorless', '66/163', 1, 1, NULL),
(200, 'Umbreon GX', 'Dark', '67/163', 1, 3, 1),
(200, 'Espeon GX', 'Psychic', '68/163', 1, 3, 1),
(90, 'Machop', 'Fighting', '52/102', 3, 1, NULL),
(130, 'Machoke', 'Fighting', '53/102', 3, 6, NULL),
(190, 'Machamp', 'Fighting', '8/102', 3, 7, NULL),
(70, 'Gastly', 'Psychic', '33/102', 3, 1, NULL),
(100, 'Haunter', 'Psychic', '29/102', 3, 6, NULL),
(150, 'Gengar', 'Psychic', '5/102', 3, 7, NULL),
(60, 'Abra', 'Psychic', '43/102', 3, 1, NULL),
(90, 'Kadabra', 'Psychic', '32/102', 3, 6, NULL),
(150, 'Alakazam', 'Psychic', '1/102', 3, 7, NULL),
(200, 'Dragonite EX', 'Dragon', '74/163', 1, 3, 2),
(300, 'Lapras VMAX', 'Water', '75/163', 1, 3, 3);

-- Add attacks for new Pokémon
INSERT INTO tbl_attacks (card_id, name, energy_cost, damage, effect, attack_rule)
SELECT c.id, 'Vine Whip', '1 Grass', 20, 'Basic attack.', 'No special rule'
FROM tbl_cards c WHERE c.name = 'Bulbasaur'
UNION ALL
SELECT c.id, 'Solar Beam', '4 Grass', 120, 'Standard damage.', 'No special rule'
FROM tbl_cards c WHERE c.name = 'Ivysaur'
UNION ALL
SELECT c.id, 'Bubble', '1 Water', 20, 'May Paralyze opponent.', 'Status effect'
FROM tbl_cards c WHERE c.name = 'Squirtle'
UNION ALL
SELECT c.id, 'Hydro Pump', '4 Water', 120, 'Extra damage per Water energy.', 'Scaling rule'
FROM tbl_cards c WHERE c.name = 'Wartortle'
UNION ALL
SELECT c.id, 'Sing', '2 Colorless', 0, 'Opponent is Asleep.', 'Status effect'
FROM tbl_cards c WHERE c.name = 'Jigglypuff'
UNION ALL
SELECT c.id, 'Fairy Wind', '2 Fairy', 60, 'Standard damage.', 'No special rule'
FROM tbl_cards c WHERE c.name = 'Wigglytuff GX'
UNION ALL
SELECT c.id, 'Moonlight Fang', '2 Dark', 90, 'Prevent damage next turn.', 'Defensive rule'
FROM tbl_cards c WHERE c.name = 'Umbreon GX'
UNION ALL
SELECT c.id, 'Psychic', '2 Psychic', 80, 'Extra damage per energy.', 'Scaling rule'
FROM tbl_cards c WHERE c.name = 'Espeon GX'
UNION ALL
SELECT c.id, 'Seismic Toss', '3 Fighting', 100, 'Standard damage.', 'No special rule'
FROM tbl_cards c WHERE c.name = 'Machop'
UNION ALL
SELECT c.id, 'Shadow Ball', '3 Psychic', 100, 'Opponent discards energy.', 'Energy discard rule'
FROM tbl_cards c WHERE c.name = 'Gengar'
UNION ALL
SELECT c.id, 'Psychic', '3 Psychic', 120, 'Extra damage per energy.', 'Scaling rule'
FROM tbl_cards c WHERE c.name = 'Kadabra'
UNION ALL
SELECT c.id, 'Dragon Claw', '3 Dragon', 130, 'Standard damage.', 'No special rule'
FROM tbl_cards c WHERE c.name = 'Dragonite EX'
UNION ALL
SELECT c.id, 'G-Max Resonance', '4 Water', 250, 'Opponent’s Pokémon is Paralyzed.', 'Status effect'
FROM tbl_cards c WHERE c.name = 'Lapras VMAX';

-- Add abilities for new Pokémon
INSERT INTO tbl_abilities (card_id, name, trigger_condition, effect, usage_limit)
SELECT c.id, 'Overgrow', 'When HP < 30%', 'Increase Grass attack damage by 20.', 'Passive'
FROM tbl_cards c WHERE c.name = 'Ivysaur'
UNION ALL
SELECT c.id, 'Torrent', 'When HP < 30%', 'Increase Water attack damage by 20.', 'Passive'
FROM tbl_cards c WHERE c.name = 'Wartortle'
UNION ALL
SELECT c.id, 'Cute Charm', 'When attacked', 'Opponent may become Infatuated.', 'Passive'
FROM tbl_cards c WHERE c.name = 'Wigglytuff GX'
UNION ALL
SELECT c.id, 'Dark Cloak', 'Always active', 'Free retreat cost for Dark Pokémon.', 'Passive'
FROM tbl_cards c WHERE c.name = 'Umbreon GX'
UNION ALL
SELECT c.id, 'Synchronize', 'When affected by status', 'Opponent also receives status.', 'Passive'
FROM tbl_cards c WHERE c.name = 'Espeon GX'
UNION ALL
SELECT c.id, 'Guts', 'When HP < 50%', 'Increase Fighting attack damage by 40.', 'Passive'
FROM tbl_cards c WHERE c.name = 'Machamp'
UNION ALL
SELECT c.id, 'Levitate', 'Always active', 'Immune to Ground-type attacks.', 'Passive'
FROM tbl_cards c WHERE c.name = 'Gengar'
UNION ALL
SELECT c.id, 'Inner Focus', 'Always active', 'Prevents flinching.', 'Passive'
FROM tbl_cards c WHERE c.name = 'Kadabra'
UNION ALL
SELECT c.id, 'Multiscale', 'When at full HP', 'Reduce damage by half.', 'Passive'
FROM tbl_cards c WHERE c.name = 'Dragonite EX'
UNION ALL
SELECT c.id, 'Shell Armor', 'Always active', 'Reduce damage taken by 30.', 'Passive'
FROM tbl_cards c WHERE c.name = 'Lapras VMAX';
