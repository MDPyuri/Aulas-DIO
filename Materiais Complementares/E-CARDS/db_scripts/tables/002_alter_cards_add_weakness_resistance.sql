USE pokemontcg_db;

-- Add weakness and resistance fields to the cards table
ALTER TABLE tbl_cards
    ADD COLUMN weakness VARCHAR(100) NULL AFTER additional_id,
    ADD COLUMN resistance VARCHAR(100) NULL AFTER weakness;
