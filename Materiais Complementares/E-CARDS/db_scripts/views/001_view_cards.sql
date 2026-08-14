DROP VIEW IF EXISTS vw_cards;

CREATE VIEW vw_cards AS
SELECT
    c.id AS card_id,
    c.hp,
    c.name AS card_name,
    c.type,
    c.card_number,
    col.name AS collection_name,
    st.name AS stage_name,
    ad.name AS additional_name,
    c.weakness,
    c.resistance
FROM tbl_cards AS c
LEFT JOIN tbl_collections AS col ON c.collection_id = col.id
LEFT JOIN tbl_stages AS st ON c.stage_id = st.id
LEFT JOIN tbl_additionals AS ad ON c.additional_id = ad.id;
