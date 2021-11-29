SELECT name, fran_name AS franchise, EGSP AS GlobalSmashPower, tier
FROM Charachter, Franchise, GSP, Tier
WHERE Charachter.fran_id = Franchise.fran_id
AND Charachter.char_id = GSP.char_id
AND Charachter.tier_id = Tier.tier_id
;