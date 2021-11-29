INSERT INTO Charachter
WHERE char_id in (SELECT char_id 
                FROM Shadow_Fighter, Character
                WHERE Charachter.char_id = Shadow_Fighter.shadow_id)
;