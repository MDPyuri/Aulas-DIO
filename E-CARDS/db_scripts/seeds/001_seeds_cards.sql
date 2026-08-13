-- Insert sample collections
INSERT INTO tbl_collections (name, release_date, total_cards)
VALUES 
('Hidden Fates', '2019-08-23', 163),
('Shining Legends', '2017-10-06', 73);

-- Insert sample stages
INSERT INTO tbl_stages (name, evolves_from, evolution_rule, description)
VALUES
('Basic', NULL, 'Can be played directly onto the field.', 'Starting stage Pokémon'),
('Stage 1', 'Rowlet', 'Must evolve from Rowlet.', 'Intermediate evolution'),
('Stage 2', 'Dartrix', 'Must evolve from Dartrix.', 'Final evolution stage'),
('Stage 1', 'Charmander', 'Must evolve from Charmander.', 'Charmeleon evolution'),
('Stage 2', 'Charmeleon', 'Must evolve from Charmeleon.', 'Charizard evolution');

-- Insert sample additionals
INSERT INTO tbl_additionals (name, rule_effect, limit_per_deck, description)
VALUES
('GX', 'When knocked out, opponent takes 2 prize cards.', 4, 'Special GX Pokémon'),
('EX', 'When knocked out, opponent takes 2 prize cards.', 4, 'Older EX mechanic'),
('VMAX', 'When knocked out, opponent takes 3 prize cards.', 4, 'Gigantamax Pokémon');

-- Insert sample cards (10 Pokémon)
INSERT INTO tbl_cards (hp, name, type, card_number, collection_id, stage_id, additional_id)
VALUES
(240, 'Decidueye GX', 'Grass', '10/163', 1, 3, 1),
(60, 'Rowlet', 'Grass', '1/73', 2, 1, NULL),
(90, 'Dartrix', 'Grass', '2/73', 2, 2, NULL),
(150, 'Charizard GX', 'Fire', '9/163', 1, 5, 1),
(70, 'Charmander', 'Fire', '3/73', 2, 1, NULL),
(90, 'Charmeleon', 'Fire', '4/73', 2, 4, NULL),
(130, 'Pikachu', 'Electric', '25/163', 1, 1, NULL),
(180, 'Mewtwo GX', 'Psychic', '39/163', 1, 3, 1),
(200, 'Rayquaza EX', 'Dragon', '60/163', 1, 3, 2),
(320, 'Snorlax VMAX', 'Colorless', '45/163', 1, 3, 3);

-- Insert sample attacks
INSERT INTO tbl_attacks (card_id, name, energy_cost, damage, effect, attack_rule)
VALUES
(1, 'Razor Leaf', '2 Grass', 90, 'Standard damage attack.', 'No special rule'),
(2, 'Tackle', '1 Colorless', 10, 'Basic attack.', 'No special rule'),
(3, 'Leaf Blade', '2 Grass', 50, 'Flip a coin, extra damage.', 'Conditional rule'),
(4, 'Flamethrower', '3 Fire', 150, 'Discard 1 Fire energy.', 'Energy discard rule'),
(5, 'Scratch', '1 Fire', 20, 'Basic attack.', 'No special rule'),
(6, 'Fire Fang', '2 Fire', 60, 'Burns opponent.', 'Status effect'),
(7, 'Thunderbolt', '3 Electric', 100, 'Discard all energy.', 'Energy discard rule'),
(8, 'Psychic Nova GX', '3 Psychic', 200, 'GX attack, once per game.', 'GX rule'),
(9, 'Dragon Burst', '3 Fire/Lightning', 180, 'Discard chosen energy.', 'Energy discard rule'),
(10, 'G-Max Snooze', '4 Colorless', 220, 'Opponent is Asleep.', 'Status effect');

-- Insert sample abilities
INSERT INTO tbl_abilities (card_id, name, trigger_condition, effect, usage_limit)
VALUES
(1, 'Feather Arrow', 'Once per turn', 'Place 2 damage counters on opponent’s Pokémon.', 'Unlimited'),
(4, 'Blaze', 'When HP < 50%', 'Increase Fire attack damage by 30.', 'Passive'),
(7, 'Static', 'When attacked', 'Opponent’s Pokémon may become Paralyzed.', 'Passive'),
(8, 'Pressure', 'Always active', 'Opponent’s attacks cost 1 extra energy.', 'Passive'),
(9, 'Air Lock', 'Always active', 'Negates weather effects.', 'Passive'),
(10, 'Thick Fat', 'Always active', 'Reduce damage from Fire and Ice attacks.', 'Passive');
