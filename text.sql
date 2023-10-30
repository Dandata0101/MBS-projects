
    SELECT *
        
    FROM flights a
    LEFT JOIN carriers b ON a.carrier_id = b.cid
    LEFT JOIN airports c ON a.arrival_aid = c.aid
    LEFT JOIN airports d ON a.departure_aid = d.aid
	


	