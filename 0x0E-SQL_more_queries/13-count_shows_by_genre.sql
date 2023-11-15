-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked
SELECT tb_genres.name AS `genre`, COUNT(*) AS `number_of_shows` FROM tv_genres INNER JOIN tv_show_genres.genre_id GROUP BY tv_genres.name ORDER BY number_of_shows DESC;
