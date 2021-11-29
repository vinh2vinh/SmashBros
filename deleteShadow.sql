
DELETE 
FROM Charachter
WHERE char_id in (SELECT char_id 
                FROM Shadow_Fighter, Character
                WHERE char_id = shadow_id);