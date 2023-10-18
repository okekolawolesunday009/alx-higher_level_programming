-- same database with task 11
-- rsult should show null if no record if the genre has no show

SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, 0)
FROM tv_shows
JOIN tv_show_genres
ON show_id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
