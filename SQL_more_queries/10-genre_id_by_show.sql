-- SQL query to list all shows with at least one genre linked in the hbtn_0d_tvshows database

-- Query to list all shows with at least one genre linked and sort by title and genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tvshows
JOIN hbtn_0d_tvshows ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
