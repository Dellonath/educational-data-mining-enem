SELECT 
	*
FROM tfg.enem 
WHERE 
	rand() < 0.0030683 AND
    father_schooling IS NOT NULL;