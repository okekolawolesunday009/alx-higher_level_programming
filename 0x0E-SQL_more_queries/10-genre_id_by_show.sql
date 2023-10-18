 -- import the required database
-- write the scipt that liist all the details of shows wit h their id
-- only use one select statement
-- etc

SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows 
JOIN tv_show_genres
ON show_id = tv_show_genres.show_id
ORDER BY tv_shows.title ,tv_show_genres.genre_id;

