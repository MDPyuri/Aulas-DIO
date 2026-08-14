DROP DATABASE IF EXISTS pokemontcg_db;
CREATE DATABASE pokemontcg_db;
USE pokemontcg_db;

-- Table for Pokémon TCG collections
CREATE TABLE tbl_collections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    release_date DATE NOT NULL,
    total_cards INT NOT NULL
);

-- Table for card evolution stages (Basic, Stage 1, Stage 2, etc.)
CREATE TABLE tbl_stages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    evolves_from VARCHAR(100),
    evolution_rule TEXT,
    description TEXT
);

-- Table for additional card types (EX, GX, V, VMAX, etc.)
CREATE TABLE tbl_additionals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    rule_effect TEXT,
    limit_per_deck INT DEFAULT 4,
    description TEXT
);

-- Table for Pokémon TCG cards
CREATE TABLE tbl_cards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hp INT,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50),
    card_number VARCHAR(20),
    collection_id INT,
    stage_id INT,
    additional_id INT,
    FOREIGN KEY (collection_id) REFERENCES tbl_collections(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (stage_id) REFERENCES tbl_stages(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (additional_id) REFERENCES tbl_additionals(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Table for attacks (each card can have multiple attacks)
CREATE TABLE tbl_attacks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    card_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    energy_cost VARCHAR(100),
    damage INT,
    effect TEXT,
    attack_rule TEXT,
    FOREIGN KEY (card_id) REFERENCES tbl_cards(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Table for abilities (passive or triggered effects)
CREATE TABLE tbl_abilities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    card_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    trigger_condition TEXT,
    effect TEXT,
    usage_limit VARCHAR(50),
    FOREIGN KEY (card_id) REFERENCES tbl_cards(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
