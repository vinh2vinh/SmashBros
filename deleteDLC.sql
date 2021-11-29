DELETE 
FROM Charachter
WHERE char_id in (SELECT char_id 
                FROM DLC, Character
                WHERE Character.char_id = DLC.char_id);