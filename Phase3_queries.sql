-- Shows which charachters are the same 
SELECT Charachter.name AS Shadow,
    OG.name AS Original
FROM Charachter,
    Charachter AS OG,
    Shadow_Fighter
WHERE Charachter.char_id = Shadow_Fighter.shadow_id
    AND OG.char_id = Shadow_Fighter.og_id;

--search for a character and show its teir 
SELECT Charachter.name AS Name,
    Tier.tier AS Rank
FROM Charachter,
    Tier
WHERE Tier.tier_id = Charachter.tier_id;

--display all characters and their franchise// will be run before entering the loop 
SELECT Charachter.name AS Name,
    Franchise.fran_name AS "From"
FROM Charachter,
    Franchise
WHERE Charachter.fran_id = Franchise.fran_id
ORDER BY Franchise.fran_name;

--select all characters based on a franchise
SELECT Charachter.name AS Name,
    Franchise.fran_name AS 'From'
FROM Charachter,
    Franchise
WHERE Charachter.fran_id = Franchise.fran_id
    AND Franchise.fran_name LIKE '%Donkey%';

--shows dlc names, thier franchise and their rank
SELECT fran_name AS 'Franchise',
    name AS 'Name',
    tier AS 'Tier'
FROM DLC,
    Charachter,
    Tier,
    Franchise
WHERE Charachter.char_id = DLC.char_id
    AND Franchise.fran_id = DLC.fran_id
    AND Charachter.tier_id = Tier.tier_id;

--display pros, the char they play and their rank
SELECT player AS 'Player',
    Charachter.name AS 'Main',
    Tier.tier AS 'Tier',
    OG.name AS 'Alt',
    alt_tier.tier AS 'Tier'
FROM Pros,
    Charachter,
    Tier,
    Charachter AS OG,
    Tier AS alt_tier
WHERE Charachter.char_id = Pros.main
    AND Tier.tier_id = Charachter.tier_id
    AND OG.char_id = Pros.Alt
    AND alt_tier.tier_id = OG.tier_id

